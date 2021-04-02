from django.shortcuts import render
from .models import Character

# Create your views here.
from django.http import HttpResponse

def home(request):
  return render(request, 'about.html')

def about(request):
  return render(request, 'about.html')

def characters_index(request):
  characters = Character.objects.all()
  return render(request, 'characters/index.html', { 'characters': characters })

def characters_detail(request, characters_name):
  character = Character.objects.get(name=characters_name)
  return render(request, 'characters/detail.html', {'character' : character})