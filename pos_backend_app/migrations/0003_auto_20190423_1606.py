# Generated by Django 2.1 on 2019-04-23 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos_backend_app', '0002_auto_20190423_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='Emailaddress',
        ),
        migrations.AddField(
            model_name='users',
            name='Email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]