FROM python:3.10.12
RUN apt-get update
# set the working directory
WORKDIR /app
# copy the repository files to it
COPY . /app
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
CMD uwsgi --http=0.0.0.0:80 --module=server.wsgi