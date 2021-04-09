from django.contrib import admin
from .models import (Customer,Product,Cart,OrderPlaced,Profile)
from django.urls import reverse
from django.utils.html import format_html

admin.site.register(Profile)

@ admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','place','area','Pradesh']


@ admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','Price','Selling_Price','Description','Manufacturer','category','Image']

@ admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

@ admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','ordered_date','status']


    def customer_info(self,obj):
        link=reverse("admin:BC_customer_change",args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>',link,obj.customer.name)
    
    def product_info(self,obj):
        link=reverse("admin:BC_product_change",args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>',link,obj.product.title)