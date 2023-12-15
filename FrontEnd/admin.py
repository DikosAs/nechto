from django.contrib import admin
from .models import Game

# Register your models here.
class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'password']

admin.site.register(Game, GameAdmin)