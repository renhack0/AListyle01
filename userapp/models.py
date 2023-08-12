from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    jins = models.CharField(max_length=20, blank=True)
    shahar = models.CharField(max_length=30)
    davlar = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
