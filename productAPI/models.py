import datetime
from django.db import models



class Famille(models.Model):
    designation = models.CharField(max_length=100, blank=True, default='') 

    def __unicode__(self):
        return self.designation

class Laboratoire(models.Model):
    designation = models.CharField(max_length=100, blank=True, default='') 

    def __unicode__(self):
        return self.designation


class Product(models.Model):
    designation = models.CharField(max_length=100, blank=True, default='')
    reference = models.CharField(max_length=100, default='')
    creation_date = models.DateField(default=datetime.date.today)
    contenantCoffret = models.IntegerField(default='1', null=True)
    testContenant = models.IntegerField(default='1', null=True)
    cmm = models.IntegerField(default='1', null=True)
    StockMiniMois = models.IntegerField(default='1', null=True)
    familles = models.ForeignKey(Famille, related_name='products',on_delete=models.SET_NULL, blank=True, null=True)
    laboratoires = models.ForeignKey(Laboratoire,related_name='products', on_delete=models.SET_NULL, blank=True, null=True)

    def __unicode__(self):
        return self.designation
