from django.db import models

class Product(models.Model):
    title=models.CharField(max_length=120)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.FileField(upload_to='products/images/',null=True)
    image2=models.FileField(upload_to='products/images/',null=True)
    slug=models.SlugField(unique=True)
    timestamp=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.title


        