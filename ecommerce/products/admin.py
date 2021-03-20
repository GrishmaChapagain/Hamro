from django.contrib import admin
from .models import Customer


admin.site.register(Customer)
# class CustomerModelAdmin(admin.ModelAdmin):
#     list_display=['id','user','name','place','area','Pradesh']
