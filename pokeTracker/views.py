## class_projects/pokeTracker/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'pokeTracker/index.html')

def login(request):
    return render(request, 'pokeTracker/login.html')

def pokedex(request):
    kanto = range(1, 151)  # Replace this with your actual image numbers
    johto = range(152, 251)
    hoenn = range(252, 386)
    sinnoh = range(387, 493)
    unova = range(494, 649)
    kalos = range(650, 721)
    alola = range(722, 807)
    go = range(808, 809)
    galar = range(810, 905)
    paldea = range(906, 1025)
    aforms = [20019, 20020, 20026, 20027, 20028, 20037, 20038, 20050,
              20051, 20052, 20053, 20074, 20075, 20076, 20088, 20089,
              20103, 20105]
    gforms = [30052, 30077, 30078, 30079, 30080, 30083, 30110, 30122,
              30144, 30145, 30146, 30199, 30222, 30263, 30264, 30554,
              30555, 30562, 30618]
    hforms = [40058, 40059, 40100, 40101, 40157, 40211, 40215, 40503,
              40549, 40570, 40571, 40628, 40705, 40706, 40713]
    pforms = [50128, 50194]

    context = {'kanto': kanto, 'johto': johto, 'hoenn': hoenn, 
               'sinnoh': sinnoh, 'unova': unova, 'kalos': kalos,
               'alola': alola, 'go': go, 'galar': galar, 'paldea': paldea,
               'aforms': aforms, 'gforms': gforms, 'hforms': hforms,
               'pforms': pforms}
    return render(request, 'pokeTracker/pokedex.html', context)

def shinydex(request):
    kanto = range(1, 151)  # Replace this with your actual image numbers
    johto = range(152, 251)
    hoenn = range(252, 386)
    sinnoh = range(387, 493)
    unova = range(494, 649)
    kalos = range(650, 721)
    alola = range(722, 807)
    go = range(808, 809)
    galar = range(810, 905)
    paldea = range(906, 1025)
    aforms = [20019, 20020, 20026, 20027, 20028, 20037, 20038, 20050,
              20051, 20052, 20053, 20074, 20075, 20076, 20088, 20089,
              20103, 20105]
    gforms = [30052, 30077, 30078, 30079, 30080, 30083, 30110, 30122,
              30144, 30145, 30146, 30199, 30222, 30263, 30264, 30554,
              30555, 30562, 30618]
    hforms = [40058, 40059, 40100, 40101, 40157, 40211, 40215, 40503,
              40549, 40570, 40571, 40628, 40705, 40706, 40713]
    pforms = [50128, 50194]

    context = {'kanto': kanto, 'johto': johto, 'hoenn': hoenn, 
               'sinnoh': sinnoh, 'unova': unova, 'kalos': kalos,
               'alola': alola, 'go': go, 'galar': galar, 'paldea': paldea,
               'aforms': aforms, 'gforms': gforms, 'hforms': hforms,
               'pforms': pforms}
    return render(request, 'pokeTracker/shinydex.html', context)