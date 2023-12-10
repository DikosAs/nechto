# Generated by Django 4.2.5 on 2023-12-05 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0005_alter_game_number_alter_game_password'),
        ('PlayFront', '0002_rename_name_player_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='gameID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='FrontEnd.game'),
            preserve_default=False,
        ),
    ]
