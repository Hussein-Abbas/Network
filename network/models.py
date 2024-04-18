from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator


class User(AbstractUser):
    followers_count = models.IntegerField(default=0, validators=[MinValueValidator(0)], null=False, blank=False)
    following_count = models.IntegerField(default=0, validators=[MinValueValidator(0)], null=False, blank=False)

    # People who the user is following them
    following = models.ManyToManyField('self', symmetrical=False, null=True, blank=True)
