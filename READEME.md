# PANAORBIT

## Prerequisites
Make sure you have installed python 3.10


## setup virtualenv

sh
pip install virtualenv
virtualenv .venv
source .venv/bin/activate


## install requirements

bash
pip install -r requirements.txt


## Need to expose values for the following environment variables.
commandline
SERVER_BASE_URL
DB_NAME
DB_USER
DB_PASSWORD
DB_HOST
DB_PORT
TWILIO_AUTH_TOKEN
TWILIO_PHONE_NUMBER
ACCOUNT_SID
OTP_LENGTH
OTP_EXPIRE_IN_MINUTES

## running django management commands & usage
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## swagger
you can access swagger in `/api/docs` end point once you started the server