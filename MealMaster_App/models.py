

from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from pkg_resources import _
from rest_framework.authtoken.models import Token

class MonImage(models.Model):

    image = models.ImageField(upload_to='images/')
    name = models.TextField(max_length=500, default="")
    description = models.TextField(max_length=800, default="")

    def __str__(self):
        return f"{self.image.name}"

class Tag(models.Model):
    tag = models.TextField(max_length=500, default="")
    def __str__(self):
        return f"{self.tag}"


