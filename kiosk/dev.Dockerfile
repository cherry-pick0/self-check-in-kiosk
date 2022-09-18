# Source: https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

# Base image
## This installs a Python image into the Docker image.
## This is also the version of Python that will run the application in the container
FROM python:3.9.6-alpine

# Setup environment variable
## Here we declare the working directory and assign it to the variable name DockerHOME.
## This will be the root directory of the Django app in the container
ENV DockerHOME=/usr/src/kiosk/
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
## This creates the directory with the specified path assigned to
## the DockerHOME variable within the image
RUN mkdir -p $DockerHOME

# Where your code lives
## This explicitly tells Docker to set the provided directory as
## the location where the application will reside within the container
WORKDIR $DockerHOME

# Install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Install dependencies
RUN pip install pipenv
# Note: why not pipenv install?
# Workaround for requirements.txt
COPY Pipfile /tmp
COPY Pipfile.lock /tmp
RUN cd /tmp && pipenv requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

# Copy whole project to your docker home directory.
COPY . $DockerHOME

RUN sed -i 's/\r$//g' $DockerHOME/entrypoint.dev.sh
RUN chmod +x $DockerHOME/entrypoint.dev.sh

# Run entrypoint.sh to verify that Postgres is healthy
# before applying the migrations and running the
# Django development server
ENTRYPOINT ["./entrypoint.dev.sh"]



################################################################

## Base image
### This installs a Python image into the Docker image.
### This is also the version of Python that will run the application in the container
#FROM python:3.9
#
## Setup environment variable
### Here we declare the working directory and assign it to the variable name DockerHOME.
### This will be the root directory of the Django app in the container
#ENV DockerHOME=/home/jerneja/GitHubProjects/self-check-in-kiosk
#
## Set work directory
### This creates the directory with the specified path assigned to
### the DockerHOME variable within the image
#RUN mkdir -p $DockerHOME
#
## Where your code lives
### This explicitly tells Docker to set the provided directory as
### the location where the application will reside within the container
#WORKDIR $DockerHOME
#
## Set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
## Install dependencies
### This updates the pip version that will be used to install
### the dependencies for the application
##RUN pip install --upgrade pip
#
## Copy whole project to your docker home directory.
## COPY . $DockerHOME
#
## Install python dependencies in /.venv
#COPY Pipfile .
#COPY Pipfile.lock .
#
## Run this command to install all dependencies
#RUN apt update
#RUN apt-get -y install pipenv
#RUN pipenv install
## port where the Django app runs
#EXPOSE 8000
## start server
#CMD python manage.py runserver

