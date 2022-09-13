## Steps of creating this project (notes)

**1. Activate the environment (this command creates or activates virtual environment)**

        pipenv shell

   This will create a new virtual environment with Pipfile

        (self-check-in-kiosk) jerneja@jerneja:~/GitHubProjects/self-check-in-kiosk$

**2. Install django and other dependencies**

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


**3. Create a django project**

        django-admin startproject kiosk
        # Add 'kiosk' to INSTALLED_APPS in settings.py
        
   <sub>3.1 Check if django server is running</sub>
   
        cd kiosk
        python manage.py runserver
   or
   
        make runserver
        
   <sub>3.2 Create your models (only example)</sub>
   
        python manage.py startapp registrations
        python manage.py makemigrations
   
**4. Add configuration files:**

Pre-commit:
- .pre-commit-config.yaml
- Execute pre-commit install to install git hooks in your .git/ directory

Black:
- pyproject.toml
    
**5. Setup db**

        # Create local db
        sudo -u postgres createdb kioskdb
            
        # Enter postgres
        sudo -u postgres psql
        
        # Create new user and grant privileges
        CREATE USER kiosk WITH ENCRYPTED PASSWORD 'kiosk';
        GRANT ALL PRIVILEGES ON DATABASE kioskdb to kiosk;
        
        # For testing purposes - add permission to create db
        ALTER USER kiosk CREATEDB;
        
        # Connect to our new local db
        \c self-check-in-kiosk-db

**6. Docker**
    
<sub>6.1 Installing Docker([source](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)) </sub>

        # First, update your existing list of packages
        sudo apt update
        
        # Next, install a few prerequisite packages which let apt use packages over HTTPS:
        sudo apt install apt-transport-https ca-certificates curl software-properties-common
        
        # Then add the GPG key for the official Docker repository to your system:
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
        
        # Add the Docker repository to APT sources:
        sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
    
        # Make sure you are about to install from the Docker repo instead of the default Ubuntu repo
        apt-cache policy docker-ce
        
        # Finally, install Docker
        sudo apt install docker-ce
        
        # Check that it’s running
        sudo systemctl status docker
        

<sub>6.2 Installing Docker Compose</sub>
        
        # Install Docker Compose
        sudo apt-get install docker-compose-plugin

<sub>About docker and virtual env ([source](https://stackoverflow.com/questions/66407993/which-is-better-virtual-env-or-docker)) </sub>

> A virtualenv only encapsulates Python dependencies.
A Docker container encapsulates an entire OS. With a Python virtualenv,
you can easily switch between Python versions and dependencies,
but you're stuck with your host OS.
With a Docker image, you can swap out the entire OS - install and run Python
on Ubuntu, Debian, Alpine, even Windows Server Core.


<sub>6.3 Add Dockerfile to project</sub>


<sub>6.4 Build docker image </sub>
    
        docker build . -t docker-django-v0.0

Note: for some reason I need to run this before
    
        sudo chmod 777 /var/run/docker.sock
TODO finish dockerization


**7. User auth**

- source: [docs](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/)

We will have a custom User model. Create users module/django app:
        
        cd apps
        python ../manage.py startapp users


**8. Pycharm settings**

- Open django project at (where manage.py is):

        self-check-in-kiosk/kiosk
   
- Enable and add django settings in Pycharm: [hint](https://drive.google.com/file/d/1tGmYeOPrWT4yqgyszEUNf6BTfbNrzJGT/view?usp=sharing)


**9. Add environment variables to your system**
        
- on Ubuntu, go to .bashrc file and add:
         
         
         export DJANGO_SETTINGS_MODULE="kiosk.settings"
