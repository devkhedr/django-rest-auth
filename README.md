# Django Rest Authentication
API endpoints for users authentication (register, login, logout) built using Django REST framework, Knox Tokens.

## Installation and setup

#### Clone the project


```Bash
git clone https://github.com/devkhedr/django-rest-auth.git
```
#### Run the API server
   - create your virtual environment, and activate it.
   
   - install all the required dependencies
        ```Bash
        pip install -r requirements.txt
        ```
    - apply the django migrations
        ```Bash
        python manage.py makemigrations
        python manage.py migrate
        ```
    - start the API server.
        ```Bash
        python manage.py runserver
        ```
        now the server should be running on http://localhost:8000/