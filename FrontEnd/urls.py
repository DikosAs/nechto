from django.urls import path, include
from django.shortcuts import redirect
from django.urls import reverse
from .views import *

urlpatterns = [
    path('reg.html', reg_, name='reg'),
    path('login.html', login_, name='login'),
    path('logout', logout_, name='logout'),
    path('play/', games, name='play'),
    path('play/', include('games_urls')),
    path('', games),
]