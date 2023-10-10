from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from writenotes import models as note_models

class RegistrationForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ['username', 'email', 'password1', 'password2']

class NoteCollectionCreationForm(forms.ModelForm):
    class Meta:
        model = note_models.NoteCollection
        fields = ['title', 'description']