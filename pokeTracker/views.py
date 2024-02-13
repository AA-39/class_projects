from django.shortcuts import render

def index(request):
    return render(request, 'pokeTracker/index.html')

def login(request):
    return render(request, 'pokeTracker/login.html')

def pokedex(request):
    return render(request, 'pokeTracker/pokedex.html')

def checkbox_form(request):
    image_numbers = range(1, 31)  # Assuming you have images named 1.jpg, 2.jpg, ..., 30.jpg
    return render(request, 'pokeTracker/pokedex.html', {'image_numbers': image_numbers})

def shinydex(request):
    return render(request, 'pokeTracker/shinydex.html')