from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('reg.html', reg_, name='reg'),
    path('login.html', login_, name='login'),
    path('logout', logout_, name='logout'),
    path('games/', games, name='games')
]
