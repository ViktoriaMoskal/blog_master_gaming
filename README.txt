python -m pip install --upgrade pip
pip install django
django-admin startproject project1
cd project1
python manage.py startapp blog
python manage.py migrate
python manage.py runserver