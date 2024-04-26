# forms.py
from django import forms
from .models import Note

class AudioForm(forms.Form):
    audio_file = forms.FileField()