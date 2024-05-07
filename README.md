# vendor_management
vendor management system

## Instructions

1. Set Up the Database.
2. no need to create .env file, just go to vendor_management > vendor_management > settings.py and update DATABASE credentials.

3. run migrate.
4. create a superuser by python manage.py createsuperuser
5. restore postman collection from https://orange-sunset-792074.postman.co/workspace/task~8c725600-f9e6-42b0-a080-6a11a5696529/collection/23515172-a44eebb1-b2f7-455c-a5ac-cff2f88acca7?action=share&creator=23515172

## Development Instructions

1. *Clone* the Repository

git clone https://github.com/RominGujarati/vendor_management.git


2. Setup the *Environment*
   Once cloned, take a look at the Folder Structure.


python -m venv venv


3. Install the *Requirements*

pip install -r requirements.txt


5. Project *Setup*
   Run these following commands to setup the Project


python manage.py makemigrations
python maange.py migrate


6. *Start* Project

python manage.py runserver


==============
End of the Instructions