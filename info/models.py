from django.db import models

class Info(models.Model):
    cake=models.IntegerField(null=True)
    timestamp=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)