

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

class User(AbstractUser):

    username = models.TextField(blank=True, unique=True, default="")
    password = models.TextField(blank=True)
    email_adress = models.TextField(blank=True)
    #profile_pic = models.ImageField(blank=True)
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name="meal_master_user_groups")
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('_user permissions'),
        blank=True,
        related_name='meal_master_user_permission',
        help_text=_('_Specific permissions for this user.'),
    )

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

    def __str__(self):
        return self.username
