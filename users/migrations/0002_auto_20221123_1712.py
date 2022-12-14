# Generated by Django 3.2.6 on 2022-11-23 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='past_trips',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='api.Trip'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='upcoming_trips',
            field=models.ManyToManyField(blank=True, related_name='users_confirmed', to='api.Trip'),
        ),
    ]
