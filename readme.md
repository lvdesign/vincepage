# base



### run
source ./venv/bin/activate
cd /Users/laurentvignaux/venv/vincepage

python manage.py runserver


python manage.py migrate

python manage.py makemigrations mesvins
python manage.py migrate mesvins

python manage.py createsuperuser
admin: toto
psw: totototo

python manage.py collectstatic

## dependances
pip freeze > requirements.txt

nano ~/.bash_profile


## Git
- $ git status
- $ git add -A
- $ git commit -m "initial commit"

## Models 

class Vin
- name
- author
- image
- description
- category
- tags

-commentaire
-favoris

class User

class Category (region) -> ManyToOne
- name
- description

class Tag (cepage) -> ManyToMany
name
description

class Commentaire -> OneToMany

heroku
contact@lvdesign.com.fr