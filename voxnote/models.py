from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class MessageVocal(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    fichier_audio = models.FileField(upload_to='messages_vocaux/')
    date_creation = models.DateTimeField(auto_now_add=True)
