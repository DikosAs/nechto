# Generated by Django 4.2.5 on 2023-12-10 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PlayFront', '0014_rename_gameid_player_game'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='game',
            new_name='gameID',
        ),
    ]
