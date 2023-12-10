from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse_lazy, reverse
from .models import Game

def user_data(req: WSGIRequest) -> dict:
    if req.user.is_authenticated:
        return {'name': req.user.username, 'login': True}
    else:
        return {'login': False}

# Create your views here.
@login_required(login_url=reverse_lazy('login'))
def games(request: WSGIRequest):
    if request.build_absolute_uri()[-5:-1] == 'play':
        games_list = [game.number for game in list(Game.objects.all())]
        return render(request, 'game/games-list.html', {'user': user_data(request), 'games': games_list})
    else:
        return redirect(reverse("play"))

def reg_(request: WSGIRequest):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse("play"))
        else:
            return render(request, 'accout/register.html', {'form': UserCreationForm, 'user': user_data(request)})
        
    form = UserCreationForm(request.POST)
    
    if form.is_valid():        
        form.save()

        username = request.POST["username"]
        password = request.POST["password1"]

        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect(reverse('play'))


def login_(request: WSGIRequest):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse("play"))
        else:
            return render(request, 'accout/login.html', {'user': user_data(request)})
    
    print(dict(request.POST))
    username = request.POST["account-name"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse("play"))

def logout_(request: WSGIRequest):
    logout(request)
    return redirect(reverse("login"))