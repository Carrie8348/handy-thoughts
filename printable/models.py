from django.db import models

# Create your models here.
class File(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=30, blank=True, null=True)
    file = models.FileField(upload_to='files/')
    description = models.TextField(max_length=300, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)


    @staticmethod
    def get_files_by_id(ids):
        return Files.objects.filter(id__in=ids)
  
    @staticmethod
    def get_all_files():
        return Files.objects.all()
  

def __str__(self):
    return self.title