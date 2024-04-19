from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('poster', 'content', 'date', 'likes')


admin.site.register(User)
admin.site.register(Post, PostAdmin)
