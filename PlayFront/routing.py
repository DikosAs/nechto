from django.urls import path
from .conseumer import *

ws_patterns = [
    path('ws/game.socket/', GameData),
]