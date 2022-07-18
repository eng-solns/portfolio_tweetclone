from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    # tweets = models.CharField(max_length=50)

class Tweet(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    # tutorial_url = models.CharField(max_length=200, blank=False, default='')
    # image_path = models.CharField(max_length=150, blank=True, null=True)
    content = models.CharField(max_length=200, blank=False, default='')
    published = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)