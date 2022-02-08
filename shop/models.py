from email import message
from email.policy import default
from statistics import mode
import string
from unicodedata import name
from django.db import models

# Create your models here.
class product(models.Model):
    Product_id = models.AutoField
    Product_name = models.CharField(max_length=50,default="")
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    Desctription = models.CharField(max_length=300)
    Pub_Date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default="")


    def __str__(self):
        return self.Product_name

class contact(models.Model):
    message_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
    
class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, default="")