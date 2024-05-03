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
    user_message = Message.objects.filter().order_by('-date')
    if not user_message:
        recognized_text='Texte généré par Voxnote'
    else:
        recognized_text=user_message[0].message

    audio_form = AudioForm()

    if request.method == 'POST':
        audio_form = AudioForm(request.POST, request.FILES)
        if audio_form.is_valid():
            audio_file = request.FILES['audio_file']
            print("Formulaire soumis avec succès")

            media_directory = os.path.join(settings.MEDIA_ROOT, 'message_vocaux')
            os.makedirs(media_directory, exist_ok=True)

            file_path = os.path.join(settings.MEDIA_ROOT, 'message_vocaux', audio_file.name)
            with open(file_path, 'wb') as destination:
                for chunk in audio_file.chunks():
                    destination.write(chunk)

            print(audio_file)

            recognized_text = generate_random_string()
            Message.objects.create(message=recognized_text)
            print("Nouveau texte généré:", recognized_text)

            if request.user.is_authenticated:
                note = Note.objects.create(user=request.user, message=recognized_text)
            print('redirect notes')
            return redirect('voxnote-notes')  # Redirige vers la vue accueil après avoir traité la requête POST

    print('texte reconnu1:', recognized_text)
    return render(request, "voxnote/accueil.html", {'recognized_text': recognized_text, 'audio_form': audio_form})
   
    

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
