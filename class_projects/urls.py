## class_projects/class_projects/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokeTracker/', include('pokeTracker.urls'))
]