from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)

    # People who the user is following them
    following = models.ManyToManyField('self', symmetrical=False, null=True, blank=True)

