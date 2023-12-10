from django.db import models
from django.contrib.auth.models import User
from FrontEnd.models import Game

# Create your models here.
class Player(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    position = models.SmallIntegerField()
    game = models.SmallIntegerField()

    def __str__(self) -> str:
        return str(self.id)

class PlayerPlay(models.Model):
    playerID = models.ForeignKey(Player, models.CASCADE)
    gameID = models.ForeignKey(Game, models.CASCADE)
    status = models.BooleanField()

class Card(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('Название', max_length=10)
    descriptin = models.TextField('Описание', null=True, blank=True)
    function = models.ForeignKey('CardFunction', models.CASCADE, verbose_name='Функция')
    image = models.ImageField('Изображение', null=True, blank=True)
    maxPlayerInGame = models.IntegerField('Максиьальное число игрков', default=0)
    maxCardInColoda = models.IntegerField('Максиьальное число карт в колоде', default=0)

    def __str__(self) -> str:
        return str(self.id)

    class Meta():
        verbose_name = "карту"
        verbose_name_plural = "Карты"

class CardFunction(models.Model):
    id = models.BigAutoField(primary_key=True)
    function = models.CharField('Функция', max_length=100)
    
    def __str__(self) -> str:
        return self.function    

    class Meta():
        verbose_name = "функцию карты"
        verbose_name_plural = "Функции карт"

class Coloda(models.Model):
    id = models.BigIntegerField(primary_key=True)

class PlayerCards(models.Model):
    id = models.BigAutoField(primary_key=True)
    card_1 = models.ForeignKey(Card, models.CASCADE, related_name='card_1')
    card_2 = models.ForeignKey(Card, models.CASCADE, related_name='card_2')
    card_3 = models.ForeignKey(Card, models.CASCADE, related_name='card_3')
    card_4 = models.ForeignKey(Card, models.CASCADE, related_name='card_4')
    card_5 = models.ForeignKey(Card, models.CASCADE, related_name='card_5', null=True, blank=True)
    playerID = models.ForeignKey(Player, models.CASCADE)