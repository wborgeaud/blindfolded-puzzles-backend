# Generated by Django 3.2 on 2021-04-13 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puzzles', '0006_puzzleid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='puzzleid',
            old_name='puzzle_id',
            new_name='puzzle',
        ),
    ]
