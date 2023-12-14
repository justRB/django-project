from django.db import models
from django.utils import timezone

# Teams
class Teams(models.Model):
    name = models.CharField(max_length=20, unique=True)
    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(default=timezone.now())

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        return super().save(*args, **kwargs)

# Users 
class Users(models.Model):
    username = models.CharField(max_length=20, unique=True, null=False)
    password = models.BinaryField(max_length=100, null=False)
    isAdmin = models.BooleanField(default=False)
    team = models.ForeignKey(Teams, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(default=timezone.now())

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'

    is_active = models.BooleanField(default=True)

    @property
    def is_anonymous(self):
        return False
    
    @property
    def is_authenticated(self):
        return True

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        return super().save(*args, **kwargs)