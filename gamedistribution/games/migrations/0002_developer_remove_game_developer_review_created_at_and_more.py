# Generated by Django 5.0.4 on 2024-04-08 15:15

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='developer',
        ),
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('game', 'user')},
        ),
        migrations.AddField(
            model_name='game',
            name='developers',
            field=models.ManyToManyField(related_name='games', to='games.developer'),
        ),
    ]
