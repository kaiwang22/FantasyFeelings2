# Generated by Django 4.1.3 on 2023-08-21 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_nflplayer_current_feeling'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentimententry',
            name='times',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
