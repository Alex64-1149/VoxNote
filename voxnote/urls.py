from django.urls import path
from . import views
from .views import NoteDeleteView,NoteDetailView

urlpatterns = [
    path('', views.accueil, name='voxnote-accueil'),
    path ('notes/', views.mesNotes, name='voxnote-notes'),
    path('about/', views.about, name='voxnote-about'),
    path('notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='voxnote-delete'),
    path('notes/<int:pk>/', NoteDetailView.as_view(),name="voxnote-detail"),

]