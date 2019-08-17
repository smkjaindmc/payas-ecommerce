from django.contrib import admin

from .models import Cart
class CartAdmin(admin.ModelAdmin):
    class Meta:
        model= Cart
admin.site.register(Cart,CartAdmin)        
        
        
