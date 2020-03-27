from django_registration.forms import RegistrationForm
from users.models import CustomUser

# Tutto queto perche' la REGISTRATION di DRF si aspetta di lavorare
# con il modello di default USER e non quello fatto custom da noi

# https://django-registration.readthedocs.io/en/2.0.4/forms.html

class CustomUserForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = CustomUser
