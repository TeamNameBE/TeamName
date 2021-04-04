# Generated by Django 3.1.7 on 2021-04-03 15:39

import ctf.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ctf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('website', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Challenges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('points', models.IntegerField(default=0)),
                ('category', models.TextField(choices=[('pwn', 'pwn'), ('crypto', 'crypto'), ('reverse', 'reverse'), ('stegano', 'stegano'), ('osint', 'osint'), ('forensic', 'forensic')])),
                ('validate', models.BooleanField()),
                ('ctf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf.ctf')),
                ('user', models.ForeignKey(on_delete=models.SET(ctf.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
