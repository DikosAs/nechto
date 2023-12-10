# Generated by Django 4.2.5 on 2023-12-08 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlayFront', '0005_alter_player_game_alter_player_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('function', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.SmallIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.SmallIntegerField(),
        ),
    ]
