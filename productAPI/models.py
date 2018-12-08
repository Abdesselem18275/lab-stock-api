import datetime
from django.db import models
from django.utils import timezone
from django.db.models import Sum



TRANS_TYPE = (
    ('IN', 'ENTREE'),
    ('OUT', 'SORTIE'))

class Famille(models.Model):
    designation = models.CharField(unique=True,max_length=100, blank=False, default='') 
    modification_date=models.DateTimeField(default=timezone.now,blank=False)
    creation_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.designation

class Laboratoire(models.Model):
    designation = models.CharField(unique=True,max_length=100, blank=False, default='') 
    modification_date=models.DateTimeField(default=timezone.now,blank=False)
    creation_date = models.DateField(default=datetime.date.today)


    def __str__(self):
        return self.designation

class Product(models.Model):
    designation = models.CharField(unique=True,max_length=100, blank=False, default='')
    reference = models.CharField(max_length=100, default='',blank=False)
    creation_date = models.DateField(default=datetime.date.today)
    modification_date=models.DateTimeField(default=timezone.now,blank=False)
    contenantCoffret = models.IntegerField(default='1', null=False)
    testContenant = models.IntegerField(default='1', null=False)
    cmm = models.IntegerField(default='1', null=False)
    StockMiniMois = models.IntegerField(default='1', null=False)
    famille = models.ForeignKey(Famille, related_name='products',on_delete=models.SET_NULL, blank=True, null=True)
    laboratoire = models.ForeignKey(Laboratoire,related_name='products', on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.designation

    @property
    def total_quantity(self):
        try :
            total_in = ProductTrans.objects.filter(product__id=self.id,trans_type = 'IN').aggregate(Sum('quantite'))["quantite__sum"]
        except TypeError as err :
             total_in = 0
        try :
            total_out = ProductTrans.objects.filter(product__id=self.id,trans_type = 'OUT').aggregate(Sum('quantite'))["quantite__sum"]
        except TypeError as err :
             total_out = 0  
        return total_in - total_out 

    @property
    def total_stock_mois(self):
        return (self.total_quantity * self.testContenant) / self.cmm



class ProductTrans(models.Model):
    code_lot =  models.CharField(max_length=100, blank=False, default='')
    product = models.ForeignKey(Product,related_name='transactions', on_delete=models.SET_NULL, blank=True, null=True)
    quantite = models.IntegerField(default='1',blank=False)
    modification_date=models.DateTimeField(default=timezone.now,blank=False)
    creation_date = models.DateField(default=datetime.date.today)
    peremption_date = models.DateField(default=datetime.date.today,blank=False)
    trans_type = models.CharField(max_length=10,choices=TRANS_TYPE)
    remarks = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.designation