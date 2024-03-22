from django.shortcuts import render
from django.http import HttpResponse

def accueil(request):
    return render(request,"voxnote/accueil.html")

def mesNotes(request):
    return render(request,"voxnote/notes.html")