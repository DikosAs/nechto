from django.urls import path
from .views import *

urlpatterns = [
    path('game.html', game, name='game'),
    path('get-users-data', users_data),
    # path('get-user-cards', user_cards),
    path('get-all-cards-data', cards_data),
    path('add-player-id-game', add_player_id_game),
    path('exit', exit_of_game, name='exit'),
]