# Generated by Django 4.2.5 on 2023-11-12 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Center', '0005_remove_games_id_alter_games_gameid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.AlterField(
            model_name='users',
            name='position',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
