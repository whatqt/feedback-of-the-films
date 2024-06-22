from register.views import index_home
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('', index_home),
    path('register/', include('register.urls')),
    path('select_films/', include('review_films.urls')),    
]
