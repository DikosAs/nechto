# Generated by Django 4.2.5 on 2023-12-05 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0004_rename_games_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='number',
            field=models.CharField(max_length=5, primary_key=True, serialize=False, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='game',
            name='password',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Пароль'),
        ),
    ]