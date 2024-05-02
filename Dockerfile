# Build the frontend
FROM node:20 as frontend

COPY package.json pnpm-lock.yaml postcss.config.js tailwind.config.js webpack.config.js ./
COPY ./yotta/static_src/ ./yotta/static_src/
COPY ./yotta/templates ./yotta/templates 

RUN npm install -g pnpm
RUN pnpm install && pnpm run build


# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:3.12.2-bullseye as production

ARG POETRY_INSTALL_ARGS="--only main"

# IMPORTANT: Remember to review both of these when upgrading
ARG POETRY_VERSION=1.5.1

# Install dependencies in a virtualenv
ENV VIRTUAL_ENV=/venv

RUN useradd wagtail --create-home && mkdir /app $VIRTUAL_ENV && chown -R wagtail /app $VIRTUAL_ENV

WORKDIR /app

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PATH=$VIRTUAL_ENV/bin:$PATH \
    POETRY_INSTALL_ARGS=${POETRY_INSTALL_ARGS} \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=yotta.settings.production \
    PORT=8000 \
    WEB_CONCURRENCY=3 \
    GUNICORN_CMD_ARGS="-c gunicorn-conf.py --max-requests 1200 --max-requests-jitter 50 --access-logfile - --timeout 25"

# Make $BUILD_ENV available at runtime
ARG BUILD_ENV
ENV BUILD_ENV=${BUILD_ENV}

# Port exposed by this container. Should default to the port used by your WSGI
# server (Gunicorn). This is read by Dokku only. Heroku will ignore this.
EXPOSE 8000

# Install poetry at the system level
RUN pip install --no-cache poetry==${POETRY_VERSION}

# Use /app folder as a directory where the source code is stored.
WORKDIR /app

# Add bash commands
COPY scripts/bash.sh /home/wagtail/.bashrc

# Install your app's Python requirements.
RUN python -m venv $VIRTUAL_ENV
COPY --chown=wagtail pyproject.toml poetry.lock ./
RUN pip install --no-cache --upgrade pip && poetry install ${POETRY_INSTALL_ARGS} --no-root --extras gunicorn && rm -rf $HOME/.cache

COPY --chown=wagtail --from=frontend ./yotta/static_compiled ./yotta/static_compiled

# Copy application code.
COPY --chown=wagtail . .

# Run poetry install again to install our project (so the the wagtail package is always importable)
RUN poetry install ${POETRY_INSTALL_ARGS}

RUN SECRET_KEY=none python manage.py collectstatic --noinput --clear

# Run the WSGI server. It reads GUNICORN_CMD_ARGS, PORT and WEB_CONCURRENCY
# environment variable hence we don't specify a lot options below.
CMD gunicorn yotta.wsgi:application

FROM production as development

# Install `psql`, useful for `manage.py dbshell`
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    postgresql-client jpegoptim pngquant gifsicle libjpeg-progs webp \
    && apt-get autoremove && rm -rf /var/lib/apt/lists/*

CMD tail -f /dev/null