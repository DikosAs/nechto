from django.db import models

# Create your models here.
class Accounts(models.Model):
    name = models.CharField('Ник', primary_key=True, max_length=25)
    password = models.CharField('Пароль', max_length=1024)