from django.db import models
# Create your models here.
class Articles(models.Model):
    title = models.TextField()
    content = models.TextField()
    author = models.TextField()
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)