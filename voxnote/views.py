from django.shortcuts import render, redirect
from .forms import MessageVocalForm
from django.http import JsonResponse
from pydub import AudioSegment
import io

def accueil(request):
    return render(request,"voxnote/accueil.html")

def mesNotes(request):
    return render(request,"voxnote/notes.html")