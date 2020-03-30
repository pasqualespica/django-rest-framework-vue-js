
## Init env

```bash 
python -m venv venv_prj
. venv_prj/bin/activate
pip install django djangorestf
```

## Init project

```bash
django-admin startproject QuestionTime

(venv_prj) (base) Pasquales-MacBook-Pro:QuestionTime_App_prj pasqualespica$ cd QuestionTime/
(venv_prj) (base) Pasquales-MacBook-Pro:QuestionTime pasqualespica$ 
(venv_prj) (base) Pasquales-MacBook-Pro:QuestionTime pasqualespica$ ls -lrt
total 8
-rwxr-xr-x  1 pasqualespica  staff  632 Mar 26 15:14 manage.py
drwxr-xr-x  7 pasqualespica  staff  224 Mar 26 15:14 QuestionTime

```

## Due applicazioni django

### 1 - Users app
```bash
python manage.py startapp users
```

Anche se non estenderemo la class di default di  Django `AbstractUser`
creiamo comqunque un modello `CustomUser` e lo registraimo in `settings.py`
di progetto tramite la direttiva `AUTH_USER_MODEL` e poi applichiamo
la migrazione

```bash
(venv_prj) (base) Pasquales-MacBook-Pro:QuestionTime pasqualespica$ python manage.py makemigrations
Migrations for 'users':
  users/migrations/0001_initial.py
    - Create model CustomUser
```
e poi 

```bash
(venv_prj) (base) Pasquales-MacBook-Pro:QuestionTime pasqualespica$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, authtoken, contenttypes, sessions, users
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
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
  Applying users.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying authtoken.0001_initial... OK
  Applying authtoken.0002_auto_20160226_1747... OK
  Applying sessions.0001_initial... OK
```

e poi andiamo in `admin.py` per `Register your models` e infine

```bash
(venv_prj) (base) Pasquales-MacBook-Pro:QuestionTime pasqualespica$ python manage.py createsuperuser
Username: admin

```
Utilizzeremo DjagoRestAuth per la registrazione di nuovi utenti tramite endpoint
rest, mentre utilizzeremo DjangoRegistration per la registrazione di nuovi
utenti tramite la nostra interfaccia web

```bash
pip install django-rest-auth
pip install django-allauth
pip install django-registration
pip install django-crispy-forms
```

poi andiamo in `settings.py` per configurarli ... e dopo il comando `migrate`

dopo nel file `urls.py` per definire i path dei nostri package

...

Dobbiamo ora allestire una views ( un path url ) che corrispondera' con la nostra
homepage della nosta SinglePageApplication ( see `LOGIN_REDIRECT_URL = "/"`)

```python
# https://docs.python.org/3/library/re.html
re_path(r"^.*$",
    IndexTemplateView.as_view(),
    name="entry-point")
```

Poi sotto `user` creiamo la folder `api` con i nostri **serializers** e rispettive **views** e rispettivo `api/urls.py` con settaggio permesso
globale in `settings.py` se si e' autenticati.



### 2 - Questions app


