from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

#opciones del formulario

#formularios de la pagina
class FormUser(UserCreationForm):

    class Meta:
        model=User
        fields=['username','email','password1','password2']
