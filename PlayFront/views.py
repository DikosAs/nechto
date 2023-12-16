from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.urls import reverse
from .models import *
from FrontEnd.views import user_data
from random import shuffle
from time import sleep


# Create your views here.
def game(request: WSGIRequest):
    return render(request, 'game/game.html', {'user': user_data(request)})


def add_player_id_game(request: WSGIRequest):
    if request.method == 'POST':
        game_id: Game = Game.objects.get(id=int(request.build_absolute_uri().split('/')[-2]))
        username: str = str(request.user.username)
        user_in_game: list = list(Player.objects.filter(gameID=game_id))

        if len(user_in_game) > game_id.maxPlayers:
            return JsonResponse({'status': False})
        if len(User.objects.filter(username=username)) != 1:
            return JsonResponse({'status': False})
        if len(Player.objects.filter(username=username)) > 0:
            return JsonResponse({'status': False})

        Player.objects.create(
            username=username,
            position=len(user_in_game),
            gameID=game_id
        )

        if game_id.maxPlayers >= len(Player.objects.filter(gameID=game_id)):
            if len(Coloda.objects.filter(gameID=game_id)) == 0:
                cards = []
                for card in Card.objects.filter(maxCardInColoda__lte=game_id.maxPlayers):
                    for num in range(card.maxPlayerInGame):
                        cards.append(card.id)

                Coloda.objects.create(
                    gameID=game_id,
                    coloda=str(shuffle(cards))
                )

        return JsonResponse({'status': True})

    post_data = dict(request.POST)
    print(post_data)


def exit_of_game(request: WSGIRequest):
    try:
        game_id = request.build_absolute_uri().split('/')[-2]
        username = request.user.username

        Player.objects.get(gameID=game_id, username=username).delete()
        sleep(1)
        if len(Player.objects.filter(gameID=game_id)) == 0:
            Coloda.objects.get(gameID=game_id).delete()
        return redirect(reverse('play'))
    except:
        return redirect(reverse('game'))


def users_data(request: WSGIRequest):
    game_id = request.build_absolute_uri().split('/')[-2]

    return_data = {}
    length = 0
    players = Player.objects.filter(gameID=game_id)
    for player in players:
        return_data[player.position + 1] = {
            'name': player.username
        }
        length += 1

    return JsonResponse({'users': return_data, 'users_length': length})


def cards_data(request: WSGIRequest):
    data = {}
    for card in Card.objects.all():
        data[card.id] = {
            'name': card.name,
            'description': card.descriptin,
            'function': str(card.function),
            'image': str(card.image)
        }
    return JsonResponse({'cards': data})

# def user_cards(request: WSGIRequest):
#     gameID = request.build_absolute_uri().split('/')[-2]
#     username = request.user.username
#     userid = request.user.id

#     table_line = PlayerCards.objects.filter(playerID=userid)[0]
#     print(table_line)
#     cardsID = [
#         table_line.card_1, 
#         table_line.card_2, 
#         table_line.card_3, 
#         table_line.card_4
#     ]
#     try:
#         cardsID.append(table_line.card_5)
#     except: pass


#     print(cardsID)
#     return JsonResponse({'cards': cardsID})
