from rest_framework import serializers
from .models import Order
from .models import Product

class OrderSerializer(serializers.ModelSerializer):
    fromDate=serializers.DateField(format="%Y-%m-%d",input_formats=["%Y-%m-%d"])
    endDate=serializers.DateField(format="%Y-%m-%d",input_formats=["%Y-%m-%d"])
    class Meta:
        model = Order
        fields = ['name','email','phone','fromDate','endDate','quantity','deliverytime','address','pincode','created_at']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'        
