from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.


class blogPost (models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    heading_one = models.CharField(max_length=500)
    content_one = models.CharField(max_length=7500)
    heading_two = models.CharField(max_length=500)
    content_two = models.CharField(max_length=7500)
    heading_three = models.CharField(max_length=500)
    content_three = models.CharField(max_length=7500)
    publish_date = models.DateField()
    thumbnail = models.ImageField(upload_to="blog/images", default="")

    def __str__(self):
        return self.title[0:25]
