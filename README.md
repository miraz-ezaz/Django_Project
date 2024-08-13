# PropertyInfo Django Project

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Clone the Project](#clone-the-project)
  - [Create a Virtual Environment](#create-a-virtual-environment)
  - [Install Packages](#install-packages)
  - [Create PostgreSQL Databases](#create-postgresql-databases)
  - [Setup the `.env` File](#setup-the-env-file)
- [Django Models](#django-models)
- [Database Migrations](#database-migrations)
- [Create a Superuser](#create-a-superuser)
- [Run the Development Server](#run-the-development-server)
- [Access the Admin Interface](#access-the-admin-interface)
- [CLI Application](#cli-application)
  - [Available Commands](#available-commands)
  - [How to Run the Commands](#how-to-run-the-commands)

## Introduction

PropertyInfo is a Django-based project designed to manage hotel information and associated images. It includes a command-line interface (CLI) application to fetch and manage data from a database that contains scraped data about hotels.

## Getting Started

### Clone the Project

Start by cloning the repository from GitHub:

```bash
git clone https://github.com/miraz-ezaz/Django_Project.git
cd Django_Project
```

### Create a Virtual Environment

Create a virtual environment using `venv`:

```bash
python3 -m venv venv
```

Activate the virtual environment:

- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- On **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### Install Packages

Install all required packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Create PostgreSQL Databases

Create a PostgreSQL databases: For the Django project (`default_db`)

1. Open the PostgreSQL command-line tool:

   ```bash
   psql -U postgres
   ```

2. Create the database:

   ```sql
   CREATE DATABASE default_db_name;
   ```

3. Create users and set privileges if necessary.

### Setup the `.env` File

Create a `.env` file in the `propertyInfo` folder with the following contents:

```plaintext
# .env file for Django project configuration

# Default Database Configuration
DEFAULT_DB_ENGINE=django.db.backends.postgresql
DEFAULT_DB_NAME=default_db_name
DEFAULT_DB_USER=db_user
DEFAULT_DB_PASSWORD=db_password
DEFAULT_DB_HOST=localhost
DEFAULT_DB_PORT=5432

# Scrap Database Configuration
SCRAP_DB_ENGINE=django.db.backends.postgresql
SCRAP_DB_NAME=scrap_db_name
SCRAP_DB_USER=scrap_db_user
SCRAP_DB_PASSWORD=scrap_db_password
SCRAP_DB_HOST=localhost
SCRAP_DB_PORT=5432

# Scrapy Image Directory
SCRAPY_IMAGE_DIR=/home/youruser/pathe/to/Scrapy/Project/hotel_spider/
```

Replace the placeholders with your actual database credentials and file paths.

## Django Models

The project includes the following models:

- **Hotel**: Manages hotel information.
- **Image**: Stores images associated with hotels.
- **Location** and **Amenity**: Manage hotel locations and amenities respectively.

## Database Migrations

Run the following commands to apply the migrations and set up the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Create a Superuser

Create a superuser to access the Django admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin user.

## Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

## Access the Admin Interface

Visit the admin interface in your web browser:

```
http://127.0.0.1:8000/admin/
```

Log in with the superuser credentials you created earlier. You can now perform CRUD operations on the `Hotel`, `Image`, `Location`, and `Amenity` models.

## CLI Application

The project includes a CLI application (`fetchHotelDataCLI`) with several commands to manage data.

### Available Commands

1. **`view_all_hotels`**: Display all hotel details from the `scrapdb` database.
   ```bash
   python manage.py fetch_data view_all_hotels
   ```

2. **`insert_into_database`**: Insert hotels and associated images into the default database from the `scrapdb` database. It skips hotels that already exist.
   ```bash
   python manage.py fetch_data insert_into_database
   ```

3. **`insert_only_images`**: Insert images for existing hotels in the default database from the `scrapdb` database.
   ```bash
   python manage.py fetch_data insert_only_images
   ```

### How to Run the Commands

Each command can be executed using the `manage.py` script with the `fetch_data` management command:

```bash
python manage.py fetch_data <subcommand>
```

Replace `<subcommand>` with the specific command you want to run (e.g., `view_all_hotels`, `insert_into_database`, `insert_only_images`).

