# Generated by Django 4.2.7 on 2023-11-21 11:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_users_created_alter_users_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
