## Steps of creating this project (notes)

Note: these are only notes and not instructions, in order to make
this app structure more easily understandable.

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
* [awscli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html): AWS client


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

Note: docker-compose will create its own db-container,
but using postgresql on our machine will make it easier
for our development process.

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
        \c kioskdb

**6. Docker**

Note: for development process, dockerization isn't necessary.
But we are setting this up for staging and production servers.
    
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


<sub>6.4 Build docker containers </sub>

        # Note - you might need to run this before:
        sudo chmod 777 /var/run/docker.sock

        # You might need to stop postgres on your machine,
        # in order to run docker-compose, since db-container
        # will use the same port 5432
        sudo service postgresql stop
        
        # Build and run containers
        # Use -d to run containers in the background
        docker-compose -f docker-compose.dev.yml up -d --build
        
        # Run migrations in container
        docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
        

<sub>6.4.1 Build and push prod containers </sub>
        
        # todo: nginx container id
        docker-compose -f docker-compose.prod.yml up --build -d
        
        # Push containers to server
        docker-compose -f docker-compose.prod.yml push
        


<sub>6.5 Dockerization </sub>

One of the sources: https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/


**7. User auth**

- source: [docs](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/)

We will have a custom User model. Create users module/django app:
        
        cd apps
        python ../manage.py startapp users
etc.


**8. Pycharm settings**

- Open django project at (where manage.py is):

        self-check-in-kiosk/kiosk
   
- Enable and add django settings in Pycharm: [hint](https://drive.google.com/file/d/1tGmYeOPrWT4yqgyszEUNf6BTfbNrzJGT/view?usp=sharing)


**9. Add environment variables to your system**
        
- on Ubuntu, go to .bashrc file and add:
Note: is this still necessary?
         
         export DJANGO_SETTINGS_MODULE="kiosk.settings.dev"


**10. AWS account**

- Create AWS account
- Note: lambda??

    **10.1 Setup EC2 machine**
    
    Find 'launch ec2 instance section' and follow instructions. Here is my config:
    
    - Create t2.micro (free tier) ec2 instance, running Ubuntu.
    - You will need to create key-pair (rsa, .pem),
    with which you'll connect to the server. Check [this example](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html).
    
    After setup, you can connect via ssh:
    
        ssh ubuntu@instance-ip-address -i .ssh/kiosk-api-key.pem
        
        # Run these commands (following instructions on https://testdriven.io/blog/django-docker-https-aws/)
        $ sudo apt update
        $ sudo apt install apt-transport-https ca-certificates curl software-properties-common
        $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
        $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
        $ sudo apt update
        $ sudo apt install docker-ce
        $ sudo usermod -aG docker ${USER}
        $ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
        $ sudo chmod +x /usr/local/bin/docker-compose
        
        $ docker -v
        Docker version 20.10.8, build 3967b7d
        
        $ docker-compose -v
        docker-compose version 1.29.2, build 5becea4c
   
   -??? Next, Create IAM role "django-ec2" (following instructions on the link: https://testdriven.io/blog/django-docker-https-aws/) and attach the new role to your EC2 instance.
   -??? Setup AWS ECR (check  https://testdriven.io/blog/django-docker-https-aws/): fully-managed Docker image registry that makes it easy for developers to store and manage images
   - 
   
    **10.2 Setup RDS**
    
    Go to RDS section and find 'Create database' section.
    
    - PostgreSQL engine
    - Size: db.t3.micro
    - Template: Free tier
    - Database auth: Password and IAM database authentication
    - Make sure to save username and password!
    - Make it publicly accessible, so you can access it separately later
    - Edit security group inbound rules, to make postgresql accessible
    
    You can connect to the database:
    
        psql -h kioskdb.XYZ.us-east-1.rds.amazonaws.com -p 5432 -d kioskdb -U kiosk

    **10.3 Setup Deployment process**
    
    - Dockerization

    **10.4 Setup Email service**
    
    - We're using sandbox for now. 
    - Add verified identities (email addresses and domains)

    **10.5 Setup S3 bucket**
    
    **10.6 AWS CLI**
    
        - You need to have aws-cli installed
        - Go to aws dashboard to 'Security credentials' zone.
        - Set up keys in section "Access keys (access key ID and secret access key)"
        - Save the credentials!
        - Set credentials in aws (config region, aws_access_key_id, aws_secret_access_key)
        - run aws ecr get-login --no-include-email
        - or run aws --region us-east-1 ecr get-login-password | docker login --password-stdin --username AWS "AWS-ACCOUNT-ID.dkr.ecr.us-east-1.amazonaws.com"
   
    **10.7 Add image**
    
    Container images are stored in Amazon ECR repositories.
    Create new private ECR repository "django-ec2", so you
    can push images inside.
    
    https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html
    
    **10.8 Running the Containers**
    
    **11. Assign an Elastic IP address to an instance**
    
    https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html#Add_IGW_Attach_Gateway
    
    Note: some steps for aws configs are probably missed.
    
    **12. Deploy docker containers**
    
    Run on your machine: 
        
        aws --region us-east-1 ecr get-login-password | docker login --password-stdin --username AWS "108408647134.dkr.ecr.us-east-1.amazonaws.com"
        docker-compose -f docker-compose.prod.yml down
        docker-compose -f docker-compose.prod.yml build
        docker-compose -f docker-compose.prod.yml push
        # Note: do you really need to copy full directory?
        scp -i ~/.ssh/kiosk-api-key.pem -o IdentitiesOnly=yes -r $(pwd)/{kiosk,nginx,docker-compose.prod.yml} ubuntu@54.162.196.49:/home/ubuntu/test-kiosk-dir
    
    Run on server:
    
        aws --region us-east-1 ecr get-login-password | docker login --password-stdin --username AWS "108408647134.dkr.ecr.us-east-1.amazonaws.com"
        docker pull 108408647134.dkr.ecr.us-east-1.amazonaws.com/django-ec2:web
        docker pull 108408647134.dkr.ecr.us-east-1.amazonaws.com/django-ec2:nginx-proxy 
        docker-compose -f docker-compose.prod.yml up -d
        
        # Go to shell
        docker exec -it <container_id> python manage.py shell
