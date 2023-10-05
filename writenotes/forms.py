from django import forms
from . import models

class NoteCollectionCreationForm(forms.ModelForm):
    class Meta:
        model = models.NoteCollection
        fields = ['title', 'description']

class NoteCreationForm(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = ['title', 'content']
