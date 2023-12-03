from django.shortcuts import render, redirect, reverse 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.
def games(request: WSGIRequest):
    return render(request, 'games-list.html')

def reg_(request: WSGIRequest):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse("game"))
        else:
            return render(request, 'register.html', {'form': UserCreationForm})
        
    form = UserCreationForm(request.POST)
    
    if form.is_valid():        
        form.save()

        username = request.POST["username"]
        password = request.POST["password1"]

        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect(reverse('game'))


def login_(request: WSGIRequest):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse("game"))
            pass
        else:
            return render(request, 'login.html')
        
    username = request.POST["account-name"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse("game"))
    return render(request, "auth/login.html", context={"error": "Неправильный логин или пароль"})

def logout_(request: WSGIRequest):
    logout(request)
    return redirect(reverse("login"))