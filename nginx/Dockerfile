# Source: https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d