# Generated by Django 2.1.5 on 2019-04-05 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_friend_current_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year',
            field=models.CharField(choices=[('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('Graduate Student', 'Graduate Student'), ('Faculty', 'Faculty'), ('Other', 'Other')], max_length=16),
        ),
    ]