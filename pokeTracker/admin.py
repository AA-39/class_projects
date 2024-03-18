## class_projects/pokeTracker/admin.py
from django.contrib import admin
from .models import Pokemon, PokedexCheckedCheckbox, ShinydexCheckedCheckbox

admin.site.register(Pokemon)
admin.site.register(PokedexCheckedCheckbox)
admin.site.register(ShinydexCheckedCheckbox)