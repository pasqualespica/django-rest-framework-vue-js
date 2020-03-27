from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser

class CustomUserAdmin(UserAdmin):
    # se dovessimo aggiugnere dei campi in piu' al  nostro custom User
    # potremmo aggiungere una nuova classe form da noi definita
    # add_form = ... per la creazione 
    # form  ... per la modifica

    model = CustomUser
    list_display = ["username", "email", "is_staff"]

admin.site.register(CustomUser, CustomUserAdmin)
