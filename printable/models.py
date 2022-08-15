import uuid
from django.db import models


# Create your models here.
class File(models.Model):
    file_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)
    title = models.CharField(max_length=200, unique=True)
    file = models.FileField(upload_to='file/')
    author = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
       return self.title
