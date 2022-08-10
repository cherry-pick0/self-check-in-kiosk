# Self-check-in-kiosk

Track actions and status here:
https://trello.com/b/coUnjV9y/backend

Owner of the project: bozic.jerneja@gmail.com; cherry-pick0

---------------------------------------------------------

Disclaimer: instructions written for ubuntu 20.04

##Background

Install:

- python: Python 3.8.10

- PostgreSQL (database server): 12.11 (Ubuntu 12.11-0ubuntu0.20.04.1); you will need Psycopg (adapter for Python)


        # Install Postgres
        sudo apt install postgresql postgresql-contrib
        
        # Run and check the status
        sudo systemctl start postgresql.service
        sudo systemctl status postgresql.service

- pipenv (tool; Pipfile, pip, and virtualenv in one single command): version 2020.8.13


        sudo apt update
        sudo apt-get -y install pipenv


- make: automation tool for running commands (version GNU Make 4.2.1)

        
        sudo apt update
        sudo apt install make

- pre-commit (2.6.0)

        
        sudo apt update
        # Snaps are applications packaged with all their dependencies
        sudo apt install snapd
        sudo snap install pre-commit --classic

##Setup the project (follow steps)

        pipenv shell
        pipenv install

## Steps of creating this project (notes)

####1. Activate the environment (this command creates or activates virtual environment)

        pipenv shell

   This will create a new virtual environment with Pipfile

        (self-check-in-kiosk) jerneja@jerneja:~/GitHubProjects/self-check-in-kiosk$

####2. Install django and other dependencies

   This will install dependencies in our virtual environment.


        pipenv install django
        pipenv install djangorestframework
        pipenv install django-cors-headers
        # Note: pipenv install psycopg2 does not work
        pipenv install psycopg2-binary
        
        # Development dependencies
        pipenv install black --dev
        pipenv install pre-commit --dev
        pipenv install flake8 --dev
        pipenv install isort --dev
        

Notes on dev dependencies

* [Black: Python code formatter](https://github.com/psf/black) & [Setup black for PyCharm](https://godatadriven.com/blog/partial-python-code-formatting-with-black-pycharm/)
* [pre-commit](https://pre-commit.com/): run on commit
* [Flake8](https://flake8.pycqa.org/en/latest/): helps prevent things like syntax errors, typos, bad formatting, incorrect styling, follows pep8 etc.
* [isort](https://pypi.org/project/isort/): sorts imports


####3. Create a django project

        django-admin startproject kiosk
        # Add 'kiosk' to INSTALLED_APPS in settings.py
        
   ##### 3.1 Check if django server is running
   
        cd kiosk
        python manage.py runserver
   or
   
        make runserver
        
   ##### 3.2 Create your models (only example)
   
        python manage.py startapp registrations
        python manage.py makemigrations
   
####4. Add configuration files:

    - pre-commit: .pre-commit-config.yaml and run "pre-commit install"
    - black: pyproject.toml
    
####5. Setup db
        # Create local db
        sudo -u postgres createdb kioskdb
            
        # Enter postgres
        sudo -u postgres psql
        
        # Create new user and grant privileges
        CREATE USER kiosk WITH ENCRYPTED PASSWORD 'kiosk';
        GRANT ALL PRIVILEGES ON DATABASE kioskdb to kiosk;
        
        # Connect to our new local db
        \c self-check-in-kiosk-db
