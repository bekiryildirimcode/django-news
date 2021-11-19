from django.contrib import admin
from django.urls import path
from news.views import show_genres
 
urlpatterns = [
    path('', show_genres),
]
