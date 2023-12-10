from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from .models import *
from FrontEnd.views import games, user_data
    
# Create your views here.
def game(request: WSGIRequest):
    return render(request, 'game/game.html', {'user': user_data(request)})

def add_player_id_game(request: WSGIRequest):
    if request.method == 'POST':
        gameID = request.build_absolute_uri().split('/')[-2]
        username = request.user.username
        user_in_game = Player.objects.filter(game=gameID)

        if len(User.objects.filter(username=username)) != 1:
            return JsonResponse({'status': False})
        if len(Game.objects.filter(number=gameID)) != 1:
            return JsonResponse({'status': False})
        if len(Player.objects.filter(username=username)) > 0:
            return JsonResponse({'status': False})
        
        Player.objects.create(
            id = len(Player.objects.all())+1,
            username = username,
            position = len(user_in_game),
            game = gameID
        )

        return JsonResponse({'status': True})
    
    post_data = dict(request.POST)
    print(post_data)

def exit_of_game(request: WSGIRequest):
    try:
        gameID = request.build_absolute_uri().split('/')[-2]
        username = request.user.username

        Player.objects.filter(game=gameID, username=username).delete()
        return games(request)
    except:
        return game(request)

def users_data(request: WSGIRequest):
    gameID = request.build_absolute_uri().split('/')[-2]

    return_data = {}
    lenth = 0
    players = Player.objects.filter(game=gameID)
    for player in players:
        return_data[player.position+1] = {
            'name': player.username
        }
        lenth += 1

    return JsonResponse({'users': return_data, 'users_lenth': lenth})

def cards_data(request: WSGIRequest):
    data = {}
    for card in Card.objects.all():
        data[card.id] = {
            'name': card.name,
            'descriptin': card.descriptin,
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
