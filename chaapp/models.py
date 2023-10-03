from django.db import models

# Create your models here.
class book(models.Model):
    Name = models.CharField(max_length=50, null=False)
    ISBN = models.CharField(max_length=20, null=True)
    Author = models.CharField(max_length=30, null=True)
    Press = models.CharField(max_length=20, null=True)
    Content = models.CharField(max_length=500, blank=True)
    Cover = models.CharField(max_length=255, blank=True)
    Classify = models.CharField(max_length=20, blank=True)
    Price = models.CharField(max_length=20, null=False)
    Purchased = models.IntegerField(null=True)

class order(models.Model):
    subtotal = models.IntegerField(default=0)
    shipping = models.IntegerField(default=0)
    grandtotal = models.IntegerField(default=0)
    customname =  models.CharField(max_length=100, default='')
    customemail =  models.CharField(max_length=100, default='')
    customaddress =  models.CharField(max_length=100, default='')
    customphone =  models.CharField(max_length=100, default='')
    paytype =  models.CharField(max_length=50, default='')
    def __str__(self):
        return self.customname

class detail(models.Model):
    dorder = models.ForeignKey('order', on_delete=models.CASCADE)
    pname = models.CharField(max_length=100, default='')
    unitprice = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    dtotal = models.IntegerField(default=0)
    def __str__(self):
        return self.pname
