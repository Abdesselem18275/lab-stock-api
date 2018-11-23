import datetime
from django.db import models


TRANS_TYPE = (
    ('IN', 'ENTREE'),
    ('OUT', 'SORTIE'))


class Famille(models.Model):
    designation = models.CharField(unique=True,max_length=100, blank=True, default='') 
    def __str__(self):
        return self.designation

class Laboratoire(models.Model):
    designation = models.CharField(unique=True,max_length=100, blank=True, default='') 
    def __str__(self):
        return self.designation

class Product(models.Model):
    designation = models.CharField(unique=True,max_length=100, blank=True, default='')
    reference = models.CharField(max_length=100, default='')
    creation_date = models.DateField(default=datetime.date.today)
    contenantCoffret = models.IntegerField(default='1', null=True)
    testContenant = models.IntegerField(default='1', null=True)
    cmm = models.IntegerField(default='1', null=True)
    StockMiniMois = models.IntegerField(default='1', null=True)
    famille = models.ForeignKey(Famille, related_name='products',on_delete=models.SET_NULL, blank=True, null=True)
    laboratoire = models.ForeignKey(Laboratoire,related_name='products', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.designation

class ProductTrans(models.Model):
    numero_lot = models.IntegerField(unique=True,blank=False)
    produit = models.ForeignKey(Product,related_name='transactions', on_delete=models.SET_NULL, blank=True, null=True)
    quantite = models.IntegerField(default='1',blank=False)
    modification_date=models.DateTimeField(default=datetime.date.today)
    peremption_date = models.DateField(default=datetime.date.today)
    trans_type = models.CharField(max_length=10,choices=TRANS_TYPE)
    def __str__(self):
        return self.designation
    

