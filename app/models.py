from django.db import models
from django.forms import ModelForm

class Profile(models.Model):
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=5)
    major = models.CharField(max_length=200)
    bio = models.TextField(max_length=600)
    skills = models.CharField(max_length=100)
    courses = models.CharField(max_length=200)      # eventually drop down menu? hashtags?
    organizations = models.CharField(max_length=200)
    interests = models.CharField(max_length=100)
    # picture = models.ImageField()


class ProfileModel(ModelForm):
    model = Profile
    fields = ['name', 'year', 'major', 'bio', 'skills', 'courses','organizations', 'interests']
    # waiting to add picture for now

