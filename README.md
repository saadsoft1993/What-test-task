# Video Management System

This Django REST framework application is designed to manage a collection of videos, allowing users to perform various 
actions like listing, sorting, rating, and more. The application also provides user authentication and session management.

## Built With

Video Management System is built using Django, a high-level Python web framework, and Django REST Framework, an extension to Django for
building robust and flexible RESTful APIs. It utilizes a PostgreSQL database, which provides a powerful and scalable
data storage solution for the project.


* [![Python][python-shield]][python-url]
* [![Django][django-shield]][django-url]
* [![DjangoREST][rest-shield]][rest-url]
* [![Postgres][postgres-shield]][postgres-url]


## Getting started

1. #### First clone the gitlab repo with ssh.

   ```shell
       git clone https://github.com/saadsoft1993/What-test-task.git
   ```
2. #### Create a virtual environment.

   ```shell
       python -m venv venv
   ```

3. #### Activating virtual environment
    >  For **VS-Code**
    ```shell
        venv/bin/activate
    ```
   > For **Pycharm** select the interpreter from project setting.

4. #### Installing requirements
    > **_NOTE:_**  Many folks get difficulties while installing psycopg, so run this below command to fix the issue.
   ```shell
       sudo apt-get install libpq-dev
   ```
   Finally Install the requirements virtually.

   ```shell
       pip install -r requirements.txt
   ```

5. #### Set Environment variables
    > **_NOTE:_** There are some variable you need to define in .env file.
   ```shell
       cp .env.example .env
   ```
   Update your environment variables.


6. #### Do the migrations
   ```shell
       python manage.py migrate
   ```

### Now you are good to go to run the local server
   
   ```shell
       python manage.py runserver
   ```

> **_NOTE:_**  Don't forget to create a superuser mates.
   ```shell
       python manage.py createsuperuser
   ```
   Access the Django admin panel at http://localhost:8000/admin/ to manage videos, users, and other data.
   To use the API, authenticate by visiting http://localhost:8000/api/v1/authenticate/ and log in with your credentials.
   After logging in, you can access video-related endpoints and perform actions like listing, sorting, rating, and more.


## API Documentation

   The API is documented using Swagger, which provides an interactive interface for exploring and testing the endpoints. You can access the API documentation as follows:

### Swagger UI

   Swagger UI allows you to interactively explore and test the API endpoints. To access Swagger UI, follow these steps:

   1. Ensure the Django application is running.

   2. Open a web browser and go to the following URL: http://localhost:8000/
   


***

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[python-shield]: https://img.shields.io/badge/-Python-F9DC3E.svg?logo=python&style=flat
[python-url]: https://www.python.org/
[django-shield]: https://img.shields.io/badge/-Django-092E20.svg?logo=django&style=flat
[django-url]: https://www.djangoproject.com/
[rest-shield]: https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray
[rest-url]:https://www.django-rest-framework.org/
[postgres-shield]: https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white
[postgres-url]: https://www.postgresql.org/