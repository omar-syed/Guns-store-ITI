from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField()
    image       = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

class Gun(models.Model):
    
    name        = models.CharField(max_length=100)
    image       = models.ImageField(upload_to='Home/images' ,null=True,blank=True)
    price       = models.IntegerField()
    description = models.TextField()
    in_stock    = models.BooleanField(null=True,blank=True)
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner       = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name
