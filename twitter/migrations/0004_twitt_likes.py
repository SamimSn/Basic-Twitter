# Generated by Django 4.2.7 on 2024-01-02 15:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twitter', '0003_alter_twitt_created_time_alter_twitt_updated_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitt',
            name='likes',
            field=models.ManyToManyField(related_name='twitt_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
