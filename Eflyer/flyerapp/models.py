from django.db import models

# Create your models here.

class Products(models.Model):
    Category = (
        ('Fashion', 'Fashion'),
        ('Electronics' , 'Electronics'),
        ('Food','Food'),
        ('Cosmatics','Cosmatics'),
    )
    product_name = models.CharField(max_length=100, null=True)
    product_description = models.CharField(max_length=300, null=True)
    product_price = models.FloatField(max_length=30, null=True)
    category = models.CharField(max_length=200, null=True, choices=Category)
    product_images = models.ImageField(null=True)  
    
    def __str__(self) -> str:
        return self.product_name
    
class order(models.Model):
    pname = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    #pcat = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    
    def __str__(self) -> str:
        return self.pname