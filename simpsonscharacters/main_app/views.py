from django.shortcuts import render
from .models import Character
from django.views.generic import CreateView

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

class CharacterCreate(CreateView):
  model = Character
  fields = '__all__'
  template_name = 'characters/create.html'
