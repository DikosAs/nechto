# Generated by Django 4.2.5 on 2023-12-05 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlayFront', '0004_rename_gameid_player_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='game',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.SmallIntegerField(blank=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.SmallIntegerField(auto_created=True, blank=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='username',
            field=models.TextField(),
        ),
    ]