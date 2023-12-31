# Generated by Django 4.2.5 on 2023-12-10 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0006_alter_game_options'),
        ('PlayFront', '0011_playercards_delete_colodax16'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coloda',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerPlay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('gameID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FrontEnd.game')),
                ('playerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlayFront.player')),
            ],
        ),
    ]
