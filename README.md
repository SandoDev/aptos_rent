# Aptos Rent

Api to manage information of apartments for rent

## Built with
* Python 3.6.9
* Django 3.2.3
* SQLite

## Install

1. Create virtualenv

    virtualenv -p python3 venv_rent

2. Install requirements

    pip install -r requirements.txt

3. Run migrations

    python manage.py migrate

4. Run server

    python manage.py runserver

## Usage flow from admin
1. Save new Apto
    * address
    * number of rooms
    * rent price
    * etc
1. Manage the Apto
    * change status
    * include remarks

## Author
* Camilo Sandoval - camilo.sandoval.ad@gmail.com