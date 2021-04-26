from django.db import models

class Podcast(models.Model):
    Podcast_file = models.FileField(upload_to ='Podcast')
    Podcast_name = models.CharField(max_length=100,blank=False,unique=True )
    Podcast_host = models.CharField(max_length=100,blank=False,unique=True )
    Podcast_duration = models.IntegerField()
    Upload_time = models.DateTimeField(auto_now_add=True)
    Uploaded = models.BooleanField(default=False)

    def __str__(self):
        return self.Podcast_name
