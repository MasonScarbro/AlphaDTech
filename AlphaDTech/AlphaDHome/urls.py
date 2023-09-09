from django.contrib import admin
from django.urls import path
from .views import home, update_num
urlpatterns = [
     path('', home, name='home'),
     path('update-num', update_num, name='update-num'),
]
