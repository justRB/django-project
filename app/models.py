from django.db import models
from django.utils import timezone

class Users(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)
    isAdmin = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.datetime.now())
    updated = models.DateTimeField(default=timezone.datetime.now())

    def save(self, *args, **kwargs):
        self.updated = timezone.datetime.now()
        return super().save(*args, **kwargs)
