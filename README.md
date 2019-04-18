# SFDS Prereqs [![CircleCI](https://circleci.com/gh/SFDigitalServices/prereqs.svg?style=svg)](https://circleci.com/gh/SFDigitalServices/prereqs)

A service for keeping track of prerequisites and dependencies.
Jumpstarted with [SFDS microservice.py](https://github.com/SFDigitalServices/microservice-py)

## Getting started

Install python3
Install and start postgresql 11.2
Set environment variable for db connection string, assumes that you have a database named with your username
> \$ export DATABASE_URL=postgres://localhost/$(whoami)

Install pipenv
Create virtual environment and install dependencies
> \$ pipenv install

Activate the pipenv shell
> \$ pipenv shell

Start WSGI Server
> \$ gunicorn 'service.microservice:start_service()'

Run Pytest
> \$ pytest tests

Open with cURL or web browser
> \$ curl http://127.0.0.1:8000/welcome

Run DB migrations
> alembic upgrade head

Exit the pipenv shell
> \$ exit


## Useful commands
Add a package to the project
> \$ pipenv install \<package>

Remove a package
> \$ pipenv uninstall \<package>

Create a migration
> alembic revision -m "Add a column"

## Good to know

When running migrations, if you see an error which looks like
`sqlalchemy.exc.ProgrammingError: (psycopg2.ProgrammingError) function uuid_generate_v4() does not exist`
Connect to the psql database and run `CREATE EXTENSION IF NOT EXISTS "uuid-ossp";`
https://stackoverflow.com/questions/22446478/extension-exists-but-uuid-generate-v4-fails