# Generated by Django 4.2.5 on 2023-12-08 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlayFront', '0006_card_alter_player_id_alter_player_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardFunction',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('function', models.CharField(max_length=100, verbose_name='Функция')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='descriptin',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='card',
            name='function',
            field=models.SmallIntegerField(blank=True, verbose_name='ID функции'),
        ),
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(max_length=10, verbose_name='Название'),
        ),
    ]
