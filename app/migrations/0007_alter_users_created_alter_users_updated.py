# Generated by Django 4.2.7 on 2023-11-21 11:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_users_created_alter_users_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 21, 11, 7, 5, 845893, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='users',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 21, 11, 7, 5, 845893, tzinfo=datetime.timezone.utc)),
        ),
    ]