# Source: https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/


## Base image
### This installs a Python image into the Docker image.
### This is also the version of Python that will run the application in the container
#FROM python:3.9
FROM python:3.9.6-alpine

# set work directory
WORKDIR /home/jerneja/GitHubProjects/self-check-in-kiosk/kiosk

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
#RUN apt update
#RUN apt-get -y install pipenv
#RUN pipenv install
# WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager.
#RUN pip install --upgrade pip
#RUN pip install pipenv
#RUN pipenv install

RUN pip install pipenv
COPY Pipfile /tmp
COPY Pipfile.lock /tmp
RUN cd /tmp && pipenv requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

# copy project
COPY kiosk .




# ------------------------------------


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

