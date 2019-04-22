from django.contrib import admin

# Register your models here.
from .models import Profile, Post, Friend, Skill

admin.site.register(Profile)

admin.site.register(Post)

admin.site.register(Friend)

admin.site.register(Skill)
