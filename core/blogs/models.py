from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=300)
    content=models.TextField()
    created_time=models.DateTimeField()
    author_name=models.CharField(max_length=300)
    def __str__(self):
        return self.title