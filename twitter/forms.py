from django.forms import ModelForm
from django.contrib.auth.models import User

class Register(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        help_texts = {
            'username': None,  # Set the help text for the username field to None
        }  