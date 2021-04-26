from django.db import models

class Audiobook(models.Model):
    Audiobook_file = models.FileField(upload_to ='Audiobook')
    Book_Title = models.CharField(max_length=100,blank=False,unique=True )
    Book_Author = models.CharField(max_length=100,blank=False,unique=True )
    Book_Narrator = models.CharField(max_length=100,blank=False)
    Upload_time = models.DateTimeField(auto_now_add=True)
    Uploaded = models.BooleanField(default=False)

    def __str__(self):
        return self.Book_Title
