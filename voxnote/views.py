from django.shortcuts import render, redirect
from django.views.generic import DeleteView,DetailView
from django.conf import settings
from .models import Note, Message  # Import des modèles Note et Message depuis le fichier models.py
from .forms import AudioForm  # Import du formulaire AudioForm depuis le fichier forms.py
import os  # Import du module os pour les opérations liées au système d'exploitation
import random  # Import du module random pour la génération de texte aléatoire
import string  # Import du module string pour manipuler les chaînes de caractères
from django.urls import reverse_lazy


def generate_random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

class NoteDetailView(DetailView):
    model=Note

    template_name="voxnote/note_detailView.html"

class NoteDeleteView(DeleteView):
    model=Note   

    success_url=reverse_lazy('voxnote-notes')

    template_name = "voxnote/note_confirm_delete.html"

# Vue pour la page d'accueil de l'application
def accueil(request):
      # Initialisation du texte reconnu à "Allo"
    user_notes = []  # Initialisation de la liste des notes de l'utilisateur à une liste vide

    # Vérifie si l'utilisateur est connecté
    

    # Crée une instance du formulaire AudioForm
    audio_form = AudioForm()

    # Vérifie si la requête HTTP est de type POST
    if request.method == 'POST':
        # Crée une instance du formulaire AudioForm avec les données de la requête
        audio_form = AudioForm(request.POST, request.FILES)
        # Vérifie si le formulaire est valide
        if audio_form.is_valid():
            # Récupère le fichier audio depuis les données de la requête
            audio_file = request.FILES['audio_file']

            # Affiche un message dans la console indiquant que le formulaire a été soumis avec succès
            print("Formulaire soumis avec succès")

            # Crée le répertoire pour stocker les fichiers audio s'il n'existe pas
            media_directory = os.path.join(settings.MEDIA_ROOT, 'message_vocaux')
            os.makedirs(media_directory, exist_ok=True)

            # Détermine le chemin complet du fichier audio à sauvegarder
            file_path = os.path.join(settings.MEDIA_ROOT, 'message_vocaux', audio_file.name)
            # Sauvegarde le fichier audio sur le disque
            with open(file_path, 'wb') as destination:
                for chunk in audio_file.chunks():
                    destination.write(chunk)

            # Affiche dans la console le nom du fichier audio sauvegardé
            print(audio_file)

            # Traite le fichier audio pour reconnaître le texte (pour l'instant, génère simplement un texte aléatoire)
            recognized_text = generate_random_string()
            print("Nouveau texte généré:", recognized_text)

            # Enregistre le texte reconnu dans la  base de données en tant que Note
            if request.user.is_authenticated:
                note = Note.objects.create(user=request.user, message=recognized_text)
                print('texte reconnu1:',recognized_text)    
            
        return render(request, "voxnote/accueil.html", {'recognized_text': recognized_text, 'audio_form': audio_form})
                
    else:
         return render(request, "voxnote/accueil.html", { 'audio_form': audio_form})
        

   
    

# Vue pour afficher les notes de l'utilisateur
def mesNotes(request):
    user_notes = []  # Initialisation de la liste des notes de l'utilisateur à une liste vide
    # Vérifie si l'utilisateur est connecté
    if request.user.is_authenticated:
        # Récupère les notes de l'utilisateur depuis la base de données et les trie par date
        user_notes = Note.objects.filter(user=request.user).order_by('-date')
    # Rend la page de notes avec les données nécessaires pour l'affichage
    return render(request,"voxnote/notes.html",{'user_notes': user_notes})


def about(request):
    return render(request,"voxnote/about.html")
