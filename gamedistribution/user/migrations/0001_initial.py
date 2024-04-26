# Generated by Django 5.0.4 on 2024-04-26 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('surname', models.CharField(max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('contact_number', models.CharField(blank=True, max_length=50)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
