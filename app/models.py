from django.db import models
from taggit.managers import TaggableManager
from django import forms
from django.forms import ModelForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from jsonfield import JSONField

YEARS = (
    ("2019", "2019"),
    ("2020", "2020"),
    ("2021", "2021"),
    ("2022", "2022"),
    ("Graduate Student", "Graduate Student"),
    ("Faculty", "Faculty"),
    ("Other", "Other")
)

class Skill(models.Model):
    name = models.CharField(max_length=200)
    endorsements = JSONField(models.CharField(max_length=10, default = ''), blank=True)
    endorse = models.IntegerField(default=0)
    user_id = models.CharField(max_length=10) #ex: mdt2gb
    pk_id = models.IntegerField(default=0) #ex 1, 2, 3, etc..


class Profile(models.Model):
    # model = User
    # user = models.OneToOneField(User, on_delete=models.CASCADE, default="10")
    user_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=16, choices=YEARS)
    major = models.CharField(max_length=50)
    bio = models.TextField(max_length=1000, blank=True)
    # eventually drop down menu? hashtags?
    courses = models.CharField(max_length=300, blank=True)
    organizations = models.CharField(max_length=300, blank=True)
    interests = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=500, blank=True)
    image = models.ImageField(
        default='default-avatar.jpg', upload_to='profile_pics')
    facebook_url = models.URLField(max_length=200, blank=True)
    twitter_url = models.URLField(max_length=200, blank=True)
    linkedin_url = models.URLField(max_length=200, blank=True)
    github_url = models.URLField(max_length=200, blank=True)

    def courses_as_list(self):
        return self.courses.split(',')

    def organizations_as_list(self):
        return self.organizations.split(',')

    def skills_as_list(self):
        return Skill.objects.filter(pk_id = self.id).all()

    def interests_as_list(self):
        return self.interests.split(',')

    # def clean_courses(self):
    #     courses = self.cleaned_data['courses']
    #     course_list = self.courses.split(',')
    #     for c in course_list:
    #         c = c.strip()
    #         if (len(c) > 8 or len(c) < 6):
    #             raise ValidationError('Invalid course')
    #         elif(c[0].isalpha() == False or c[1].isalpha() == False):
    #             raise ValidationError('Invalid course')
    #         elif ((len(c) == 6 and c[2].isalpha()) or (len(c) == 6 and c[3].isalpha()) or (len(c) == 6 and c[4].isalpha()) or (len(c) == 6 and c[5].isalpha())):
    #             raise ValidationError('Invalid course')
    #         elif ((len(c) == 7 and c[2].isalpha() == False) or (len(c) == 7 and c[3].isalpha()) or (len(c) == 7 and c[4].isalpha()) or (len(c) == 7 and c[5].isalpha()) or (len(c) == 7 and c[6].isalpha())):
    #             raise ValidationError('Invalid course')
    #         elif ((len(c) == 8 and c[2].isalpha() == False) or (len(c) == 8 and c[3].isalpha() == False) or c[4].isalpha() or c[5].isalpha() or c[6].isalpha()):
    #             raise ValidationError('Invalid course')
    #     return True


    # picture = models.ImageField()
    @classmethod
    def add_endorse(cls):
        cls.endorse += 1

    @classmethod
    def add_endorsement(cls, string):
        cls.endorsements += ", " + str(string)

    tags = TaggableManager()


class ProfileModel(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'year', 'major', 'bio',
                  'courses', 'organizations', 'interests', 'status', 'image']
        # waiting to add picture for now

        # def save(self, commit=True):
        #     user = super(ProfileModel, self).save(commit=False)
        #
        #     if commit:
        #         user.save()
        #
        #     return user

class SkillsModel(ModelForm):
    class Meta:
        model = Skill
        fields = ['name']

class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'year', 'major', 'bio',
                  'courses', 'organizations', 'interests', 'status', 'image']
        # waiting to add picture for now


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(
        User, related_name='owner', null=True, on_delete=models.CASCADE)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)
