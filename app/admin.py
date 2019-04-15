from django.contrib import admin

# Register your models here.
from .models import Profile, Post, Friend

admin.site.register(Profile)

admin.site.register(Post)

admin.site.register(Friend)
