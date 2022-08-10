# self-check-in-kiosk
Self Check-In Kiosk

Track actions and status here:
https://trello.com/b/coUnjV9y/backend

Owner of the project: bozic.jerneja@gmail.com; cherry-pick0

---------------------------------------------------------

##Background

System packages and dependencies:

- python: Python 3.8.10
- PostgreSQL (database server): 12.11 (Ubuntu 12.11-0ubuntu0.20.04.1); you will need Psycopg (adapter for Python)
- pip (python package manager): 20.2.3 from /home/jerneja/.local/lib/python3.8/site-packages/pip (python 3.8)
- pipenv (tool; Pipfile, pip, and virtualenv in one single command): version 2020.8.13
- make: automation tool for running commands
- pre-commit

##Setup the project (follow steps)

        pipenv shell
        pipenv install

## Steps of creating this project (notes)

1. Activate the environment (this command creates or activates virtual environment)

        pipenv shell

   This will create a new virtual environment with Pipfile

        (self-check-in-kiosk) jerneja@jerneja:~/GitHubProjects/self-check-in-kiosk$

2. Install django and other dependencies

    This will install dependencies in our virtual environment.


        pipenv install django
        pipenv install djangorestframework
        pipenv install django-cors-headers
        # Development dependencies
        pipenv install black --dev
        pipenv install pre-commit --dev
        pipenv install flake8 --dev
        

Notes on dev dependencies

* [Black: Python code formatter](https://github.com/psf/black) & [Setup black for PyCharm](https://godatadriven.com/blog/partial-python-code-formatting-with-black-pycharm/)
* [pre-commit](https://pre-commit.com/)
* [Flake8](https://flake8.pycqa.org/en/latest/)

-------------------------------------------

3. Create a django project

        django-admin startproject kiosk

   Note: check if django server is running

        cd kiosk
        python manage.py runserver

   or

        make runserver

4. Add configuration files:

    - pre-commit: .pre-commit-config.yaml and run "pre-commit install"
    - black: pyproject.toml
