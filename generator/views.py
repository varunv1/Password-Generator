from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from string import ascii_lowercase, ascii_uppercase
import random as rd
# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'pass': 'afsvashdsefg'})

def password(request):
    characters = list(ascii_lowercase)
    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        characters.extend(ascii_uppercase)

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    thepass = ''
    for i in range(length):
        thepass += rd.choice(characters)
    return render(request, 'generator/password.html', {'password': thepass})


def about(request):
    return render(request, 'generator/about.html')