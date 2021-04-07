from django.contrib import admin
from .models import (Customer,Product,Cart,OrderPlaced,Profile)


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
    list_display=['id','user','customer','product','quantity','Purchased_Date','Status']