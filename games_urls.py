from django.urls import path, include
from FrontEnd.models import Game

urlpatterns = []

for game_num in list(Game.objects.all()):
    urlpatterns.append(path(f'{str(game_num.id)}/', include('PlayFront.urls')))