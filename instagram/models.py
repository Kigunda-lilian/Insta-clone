from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT,related_name='user_images')
    image = models.ImageField(upload_to = 'media/', null = True, blank = True)
    name = models.CharField(max_length=40)
    caption = models.CharField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True)
    liked= models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    comment = models.IntegerField(blank=True,null=True,default=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    
    
    class meta:
        ordering =['posted_on']