from django.contrib import admin
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    date_heirarchy=['timestamp']
    list_display=['title','price','active','updated']
    search_fields=['title','price']
    list_editable=['price','active']
    list_filter=['price','active']
    readonly_fields=['timestamp','updated']
    prepopulated_fields={"slug":("title",)}
    class Meta:
        model=Product
admin.site.register(Product, ProductAdmin)