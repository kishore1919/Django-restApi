from django.db import models

# Create your models here.
class Songs(models.Model):
    Song_upload = models.FileField(upload_to ='Songs')
    Song_name = models.CharField(max_length=100,blank=False,unique=True )
    Song_duration = models.IntegerField()
    Upload_time = models.DateTimeField(auto_now_add=True)
    Uploaded = models.BooleanField(default=False)

    def __str__(self):
        return self.Song_name


