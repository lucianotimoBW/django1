# README de mi proyecto



git init
git add .
git commit -m 'comentario...'
git push
git status

pip freeze

python -m venv venv
. venv/Scripts/activate
deactivate

pip install django
pip freeze > requirements.txt
django-admin startproject proyecto .

python manage.py migrate

python manage.py runserver



En otra consola:
$ python manage.py startapp inicio
crea la carpeta 'inicio' con varios archivos .py