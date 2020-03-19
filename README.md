# django-rest-framework-vue-js

### Useful link 
https://jsonformatter.org/
https://www.django-rest-framework.org/
https://www.django-rest-framework.org/topics/browsable-api/
https://www.django-rest-framework.org/api-guide/validators/


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


### DRF DjangoRestFramework

```bash
pip install django

pip install djangorestframework

```

creiamo project

```bash
django-admin startproject newsapi

cd newsapi

```
creaimo APP

```bash

python manage.py startapp news

```

Installare la nostra APP e DRS in `settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',   
    'news'
]
```

Poi creiamo i MODEL ... e subito dopo ...

```bash
(venv3) (base) Pasquales-MacBook-Pro:newsapi pasqualespica$ python manage.py makemigrations
Migrations for 'news':
  news/migrations/0001_initial.py
    - Create model Article
(venv3) (base) Pasquales-MacBook-Pro:newsapi pasqualespica$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, news, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying news.0001_initial... OK
  Applying sessions.0001_initial... OK
```
poi creiamo superuser 

```bash
(venv3) (base) Pasquales-MacBook-Pro:newsapi pasqualespica$ python manage.py createsuperuser
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

poi registrare modelli in `admin.py`

### Serializers test ...

```bash
(venv3) (base) Pasquales-MacBook-Pro:newsapi pasqualespica$ python manage.py shell
Python 3.8.1 (default, Feb 13 2020, 17:25:51) 
[Clang 11.0.0 (clang-1100.0.33.17)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)

```

Serialize ...

```python
>>> from news.models import Article
>>> from news.api.serializers import ArticleSerializer
>>> article_int = Article.objects.first()
>>> article_int
<Article: Mario Rossi i 20 anni mieei>
>>> ser_var = ArticleSerializer(article_int)
>>> ser_var
ArticleSerializer(<Article: Mario Rossi i 20 anni mieei>):
    id = IntegerField(read_only=True)
    author = CharField()
    title = CharField()
    description = CharField()
    body = CharField()
    location = CharField()
    publication_date = DateField()
    active = BooleanField()
    created_at = DateTimeField(read_only=True)
    updated_at = DateTimeField(read_only=True)
>>> ser_var.data
{'id': 1, 'author': 'Mario Rossi', 'title': 'i 20 anni mieei', 'description': 'Description 1', 'body': 'conetnuto', 'location': 'Italia', 'publication_date': '2020-02-25', 'active': True, 'created_at': '2020-02-25T14:44:43.234785Z'}
>>> from rest_framework.renderers import JSONRenderer
>>> json = JSONRenderer().render(ser_var.data)
>>> json
b'{"id":1,"author":"Mario Rossi","title":"i 20 anni mieei","description":"Description 1","body":"conetnuto","location":"Italia","publication_date":"2020-02-25","active":true,"created_at":"2020-02-25T14:44:43.234785Z"}

```

Deserialize ...

```python
>>> import io
>>> from rest_framework.parsers import JSONParser
>>> stream = io.BytesIO(json)
>>> data = JSONParser().parse(stream)
>>> 
>>> serializer = ArticleSerializer(data=data)
>>> serializer.save()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/pasqualespica/my_data/PAS7B/my_workspaces/django-rest-framework-vue-js/03_DRF_LV_1/venv3/lib/python3.8/site-packages/rest_framework/serializers.py", line 177, in save
    assert hasattr(self, '_errors'), (
AssertionError: You must call `.is_valid()` before calling `.save()`.
>>> serializer.is_valid()
True
>>> serializer.save()
{'author': 'Mario Rossi', 'title': 'i 20 anni mieei', 'description': 'Description 1', 'body': 'conetnuto', 'location': 'Italia', 'publication_date': datetime.date(2020, 2, 25), 'active': True}
<Article: Mario Rossi i 20 anni mieei>
>>>
>>> Article.objects.all()
<QuerySet [<Article: Mario Rossi i 20 anni mieei>, <Article: Mario Rossi i 20 anni mieei>]>
>>> 
```

### Inspect ModelSerializer 

```python
(venv3) (base) Pasquales-MacBook-Pro:newsapi pasqualespica$ python manage.py shell
Python 3.8.1 (default, Feb 13 2020, 17:25:51) 
[Clang 11.0.0 (clang-1100.0.33.17)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from news.api.serializers import ArticleSerializer
>>> serializr = ArticleSerializer()
>>> print(repr(serializr))
ArticleSerializer():
    time_since_publication = SerializerMethodField()
    author = CharField(max_length=50)
    title = CharField(max_length=120)
    description = CharField(max_length=200)
    body = CharField(style={'base_template': 'textarea.html'})
    location = CharField(max_length=120)
    publication_date = DateField()
    active = BooleanField(required=False)
    created_at = DateTimeField(read_only=True)
```

### Dajngo rest-framework LV2

*CRUD Create, Read, Update, Delete*

- **GET**             : recuperare una risorsa
- **POST**            : creare una nuova risorsa
- **PUT / PATCH**     : aggiornare una risorsa
- **DELETE**          : cancellare una risorsa


Detailed descriptions, with full methods and attributes, 
for each of Django REST Framework's class-based views and serializers.
http://www.cdrf.co/


## Setting permission policy
https://www.django-rest-framework.org/api-guide/permissions/#setting-the-permission-policy

## Pagination
https://www.django-rest-framework.org/api-guide/pagination/

## Authentication
https://www.django-rest-framework.org/api-guide/authentication/#how-authentication-is-determined

```bash
pip install django-rest-auth

```

## Rest  Auth v.2 

```bash
pip install django-allauth
```

## ViewSets e Routers

https://www.django-rest-framework.org/api-guide/viewsets/ 
https://www.django-rest-framework.org/api-guide/routers/


# Vue.js
https://vuejs.org/

con Vue.js le nostre APP sono reattive ( vedi `console` da `inspect` del web browser)

## Eventi e Metodi

https://vuejs.org/v2/api/#v-on

## Rendering Condizionale

https://vuejs.org/v2/api/#v-for

## Class & Style Binding

https://vuejs.org/v2/guide/class-and-style.html

## Vue.JS - List Rendering con v-for

https://vuejs.org/v2/api/#v-for
