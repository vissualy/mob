from django.db import models
from django.core.validators import RegexValidator
import random
from django.contrib.auth.models import User
class Userprofile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="userprofile")
    is_vendor = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    bio = models.TextField(blank=True)
    mobile_number = models.IntegerField(null=True)
    location = models.CharField(max_length=100,blank=True)
    profile_picture = models.ImageField(upload_to=("media/accountimage"),blank=True)
    def __str__(self):
        return self.user.username

class Vendor(models.Model):
    NOT_SUBMMITED = "not_submmited"
    SUBMITTED = "submitted"
    DECLINED = "declined"
    ACCEPTED = "accepted"
    STATUS_CHOICES = (
        (NOT_SUBMMITED,"not_submmited"),
        (SUBMITTED,'submitted'),
        (DECLINED,"declined"),
        (ACCEPTED,"accepted")
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="vendor")
    identification = models.ImageField(upload_to="media/vendorinfo/",blank=True)
    image = models.ImageField(upload_to="media/vendorinfo/",blank=True)
    identification_number = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile_number = models.IntegerField()
    bussiness_name = models.CharField(max_length=100)
    bussiness_address = models.CharField(max_length=100)
    bussiness_number = models.CharField(max_length=100)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,default=NOT_SUBMMITED)
    def __str__(self):
        return self.user.username