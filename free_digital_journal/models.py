from django.db import models

# Create your models here.
class Free_Download(models.Model):
    file_number = models.CharField(max_length=32, null=False, editable=False)
    title = models.CharField(max_length=200, unique=True)
    file = models.FileField(upload_to='file/')
    author = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
       return self.title
