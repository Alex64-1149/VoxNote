from django.shortcuts import render, redirect
from .forms import MessageVocalForm
from django.http import JsonResponse
from pydub import AudioSegment
import io

import random
import string

def generate_random_string():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(4))

def accueil(request):
    recognized_text=None
    if request.method == 'POST' and request.FILES.get('audio_file'):
        audio_file = request.FILES['audio_file']
        print(audio_file)
        # Process the audio file
        #recognized_text = recognize_speech(audio_file)
        print('hello')
        recognized_text=generate_random_string()
        print(recognized_text)
    return render(request,"voxnote/accueil.html",{'recognized_text': recognized_text})


def mesNotes(request):
    return render(request,"voxnote/notes.html")