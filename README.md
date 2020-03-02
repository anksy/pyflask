# pyflask

pyflask is a python's microframework, named Flask, based project gives exposes web services written in it.

It uses SQLAlchemy and Marshmallow ORM to map relational queries. You can connect to Postgres, MySQL, Sqlite etc database with your application. All you have to do changes in environment variable.

# Install Virtualenv

**Virtualenv** isolates your project level dependencies. Run below command to your project root directory:

`python -m virtualenv venv`

**venv** is your virtualenv name.

## Installing Dependencies

Run below command to install project level dependencies saved in **requirements.txt**

`pip install -r requirements.txt`

## Running Flask App

Run your flask application by
 
`python run.py`

this command will run flask application. You can access this app by pointing your browser to [http://localhost:5000/api/v1/documentation](http://localhost:5000/api/v1/documentation). This will open a swagger documentation page for your APIs.

## Change Configurations

Look for `config.py` to change app level configurations.
