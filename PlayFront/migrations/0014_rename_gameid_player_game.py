# Generated by Django 4.2.5 on 2023-12-10 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PlayFront', '0013_remove_player_game_player_gameid_delete_playerplay'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='gameID',
            new_name='game',
        ),
    ]