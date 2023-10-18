from django.contrib import admin
from villageapp.models import Product



#admin.site.register(Product)# to register the tablename 

class ProductAdmin(admin.ModelAdmin ):
    list_display =['id','name','price','cat','pdetails','is_active']
    list_filter=['cat','is_active']

admin.site.register(Product,ProductAdmin)   # registering model

