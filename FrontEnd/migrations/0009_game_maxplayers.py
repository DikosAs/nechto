# Generated by Django 4.2.5 on 2023-12-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0008_alter_game_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='maxPlayers',
            field=models.SmallIntegerField(default=0, verbose_name='Максимум игроков'),
            preserve_default=False,
        ),
    ]
