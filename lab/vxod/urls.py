from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home),
    path('reg/', reg),
    path('avt/', avt)
]