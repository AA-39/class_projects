from django.shortcuts import render

def index(request):
    return render(request, 'pokeTracker/index.html')

def login(request):
    return render(request, 'pokeTracker/login.html')

def pokedex(request):
    return render(request, 'pokeTracker/pokedex.html')

def shinydex(request):
    return render(request, 'pokeTracker/shinydex.html')