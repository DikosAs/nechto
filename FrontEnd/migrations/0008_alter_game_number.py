# Generated by Django 4.2.5 on 2023-12-10 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0007_alter_game_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='number',
            field=models.SmallIntegerField(primary_key=True, serialize=False, verbose_name='Номер'),
        ),
    ]