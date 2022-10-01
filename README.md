# Billing API

Billing API

This project was generated with [`wemake-django-template`](https://github.com/wemake-services/wemake-django-template). Current template version is: [31c2edde417409103b5445e84a2a18d95e215dc9](https://github.com/wemake-services/wemake-django-template/tree/31c2edde417409103b5445e84a2a18d95e215dc9). See what is [updated](https://github.com/wemake-services/wemake-django-template/compare/31c2edde417409103b5445e84a2a18d95e215dc9...master) since then.


## Prerequisites

You will need:

- `python 3.9.13`
- `postgresql 12`
- `django 4.1.1`
- `poetry`
- `docker`


## Development

When developing locally, we use:

- [`editorconfig`](http://editorconfig.org/) plugin (**required**)
- `pycharm 2022.2.2` (optional)



# Getting Started

## Environment Variables
Create a .env file under `/config` directory. Use `.env.template` as a base

## Bring up the containers
`#docker-compose up --build`

## You can confirm if the containers are running
`$docker ps`

## Run Migrations to create DB Tables
$docker-compose exec api python manage.py migrate

## Create Django User
`$docker-compose exec api python manage.py createsuperuser`
- username: biller
- email: biller@billing-api.xyz
- password: biller101

## Access Django Admin on web browser 
login with username and password created above

- URL: http://127.0.0.1:8000/admin/



## Extra details
___

Use the command below to access your database from the terminal (username and password
are as per your .env file in `/config` directory)

`$docker-compose exec db psql --username=POSTGRES_USER --dbname=POSTGRES_USER`

## Access PostgreSQL and Redis from your localhost
## postgresql: 
  - Host: `localhost`
  - Username: value in `POSTGRES_USER` in .env
  - Password: (blank i.e. no password)
  - Port: `6432` (This can be changed in `docker-compose.override.yml`)
  
## redis: 
  - Host: `localhost`
  - Password: (blank i.e. no password) 
  - Port: `7379` (This can be changed in `docker-compose.override.yml`)
  

Full documentation is available here: [`docs/`](docs).
