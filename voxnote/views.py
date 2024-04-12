from django.shortcuts import render, redirect
from .forms import NoteForm
from django.http import JsonResponse
from pydub import AudioSegment
from django.conf import settings
import os


import random
import string

def generate_random_string():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(4))


def accueil(request):
    recognized_text="Texte généré par l'IA"
    if request.method == 'POST' and request.FILES.get('audio_file'):
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
        #recognized_text = recognize_speech(audio_file)
        recognized_text=generate_random_string()
        print("Nouveau texte généré:", recognized_text)
        return render(request,"voxnote/accueil.html",{'recognized_text': recognized_text})
    return render(request,"voxnote/accueil.html",{'recognized_text': recognized_text})
   


def mesNotes(request):
    return render(request,"voxnote/notes.html")