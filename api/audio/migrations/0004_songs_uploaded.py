# Generated by Django 3.2 on 2021-04-22 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0003_alter_songs_song_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='Uploaded',
            field=models.BooleanField(default=False),
        ),
    ]
