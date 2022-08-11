# Source: https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application#h-dockerizing-the-application
#Create a new file called nginx.default. This will be our configuration for nginx. We’ll listen on port 8020,
#serve the static files from the /opt/app/martor_demo/static directory and forward the rest of connections
#to port 8010, where Gunicorn will be listening

# ------------------------------------

# Source: https://blog.logrocket.com/dockerizing-django-app/
#   Take, for example, a web application with the following components:
#   Web server container such as Nginx
#   Application container that hosts the Django app
#   Database container that hosts the production database, such as PostgreSQL
#   A message container that hosts the message broker, such as RabbitMQ


# Base image
## This installs a Python image into the Docker image.
## This is also the version of Python that will run the application in the container
FROM python:3.9

# Setup environment variable
## Here we declare the working directory and assign it to the variable name DockerHOME.
## This will be the root directory of the Django app in the container
ENV DockerHOME=/home/jerneja/GitHubProjects/self-check-in-kiosk

# Set work directory
## This creates the directory with the specified path assigned to
## the DockerHOME variable within the image
RUN mkdir -p $DockerHOME

# Where your code lives
## This explicitly tells Docker to set the provided directory as
## the location where the application will reside within the container
WORKDIR $DockerHOME

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
## This updates the pip version that will be used to install
## the dependencies for the application
#RUN pip install --upgrade pip

# Copy whole project to your docker home directory.
COPY . $DockerHOME
# run this command to install all dependencies
#RUN pip install -r requirements.txt
RUN pip install pipenv
RUN pipenv install
# port where the Django app runs
EXPOSE 8000
# start server
CMD python manage.py runserver