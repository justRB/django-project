# Generated by Django 4.2.7 on 2023-11-21 15:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_users_created_alter_users_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 21, 15, 51, 46, 145915, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='users',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 21, 15, 51, 46, 150905, tzinfo=datetime.timezone.utc)),
        ),
    ]