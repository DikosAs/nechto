from django.contrib import admin
from .models import Card, CardFunction

# Register your models here.
class CardAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'descriptin', 'function']

class CardFunctionAdmin(admin.ModelAdmin):
    list_display = ['id', 'function']

admin.site.register(Card, CardAdmin)
admin.site.register(CardFunction, CardFunctionAdmin)