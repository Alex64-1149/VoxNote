from django.shortcuts import render, redirect
from django.conf import settings
from .models import Note
from .forms import AudioForm
import os
import random
import string

def generate_random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def accueil(request):
    recognized_text = "Texte généré par l'IA"
    user_notes = []

    if request.user.is_authenticated:
        user_notes = Note.objects.filter(user=request.user).order_by('-date')

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
            # Process the audio file
            # recognized_text = recognize_speech(audio_file)
            recognized_text = generate_random_string()
            print("Nouveau texte généré:", recognized_text)

            # Enregistrement de la note dans la base de données
            if request.user.is_authenticated:
                note = Note.objects.create(user=request.user, message=recognized_text)
            else:
                # Handle anonymous user (optional)
                return redirect('voxnote-login')

            # Redirection vers la page d'accueil
            return redirect('voxnote-accueil')

    return render(request, "voxnote/accueil.html", {'recognized_text': recognized_text, 'audio_form': audio_form, 'user_notes': user_notes})

def mesNotes(request):
    user_notes = []

    if request.user.is_authenticated:
        user_notes = Note.objects.filter(user=request.user).order_by('-date')
    return render(request,"voxnote/notes.html",{'user_notes': user_notes})