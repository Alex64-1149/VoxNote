from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='voxnote-accueil'),
    path ('notes/', views.mesNotes, name='voxnote-notes'),
]