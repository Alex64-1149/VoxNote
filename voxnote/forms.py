# forms.py
from django import forms
from .models import MessageVocal

class MessageVocalForm(forms.ModelForm):
    class Meta:
        model = MessageVocal
        fields = ['fichier_audio']