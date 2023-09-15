FROM python:3.10.12
RUN apt-get update
# set the working directory
WORKDIR /app
# copy the repository files to it
COPY . /app
RUN pip install -r requirements.txt

RUN python manage.py migrate
RUN python manage.py loaddata product.json

EXPOSE 80
CMD gunicorn --bind=0.0.0.0:80 --forwarded-allow-ips="*" server.wsgi
