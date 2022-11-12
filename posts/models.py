from django.db import models

# Create your models here.


class Hashtag(models.Model):
    title = models.CharField(max_length=100)


class Post(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    hashtags = models.ManyToManyField(Hashtag)

