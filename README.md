# billing_api

Billing API

This project was generated with [`wemake-django-template`](https://github.com/wemake-services/wemake-django-template). Current template version is: [31c2edde417409103b5445e84a2a18d95e215dc9](https://github.com/wemake-services/wemake-django-template/tree/31c2edde417409103b5445e84a2a18d95e215dc9). See what is [updated](https://github.com/wemake-services/wemake-django-template/compare/31c2edde417409103b5445e84a2a18d95e215dc9...master) since then.


## Prerequisites

You will need:

- `python3.9`
- `postgresql 12`
- `django 4.1.1`


## Development

When developing locally, we use:

- [`editorconfig`](http://editorconfig.org/) plugin (**required**)
- `virtualenv` (optional)
- `pycharm 2022.2.2` (optional)


## Documentation

# Database Creation on Postgresql
$CREATE DATABASE billing_api WITH ENCODING='UTF8' OWNER=postgres CONNECTION LIMIT=25;

# SSL Keys for JWT
Generate SSL private and public key for SSL. The dev server comes with a set

# Environment Variables
Create .env file under /config director. Use .env.template as a base

# Migrations
$python manage.py makemigrations
$python manage.py migrate

#Create User
$python manage.py createsuperuser
- username: biller
- email: biller@billing-api.xyz
- password: biller101

# Run the application on your dev terminal
$python manage.py runserver_plus 0.0.0.0:8000

# Access Django Admin on web browser & login with username and password created above
http://127.0.0.1:8000/admin/

Full documentation is available here: [`docs/`](docs).
