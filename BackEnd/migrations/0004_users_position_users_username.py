# Generated by Django 4.2.5 on 2023-11-06 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Center', '0003_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='position',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='userName',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]