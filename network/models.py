from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator


class User(AbstractUser):
    following = models.ManyToManyField('self', related_name='followers', symmetrical=False, null=True, blank=True)


    def __str__(self):
        return self.username


class Post(models.Model):
    poster = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    date = models.DateField(auto_now_add=True, editable=False)
    likes = models.IntegerField(default=0, null=False, blank=False, validators=[MinValueValidator(0)])


    def __str__(self):
        return self.content

