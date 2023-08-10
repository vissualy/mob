from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from .validators import filesize
class Category(models.Model):
    tittle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    def __str__(self):
        return self.tittle
class Product(models.Model):
    ACTIVE = 'active'
    DELETED = 'deleted'
    STATUS_CHOICES = (
        (ACTIVE,"active"),
        (DELETED,"deleted")
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="products")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products',null=True)
    tittle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    video = models.FileField(upload_to="video/%y",validators=[filesize],null=True)
    video_count = models.PositiveBigIntegerField(default=0)
    banner = models.ImageField(upload_to=("bannerimage"),null=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default=ACTIVE)
    def __str__(self):
        return self.user.username
    def save(self, *args, **kwargs):
        if self.pk is None:  # Only multiply price during creation
            self.price *= 100
        super(Product, self).save(*args, **kwargs)
    def pricedisplay(self):
        return self.price / 100 
    