from django.db import models

# Create your models here.
class category_db(models.Model):
    Name = models.CharField(max_length=30,null=True,blank=True)
    Description = models.CharField(max_length=100,null=True,blank=True)
    Image = models.ImageField(upload_to="profile",null=True,blank=True)

class product_db(models.Model):
    Category_Name = models.CharField(max_length=30,null=True,blank=True)
    Product_Name = models.CharField(max_length=30,null=True,blank=True)
    Product_Description = models.CharField(max_length=100,null=True,blank=True)
    Product_Price = models.IntegerField(null=True,blank=True)
    Product_Image = models.ImageField(upload_to="profile",null=True,blank=True)
