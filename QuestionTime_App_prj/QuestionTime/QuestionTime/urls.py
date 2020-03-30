"""QuestionTime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path

# https://django-registration.readthedocs.io/en/2.0.4/
# https://django-registration.readthedocs.io/en/2.0.4/custom-user.html
# https://django-registration.readthedocs.io/en/2.0.4/simple-workflow.html

from django_registration.backends.one_step.views import RegistrationView

from users.forms import CustomUserForm

urlpatterns = [
    # URLS me la sezione amministrazione
    path('admin/', admin.site.urls),

    # LOGIN tramite interfaccia browser standard
    path("accounts/",
         include("django.contrib.auth.urls")),

    # Registration tramite interfaccia browser standard
    path("accounts/register/",
        RegistrationView.as_view(
            form_class=CustomUserForm,
            success_url="/",
        ), name="django_registration_register"), # name end-point path

    # includiamo anche gi altri urls messi a disposizioni da django_resgistration
    path("accounts/",
        include("django_registration.backends.one_step.urls")),

    # # LOGIN tramite interfaccia browser standard
    # path("accounts/",
    #     include("django.contrib.auth.urls")),

    # login tramite browsable-api
    path("api-auth/",
        include("rest_framework.urls")),

    # login tramite REST
    path("api/rest-auth/",
        include("rest_auth.urls")),

    # registration tramite REST
    path("api/rest-auth/registration/",
        include("rest_auth.registration.urls")),

]
