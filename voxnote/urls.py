from django.urls import path
from . import views

urlpatterns = [
    path('voxnote/', views.accueil, name='voxnote'),
]