# Generated by Django 2.1.5 on 2019-04-08 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_merge_20190405_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='github_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_url',
            field=models.URLField(blank=True),
        ),
    ]
