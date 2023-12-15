from django.db import models

# Create your models here.
class Game(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField('Пароль', max_length=1024, null=True, blank=True)
    maxPlayers = models.SmallIntegerField('Максимум игроков')

    def __str__(self) -> str:
        return str(self.id)

    class Meta():
        verbose_name = "игру"
        verbose_name_plural = "Игры"