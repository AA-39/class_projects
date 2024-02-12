from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('pokedex/', views.pokedex, name='pokedex'),
    path('shinydex/', views.shinydex, name='shinydex')
]