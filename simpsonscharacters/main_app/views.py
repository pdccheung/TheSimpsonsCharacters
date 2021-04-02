from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

class Character: 
    def __init__(self, name, age, sex, description, occupation):
        self.name = name
        self.age = age
        self.sex = sex
        self.description = description
        self.occupation = occupation

characters = [
    Character('Homer Simpson', '39', 'male', 'Homer Jay Simpson (born May 12) is the main Protagonist of The Simpsons series.', 'safety inspector'),
    Character('Marge Simpson', '36', 'female', 'Marjorie Jacqueline "Marge" Simpson is the homemker and a full-time crazy mom of the Simpsons family', 'homemaker'),
    Character('Bart Simpson', '10', 'male', 'Bartholomew JoJo "Bart" Simpson (born April 1) is the Deuteragonist of The Simpsons.', 'student' ),
    Character('List Simpson', '8', 'female', 'Lisa Marie Simpson (born May 9 1981) is the elder daughter and middle child of the Simpson family', 'student'),
    Character('Maggie Simpson', '1', 'female', 'Margaret Evelyn Lenny "Maggie" Simpson, is the 1-year-old, and youngest, child of Marge and Homer', 'baby' ),
]

def characters_index(request):
  return render(request, 'characters/index.html', { 'characters': characters })

