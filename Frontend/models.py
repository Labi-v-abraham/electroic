from django.db import models

# Create your models here.
class contact_db(models.Model):
    First_name = models.CharField(max_length=20,null=True,blank=True)
    Last_name = models.CharField(max_length=20,null=True,blank=True)
    Email_id = models.CharField(max_length=30,null=True,blank=True)
    Address = models.CharField(max_length=50,null=True,blank=True)
    City = models.CharField(max_length=40,null=True,blank=True)
    Country = models.CharField(max_length=20,null=True,blank=True)
    Zip_code = models.IntegerField(null=True,blank=True)
    Telephone = models.IntegerField(null=True,blank=True)

class register_db(models.Model):
    Name = models.CharField(max_length=25,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Email = models.CharField(max_length=45,null=True,blank=True)
    Username = models.CharField(max_length=25,null=True,blank=True)
    Password = models.CharField(max_length=25,null=True,blank=True)

class cart_db(models.Model):
    username = models.CharField(max_length=30,null=True,blank=True)
    Product = models.CharField(max_length=50,null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    TotalPrice = models.IntegerField(null=True,blank=True)
    Description = models.CharField(max_length=100,null=True,blank=True)