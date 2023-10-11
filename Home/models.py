from django.db import models

# Create your models here.
class Gun(models.Model):
    id = models.IntegerField(primary_key=True)
    
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    in_stock = models.BooleanField()
    def __str__(self):
        return self.name

