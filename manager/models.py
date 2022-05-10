from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class createnewpercel(models.Model):
    newmerchant_name = models.CharField(max_length=222,unique=True)
    newpercel_id = models.CharField(max_length=222,unique=True)
    
    def __str__(self):
        return self.newmerchant_name

    
class createcheckorder(models.Model):
    # Country Choices
    divison = (
        ('1', 'dhaka divison'),
        ('2', 'outside dhaka vision'),
        ('3', 'outside dhaka'),
        
    )
    weight = (
        ('1','500 t0 2kg'),
        ('2','3 kg'),
        ('3', '4 kg'),
        ('4','5 kg'),

    )
    product_divison= models.CharField(max_length=300, choices = divison)
    product_weight= models.CharField(max_length=300, choices= weight)
    
    def __str__(self):
        return self.product_divison



    
class createorder(models.Model):
    # Country Choices
    CHOICES = (
        ('1', 'stylezone'),
        ('2', 'delivery1'),
        ('3', 'merchant2'),
        ('4', 'merchant3'),
        ('5', 'merchant4'),
    )
    product_type = (
        ('1','Fragile'),
        ('2','Liquid]'),

    )
    select_merchant= models.CharField(max_length=300, choices = CHOICES)
    product_type = models.CharField(max_length=300, choices= product_type)
    merchant_id = models.CharField(max_length=4)
    def __str__(self):
        return self.select_merchant

