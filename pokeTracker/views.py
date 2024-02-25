## class_projects/pokeTracker/views.py

from django.shortcuts import render
from .models import Pokemon

def index(request):
    return render(request, 'pokeTracker/index.html')

def login(request):
    return render(request, 'pokeTracker/login.html')

def pokedex(request):
    regions = ['Kanto', 'Johto', 'Hoenn', 'Sinnoh', 'Unova', 'Kalos', 'Alola', 'Galar', 'Paldea']
    region_data = []

    for region in regions:
        pokemon_in_region = Pokemon.objects.filter(region=region)
        region_info = {
            'name': region,
            'pokemon_list': [{'natid': pokemon.natid} for pokemon in pokemon_in_region]
        }
        region_data.append(region_info)

    return render(request, 'pokeTracker/pokedex.html', {'regions': region_data})

def shinydex(request):
    regions = ['Kanto', 'Johto', 'Hoenn', 'Sinnoh', 'Unova', 'Kalos', 'Alola', 'Galar', 'Paldea']
    region_data = []

    for region in regions:
        pokemon_in_region = Pokemon.objects.filter(region=region)
        region_info = {
            'name': region,
            'pokemon_list': [{'natid': pokemon.natid} for pokemon in pokemon_in_region]
        }
        region_data.append(region_info)

    return render(request, 'pokeTracker/shinydex.html', {'regions': region_data})