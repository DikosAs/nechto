# Generated by Django 4.2.5 on 2023-12-12 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0012_alter_game_id'),
        ('PlayFront', '0015_rename_game_player_gameid'),
    ]

    operations = [
        migrations.AddField(
            model_name='coloda',
            name='coloda',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coloda',
            name='gameID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FrontEnd.game'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coloda',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
