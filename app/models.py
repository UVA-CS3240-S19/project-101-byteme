from django.db import models
from django import forms
from django.forms import ModelForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from jsonfield import JSONField

from taggit.managers import TaggableManager


class Profile(models.Model):
    # model = User
    # user = models.OneToOneField(User, on_delete=models.CASCADE, default="10")
    user_id = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=100)
    major = models.CharField(max_length=200)
    bio = models.TextField(max_length=600, blank=True)
    skills = models.CharField(max_length=100, blank=True)
    # eventually drop down menu? hashtags?
    courses = models.CharField(max_length=200, blank=True)
    organizations = models.CharField(max_length=200, blank=True)
    interests = models.CharField(max_length=100, blank=True)
    image = models.ImageField(
        default='default-avatar.jpg', upload_to='profile_pics')

    tags = TaggableManager()
    endorsements = JSONField(models.CharField(max_length=10), blank=True)
    endorse = models.IntegerField(default=0)
    # picture = models.ImageField()


class ProfileModel(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'year', 'major', 'bio', 'skills',
                  'courses', 'organizations', 'interests']
        # waiting to add picture for now

        # def save(self, commit=True):
        #     user = super(ProfileModel, self).save(commit=False)
        #
        #     if commit:
        #         user.save()
        #
        #     return user


class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'year', 'major', 'bio', 'skills',
                  'courses', 'organizations', 'interests']
        # waiting to add picture for now


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
