# self-check-in-kiosk
Self Check-In Kiosk

Track actions and status here:
https://trello.com/b/coUnjV9y/backend

Owner of the project: bozic.jerneja@gmail.com; cherry-pick0

---------------------------------------------------------

##Setup the project

System packages and dependencies:

- python: Python 3.8.10
- PostgreSQL (database server): 12.11 (Ubuntu 12.11-0ubuntu0.20.04.1); you will need Psycopg (adapter for Python)
- pip (python package manager): 20.2.3 from /home/jerneja/.local/lib/python3.8/site-packages/pip (python 3.8)
- pipenv (tool; Pipfile, pip, and virtualenv in one single command): version 2020.8.13


## Steps of creating this project

1) Activate the environment (this command creates or activates virtual environment)

        pipenv shell
        
   This will create a new virtual environment with Pipfile
   
        (self-check-in-kiosk) jerneja@jerneja:~/GitHubProjects/self-check-in-kiosk$
        
2) Install django and other dependencies

This will install dependencies in our virtual environment.

        pipenv install django
        pipenv install djangorestframework
        pipenv install django-cors-headers
        
3) Create django project

        django-admin startproject kiosk
        
        