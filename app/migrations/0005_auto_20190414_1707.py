# Generated by Django 2.2 on 2019-04-14 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190414_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='user_id',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
