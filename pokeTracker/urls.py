## class_projects/pokeTracker/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('pokedex/', views.pokedex, name='pokedex'),
    path('shinydex/', views.shinydex, name='shinydex'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout')
]