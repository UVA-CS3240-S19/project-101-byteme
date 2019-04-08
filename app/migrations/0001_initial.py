# Generated by Django 2.1.5 on 2019-04-08 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('year', models.CharField(choices=[('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('Graduate Student', 'Graduate Student'), ('Faculty', 'Faculty'), ('Other', 'Other')], max_length=16)),
                ('major', models.CharField(max_length=200)),
                ('bio', models.TextField(blank=True, max_length=600)),
                ('skills', models.CharField(blank=True, max_length=100)),
                ('courses', models.CharField(blank=True, max_length=200)),
                ('organizations', models.CharField(blank=True, max_length=200)),
                ('interests', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(default='default-avatar.jpg', upload_to='profile_pics')),
                ('facebook_url', models.URLField(blank=True)),
                ('twitter_url', models.URLField(blank=True)),
                ('linkedin_url', models.URLField(blank=True)),
                ('github_url', models.URLField(blank=True)),
                ('endorsements', jsonfield.fields.JSONField(blank=True, verbose_name=models.CharField(max_length=10))),
                ('endorse', models.IntegerField(default=0)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
