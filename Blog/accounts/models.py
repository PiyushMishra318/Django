from django.db import models
import datetime
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    username = models.CharField(blank=False,max_length=100)
    Body = models.TextField(blank=True)
    Posted_on = models.DateField(default=datetime.datetime.today)
    profileimg = models.ImageField(upload_to="static")


    def __str__(self):
        return self.Body



class Comment(models.Model):
    body = models.CharField(max_length=100,default='')
    commentid = models.CharField(max_length=100,blank=False,primary_key=False)
    text = models.CharField(max_length=100,default='')
    date = models.DateField(default=datetime.datetime.today)
    profileimg = models.ImageField(upload_to="static",default="")

    def __str__(self):
        return self.commentid


class UserProfile(models.Model):
    user =  models.OneToOneField(User,on_delete=models.CASCADE,)
    username = models.CharField(max_length=100,default='')
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100,default='')
    website = models.URLField(default='')
    Phone = models.IntegerField(default=0)
    profileimg = models.ImageField(upload_to='static')

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
