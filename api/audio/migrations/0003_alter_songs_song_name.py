# Generated by Django 3.2 on 2021-04-22 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0002_remove_songs_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='Song_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
