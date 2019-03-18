# SFDS Prereqs [![CircleCI](https://circleci.com/gh/SFDigitalServices/prereqs.svg?style=svg)](https://circleci.com/gh/SFDigitalServices/prereqs)

A service for keeping track of prerequisites and dependencies.
Jumpstarted with [SFDS microservice.py](https://github.com/SFDigitalServices/microservice-py)

## Getting started

Install python3
Install and start postgresql 11.2
Set environment variable for db connection string
> \$ export DATABASE_URL=postgres://$(whoami)

Install pipenv
Create virtual environment and install dependencies
> \$ pipenv install

Activate the pipenv shell
> \$ pipenv shell

Exit the pipenv shell
> \$ exit

Added a package to the project
> \$ pipenv install <package>

Start WSGI Server
> \$ gunicorn 'service.microservice:start_service()'

Run Pytest
> \$ pytest tests

Open with cURL or web browser
> \$ curl http://127.0.0.1:8000/welcome

