# Generated by Django 4.2.5 on 2023-12-10 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0006_alter_game_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='number',
            field=models.IntegerField(max_length=5, primary_key=True, serialize=False, verbose_name='Номер'),
        ),
    ]
