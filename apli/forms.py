from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,DireccionEnvio

#opciones del formulario

#formularios de la pagina
class FormUser(UserCreationForm):

    class Meta:
        model=User
        fields=['username','email','password1','password2']


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = DireccionEnvio
        fields = ['direccion', 'ciudad', 'provincia', 'codigo_postal']
        widgets = {
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}),
            'provincia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Provincia'}),
            'codigo_postal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código Postal'}),
        }