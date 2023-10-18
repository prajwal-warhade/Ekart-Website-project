from django.db import models
from django.contrib.auth.models import User #importing auth_user table 


# Create your models here. [this is SQL all querrys]
class Product(models.Model):#models.Models(models ye ek module hai  uskeke andar ka function Model)
    CAT=((1,'crop protection'),(2,'Crop neutritions'),(3,'Seeds'))
    
#SEED=((1,'HORTICULTURE'),(2,'FILED CROP'),(3,'Special CAREGORIES'),(4,'None'),)

    name=models.CharField(max_length=50,verbose_name='Product Name')
    price=models.IntegerField()
    cat=models.IntegerField(verbose_name='categories',choices=CAT)
#seed=models.IntegerField(verbose_name='Seed Categories',choices=SEED)
    pdetails=models.CharField(max_length=50,verbose_name='Product Deteils')
    is_active=models.BooleanField(default=True)#default contraits
    pimage=models.ImageField(upload_to='image')
    
class Cart(models.Model):
    userid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='userid')#fething from sessions 
    #from auth_user table data will be fetch on userid column,by foreign key
    #which means auth_user is parent table and Cart is child table. 
    #db_column='userid' using this just because it only dispaly userid.
    pid=models.ForeignKey('product',on_delete=models.CASCADE,db_column='pid')#fetching from product table
# to display the products name in admin 
    qty=models.IntegerField(default=1)
    
class Order(models.Model):
    orderid=models.IntegerField(max_length=50)
    userid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='userid')
    pid=models.ForeignKey('product',on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)
    amt=models.FloatField()
    
    
     
    
       