# Generated by Django 5.0.4 on 2024-04-09 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_game_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='downloads',
            field=models.IntegerField(default=0),
        ),
    ]
