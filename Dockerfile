# Build the frontend
FROM node:20 as frontend

COPY package.json pnpm-lock.yaml postcss.config.js tailwind.config.js webpack.config.js ./
COPY ./yotta/static_src/ ./yotta/static_src/
COPY ./yotta/templates ./yotta/templates 

RUN npm install -g pnpm
RUN pnpm install && pnpm run build


# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:3.12.2-bullseye as backend

# Add user that will be used in the container.
RUN useradd wagtail

# Port used by this container to serve HTTP.
EXPOSE 8000

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PYTHONUNBUFFERED=1 \
    PORT=8000

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadb-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    gnupg2 \
    && rm -rf /var/lib/apt/lists/*

# Purge old postgresql packages.
RUN apt-get purge -y postgresql\*

RUN curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc|gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
RUN echo "deb https://apt.postgresql.org/pub/repos/apt bullseye-pgdg main" > /etc/apt/sources.list.d/pgdg.list
RUN apt-get update && apt-get install -y postgresql-client-16

# Configure Poetry
ENV POETRY_HOME="/opt/poetry" \
    POETRY_VERSION=1.3.2

# Add `poetry` to PATH
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=${POETRY_VERSION} python3 - \
    && chmod 755 ${POETRY_HOME}/bin/poetry

# Use /app folder as a directory where the source code is stored.
WORKDIR /app

# Add bash commands
COPY scripts/bash.sh /home/wagtail/.bashrc

# Install dependencies
COPY poetry.lock pyproject.toml ./

RUN /bin/true\
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction \
    && rm -rf /root/.cache/pypoetry

# Set this directory to be owned by the "wagtail" user. 
RUN chown wagtail:wagtail /app -R && chown wagtail:wagtail /home/wagtail -R

# Copy the source code of the project into the container.
COPY --chown=wagtail:wagtail . .
COPY --from=frontend ./yotta/static_compiled ./yotta/static_compiled

# Use user "wagtail" to run the build commands below and the server itself.
USER wagtail

# Collect static files.
RUN python manage.py collectstatic --noinput --clear

# Install the application server.
RUN pip install "gunicorn==20.0.4"

# Runtime command that executes when "docker run" is called, it does the
# following:
#   1. Migrate the database.
#   2. Start the application server.
# WARNING:
#   Migrating database at the same time as starting the server IS NOT THE BEST
#   PRACTICE. The database should be migrated manually or using the release
#   phase facilities of your hosting platform. This is used only so the
#   Wagtail instance can be started with a simple "docker run" command.
CMD set -xe; python manage.py migrate --noinput; gunicorn yotta.wsgi:application
