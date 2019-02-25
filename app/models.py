from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    user_id = models.CharField(max_length =8)
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=5)
    major = models.CharField(max_length=200)
    bio = models.TextField(max_length=600)
    skills = models.CharField(max_length=100)
    courses = models.CharField(max_length=200)      # eventually drop down menu? hashtags?
    organizations = models.CharField(max_length=200)
    interests = models.CharField(max_length=100)
    image = models.ImageField(default='default-avatar.jpg', upload_to='profile_pics')
    # picture = models.ImageField()


class ProfileModel(ModelForm):
    model = Profile
    fields = ['user_id', 'name', 'year', 'major', 'bio', 'skills', 'courses','organizations', 'interests']
    # waiting to add picture for now

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

