# Generated by Django 3.2 on 2021-04-24 09:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0004_songs_uploaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='Song_upload',
            field=models.FileField(default=django.utils.timezone.now, max_length='100', upload_to='none'),
            preserve_default=False,
        ),
    ]