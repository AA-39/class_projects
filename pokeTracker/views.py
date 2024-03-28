## class_projects/pokeTracker/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import Pokemon, PokedexCheckedCheckbox, ShinydexCheckedCheckbox
from .forms import RegistrationForm

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm(request)

    return render(request, 'authentication/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()

    return render(request, 'authentication/register.html', {'form': form})

@login_required(login_url='login')
def pokedex(request):
    regions = ['Kanto', 'Johto', 'Hoenn', 'Sinnoh', 'Unova', 'Kalos', 'Alola', 'Go', 'Galar', 'Hisui', 'Paldea']
    region_data = []

    for region in regions:
        pokemon_in_region = Pokemon.objects.filter(region=region)
        region_info = {
            'name': region,
            'pokemon_list': [{'natid': pokemon.natid, 'species': pokemon.species, 'link': pokemon.link} for pokemon in pokemon_in_region]
        }
        region_data.append(region_info)

    if request.method == 'POST':
        checked_checkboxes = request.POST.getlist('checkboxes')
        checked_checkboxes_instance, created = PokedexCheckedCheckbox.objects.get_or_create(user=request.user)
        checked_checkboxes_instance.checked_checkboxes_list = checked_checkboxes
        checked_checkboxes_instance.save()

    checked_checkboxes_instance, _ = PokedexCheckedCheckbox.objects.get_or_create(user=request.user)
    user_checked_checkboxes = [int(id) for id in checked_checkboxes_instance.get_checked_checkboxes()]


    print("TEST ONE")
    print(user_checked_checkboxes)

    return render(request, 'pokedex.html', {'regions': region_data, 'user_checked_checkboxes': user_checked_checkboxes})

@login_required(login_url='login')
def shinydex(request):
    regions = ['Kanto', 'Johto', 'Hoenn', 'Sinnoh', 'Unova', 'Kalos', 'Alola', 'Go', 'Galar', 'Hisui', 'Paldea']
    region_data = []

    for region in regions:
        pokemon_in_region = Pokemon.objects.filter(region=region)
        region_info = {
            'name': region,
            'pokemon_list': [{'natid': pokemon.natid, 'species': pokemon.species, 'link': pokemon.link} for pokemon in pokemon_in_region]
        }
        region_data.append(region_info)

    if request.method == 'POST':
        checked_checkboxes = request.POST.getlist('checkboxes')
        checked_checkboxes_instance, created = ShinydexCheckedCheckbox.objects.get_or_create(user=request.user)
        checked_checkboxes_instance.checked_checkboxes_list = checked_checkboxes
        checked_checkboxes_instance.save()

    checked_checkboxes_instance, _ = ShinydexCheckedCheckbox.objects.get_or_create(user=request.user)
    user_checked_checkboxes = [int(id) for id in checked_checkboxes_instance.get_checked_checkboxes()]

    print("TEST ONE")
    print(user_checked_checkboxes)

    return render(request, 'shinydex.html', {'regions': region_data, 'user_checked_checkboxes': user_checked_checkboxes})

