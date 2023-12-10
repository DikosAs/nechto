from django.db import models

# Create your models here.
class Game(models.Model):
    number = models.CharField('Номер', primary_key=True, max_length=5)
    password = models.CharField('Пароль', max_length=1024, null=True, blank=True)

    class Meta():
        verbose_name = "игру"
        verbose_name_plural = "Игры"