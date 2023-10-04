from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

class RegistrationForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ['username', 'email', 'password1', 'password2']