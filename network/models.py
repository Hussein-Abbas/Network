from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator


class User(AbstractUser):
    following = models.ManyToManyField('self', related_name='followers', symmetrical=False, null=True, blank=True)
    likes = models.ForeignKey('Post', related_name='likes', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.username


class Post(models.Model):
    poster = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    date = models.DateField(auto_now_add=True, editable=False)


    def __str__(self):
        return self.content
