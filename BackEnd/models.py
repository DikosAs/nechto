from django.db.models import *

# Create your models here.
class Games(Model):
    gameID = IntegerField(primary_key=True)
    gamePassword = TextField(null=True)
    gameAdmin = TextField()

class Users(Model):
    userName = TextField(primary_key=True)
    userPassword = TextField()

class Users_In_Game(Model):
    userID = OneToOneRel(IntegerField(primary_key=True), "User", "id")
    gameID = ManyToOneRel(IntegerField(), "Games", "gameID")
    position = IntegerField(primary_key=True)