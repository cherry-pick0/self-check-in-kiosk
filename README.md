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
        
- Docker: version 20.10.17, build 100c701; [source](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)


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

- Docker Compose CLI plugin, version v2.6.0; [source](https://docs.docker.com/compose/install/compose-plugin/#installing-compose-on-linux-systems)


    sudo apt-get update
    sudo apt-get install docker-compose-plugin
    
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
        
### Naming
 TODO
