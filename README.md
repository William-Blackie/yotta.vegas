# Yotta Vegas Proof of Concept Wagtail Site
[yottta.developerfy.com](yotta.developerfy.com)

## Overview

Welcome to the Yotta Vegas Proof of Concept (PoC) Wagtail site. This project aims to demonstrate the capabilities and features of the Wagtail CMS for managing and delivering content for Yotta Vegas.
All IP belongs to Yotta.vegas, this is simply a demonstration used in a pitch.

## Features

- **Content Management**: Utilize Wagtail's intuitive admin interface to create and manage content effortlessly.
- **Custom Page Types**: Leverage custom page types to suit the specific needs of Yotta Vegas.
- **Rich Text Editing**: Enhance content with custom RichText features and StreamFields.
- **Accessibility**: Ensure the site meets WCAG accessibility standards.
- **Responsive Design**: Deliver a seamless experience across devices with a fully responsive design.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/William-Blackie/William-Blackie/yotta.vegas
    cd yotta.vegas
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install the dependencies(requires fabric)**:
    ```bash
    fab start
    ```

4. **Enter the dev' server**:
   ```
   fab sh
   ```
   
5. **Apply migrations**:
    ```bash
    dj migrate
    ```

6. **Create a superuser**:
    ```bash
    dj createsuperuser
    ```

7. **Run the development server**:
    ```bash
    djrun
    ```

8. **Access the admin interface**:
    - Open your web browser and navigate to `http://127.0.0.1:8000/admin/`
    - Log in using the superuser credentials created earlier.

## Usage

- **Creating Pages**: Use the Wagtail admin interface to create and manage pages. Utilize custom page types and StreamFields to build complex page structures.
- **Managing Content**: Add and edit content using Wagtail's rich text editor. Ensure content adheres to WCAG accessibility standards.
- **Previewing Changes**: Preview changes before publishing to see how they will appear on the live site.

## Deployment

For deployment, it is recommended to use a production-ready web server like Gunicorn with a reverse proxy (e.g., Nginx) and a PostgreSQL database. Ensure all static files are collected and served correctly.
