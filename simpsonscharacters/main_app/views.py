from django.shortcuts import render, redirect
from .models import Character
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 

# Create your views here.
from django.http import HttpResponse

def home(request):
  return render(request, 'about.html')

@login_required
def about(request):
  return render(request, 'about.html')

@login_required
def characters_index(request):
  characters = Character.objects.filter(user=request.user)
  return render(request, 'characters/index.html', { 'characters': characters })

@login_required
def characters_detail(request, characters_name):
  character = Character.objects.get(name=characters_name)
  return render(request, 'characters/detail.html', {'character' : character})


class CharacterCreate(LoginRequiredMixin, CreateView):
  model = Character
  fields = '__all__'
  template_name = 'characters/create.html'

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)


class CharacterUpdate(LoginRequiredMixin, UpdateView):
  model = Character
  fields = ['occupation', 'description', 'age']
  template_name = 'characters/create.html'


class CharacterDelete(LoginRequiredMixin, DeleteView):
  model = Character
  template_name = 'characters/confirm_delete.html'
  success_url = '/characters'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)