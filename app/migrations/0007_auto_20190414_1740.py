# Generated by Django 2.1.7 on 2019-04-14 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190414_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='endorse',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='endorsements',
        ),
    ]
