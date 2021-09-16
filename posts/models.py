from django.db import models

# Create your models here.

class Post(models.Model):
    """Stores 4 pieces of information: the title of the post, the location in which 
    the post was taken, the user who posted it, and the image."""


    objects = models.Manager()
    title = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100, default = "")
    user = models.CharField(max_length=100, default = "")
    cover = models.ImageField(upload_to='images/', default = "")

    def __str__(self):
        return self.title

class Users(models.Model):
    """Stores the username and password of each user"""

    objects = models.Manager()
    username = models.CharField(max_length=100,  default = "")
    password = models.CharField(max_length=100,  default = "")

class Comment(models.Model):
    """"Stores a comment, and the title of the post of which that comment is attatched to"""
    
    objects = models.Manager()
    title = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)