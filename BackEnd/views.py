from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import *
from .models import *

# Create your views here.
def addGame(req):
    if req.method == "POST":
        form = NewGameForm(req.POST, req.FILES)
        print(req.POST)
        print(req.FILES)
        print("Форма: ", form.is_valid(), "\n\n", form)
        if form.is_valid():
            games = Games(**form.cleaned_data)
            games.save()
            return redirect(reverse("create-game.html"))
    else:
        form = NewGameForm()
        return render(req, "create-game.html", context={"form": form})

    print(req)
    print(req.method)

