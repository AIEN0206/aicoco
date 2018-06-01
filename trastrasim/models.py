# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class COMP(models.Model):
    CompanyID = models.IntegerField(db_column='CompanyID', primary_key=True)      
    CompanyName = models.CharField(db_column='CompanyName', max_length=20)     
    Abbreviation = models.CharField(db_column='Abbreviation', max_length=10, blank=True, null=True)
       
    class Meta:
        db_table = "COMP"
        # managed= True

class STPR(models.Model):
    CompanyID = models.ForeignKey(COMP, models.DO_NOTHING, db_column='CompanyID', primary_key=True)  # Field name made lowercase.
    Date = models.CharField(db_column='Date', max_length=20)  # Field name made lowercase.
    TradingVolume = models.CharField(db_column='TradingVolume', max_length=20)  # Field name made lowercase.
    TurnOverinvalue = models.CharField(db_column='TurnOverinvalue', max_length=20)  # Field name made lowercase.
    OpeningPrice = models.CharField(db_column='OpeningPrice', max_length=20)  # Field name made lowercase.
    HighestPrice = models.CharField(db_column='HighestPrice', max_length=20)  # Field name made lowercase.
    LowestPrice = models.CharField(db_column='LowestPrice', max_length=20)  # Field name made lowercase.
    ClosingPrice = models.CharField(db_column='ClosingPrice', max_length=20)  # Field name made lowercase.
    PriceDifference = models.CharField(db_column='PriceDifference', max_length=20)  # Field name made lowercase.
    NumberofTransactions = models.CharField(db_column='NumberofTransactions', max_length=20)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'stocksprices'
        unique_together = (('CompanyID', 'Date'),)

class TSMC(models.Model):
    Date = models.CharField(max_length=20, primary_key=True)
    TradingVolume = models.CharField(max_length=20)
    TurnOverinvalue = models.CharField(max_length=20)
    OpeningPrice = models.CharField(max_length=20)
    HighestPrice = models.CharField(max_length=20)
    LowestPrice = models.CharField(max_length=20)
    ClosingPrice = models.CharField(max_length=20)
    PriceDifference = models.CharField(max_length=20)
    NumberofTransactions = models.CharField(max_length=20)
    
    class Meta:
        db_table = "TSMC"
        # managed= True

class FOXC(models.Model):
    Date = models.CharField(max_length=20, primary_key=True)
    TradingVolume = models.CharField(max_length=20)
    TurnOverinvalue = models.CharField(max_length=20)
    OpeningPrice = models.CharField(max_length=20)
    HighestPrice = models.CharField(max_length=20)
    LowestPrice = models.CharField(max_length=20)
    ClosingPrice = models.CharField(max_length=20)
    PriceDifference = models.CharField(max_length=20)
    NumberofTransactions = models.CharField(max_length=20)
       
    class Meta:
        db_table = "FOXC"
        # managed= True
    

# "Date","TradingVolume","TurnOverinvalue","OpeningPrice","Highestprice","Lowestprice","Closingprice","Pricedifference","NumberofTransactions",

