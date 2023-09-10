from django.contrib import admin
from django.urls import path
from .views import home, search_result
urlpatterns = [
     path('', home, name='home'),
     path('search-result', search_result, name='search-result'),
]
