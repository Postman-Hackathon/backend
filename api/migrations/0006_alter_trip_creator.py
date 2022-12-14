# Generated by Django 3.2.6 on 2022-11-23 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_remove_trip_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_trips', to=settings.AUTH_USER_MODEL),
        ),
    ]
