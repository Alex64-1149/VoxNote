from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    description=models.TextField()
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
