## class_projects/pokeTracker/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'pokeTracker/index.html')

def login(request):
    return render(request, 'pokeTracker/login.html')

def pokedex(request):
    image_numbers = range(1, 1000)  # Replace this with your actual image numbers
    context = {'image_numbers': image_numbers}
    return render(request, 'pokeTracker/pokedex.html', context)

def shinydex(request):
    image_numbers = range(1, 1000)  # Replace this with your actual image numbers
    context = {'image_numbers': image_numbers}
    return render(request, 'pokeTracker/shinydex.html', context)