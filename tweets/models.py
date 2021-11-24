from django.db import models


class Tweet(models.Model):
    # id = models.AutoField(primary_key=True)  -- Hidden field
    content = models.TextField(blank=True, null=True)
    # it will store in the sqlite file the url for the image instead
    image = models.FileField(upload_to='images/', blank=True, null=True)
