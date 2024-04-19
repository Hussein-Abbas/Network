from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # People who the user is following them
    following = models.ManyToManyField('self', related_name='followers', symmetrical=False, null=True, blank=True)