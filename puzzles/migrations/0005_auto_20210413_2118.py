# Generated by Django 3.2 on 2021-04-13 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzles', '0004_auto_20210411_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzle',
            name='bad_ratings',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='good_ratings',
            field=models.IntegerField(default=0),
        ),
    ]
