from django.db import models
from cart.models import Cart
class Register(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    prof=models.ManyToManyField(Cart,null=True,blank=True)
class Checkout(models.Model):
    order_id = models.AutoField(primary_key=True,default=0)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    phone=models.CharField(max_length=100)
    adress=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    
    
    
    