from django.db import models
from cart.models import Cart
class Register(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    prof=models.ManyToManyField(Cart,null=True,blank=True)
    
    
    
    