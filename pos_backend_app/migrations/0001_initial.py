# Generated by Django 2.1 on 2019-04-23 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10)),
                ('DateOfBirth', models.DateField()),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile', models.PositiveIntegerField(default=755228899)),
                ('Status', models.BooleanField(default='false')),
            ],
        ),
    ]