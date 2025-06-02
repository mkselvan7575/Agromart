from django.db import models
from django.utils import timezone
import os
import datetime
from datetime import date,timedelta


def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

def default_to_date():
    return date.today()+timedelta(days=15)

class Product(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to=getFileName,null=False,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    rating=models.IntegerField(null=False,blank=False)
    aosDelay=models.CharField(max_length=5,default="enter the delay timing")


    def __str__(self):
        return self.name  


class Order(models.Model):
    name=models.CharField(default="Enter your Name",max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    fromDate=models.DateField(default=date.today)
    endDate=models.DateField(default=default_to_date)
    quantity = models.IntegerField()
    deliverytime=models.CharField(max_length=50,default='enter the shift')
    address=models.TextField(default="address is required")
    pincode=models.CharField(max_length=6,default="000000")
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
