# Generated by Django 4.2.5 on 2023-11-12 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Center', '0004_users_position_users_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='id',
        ),
        migrations.AlterField(
            model_name='games',
            name='gameID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='games',
            name='gamePassword',
            field=models.TextField(null=True),
        ),
    ]
