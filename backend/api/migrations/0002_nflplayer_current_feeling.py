# Generated by Django 4.1.3 on 2023-08-21 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nflplayer',
            name='current_feeling',
            field=models.FloatField(default=0.0),
        ),
    ]