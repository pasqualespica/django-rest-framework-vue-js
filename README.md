# django-rest-framework-vue-js

## JAVASCRIPT per Sviluppatori Python - CORSO RAPIDO COMPLETO
 https://www.youtube.com/watch?v=VHlBwk_ZQRs&feature=youtu.be

### 04_REQUESTS


### FIRST_API_DJANGO

```bash
pip install django

pip install pillow
```

```bash
django-admin startproject onlinestore

cd onlinestore

python manage.py migrate

```

create superuser

```bash 
python manage.py createsuperuser
Username (leave blank to use 'pasqualespica'): admin
Email address: 
Password: 
Password (again): 
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

create app 
(avremmo potuto aspettare di creare i modelli di `products` prima da dare il comando `migrate` ma va bene anche cosi)
```
python manage.py startapp products
```

andiamo ora a installare la nosta app in `onlinestore\settings.py`

```

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'products'
]
```

adesso siamo pronti di creare i nostri modelli nel file `models.py` della nostra
app `products` e poi lanciare i comandi :

```bash
(venv2) (base) Pasquales-MacBook-Pro:onlinestore pasqualespica$ python manage.py makemigrations
Migrations for 'products':
  products/migrations/0001_initial.py
    - Create model Manufacturer
    - Create model Product

```

```bash
(venv2) (base) Pasquales-MacBook-Pro:onlinestore pasqualespica$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, products, sessions
Running migrations:
  Applying products.0001_initial... OK
```

adesso siamo pronti a creare le nostre `views` all'interno del file `views.py`