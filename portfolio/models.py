from django.db import models

# Create your models here.
class MemberCentre(models.Model):
    account = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    cellphone = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    birth = models.DateField()
    address = models.CharField(max_length=45, blank=True, null=True)
    gender = models.CharField(max_length=45, blank=True, null=True)
    education = models.CharField(max_length=45, blank=True, null=True)
    job = models.CharField(max_length=45, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'MemberCentre'

#----------------portfolio models -----------------

class portfolio(models.Model):
    memberId = models.ForeignKey('membercentre',
    on_delete=models.CASCADE)
    objective_choices = (('retire','retire'),
                ('education','education'),
                ('house','house'),
                ('travel','travel'),
                ('wedding','wedding'),
                ('other','other'))
    objective = models.CharField(max_length=10,choices=objective_choices)
    duration = models.IntegerField()
    targetFV = models.IntegerField()
    risk_choices = (('low','low'),
            ('med','medium'),
            ('high','high'))
    risk = models.CharField(max_length=4,choices=risk_choices)
    startDeposit = models.IntegerField()
    monthlyDeposit = models.IntegerField()
    usStock = models.CharField(max_length=10)
    usStockPct = models.DecimalField(max_digits=6, decimal_places=2)
    worldStock = models.CharField(max_length=10)
    worldStockPct = models.DecimalField(max_digits=6, decimal_places=2)
    emerStock = models.CharField(max_length=10)
    emerStockPct = models.DecimalField(max_digits=6, decimal_places=2)
    sectorStock = models.CharField(max_length=10)
    sectorStockPct = models.DecimalField(max_digits=6, decimal_places=2)
    usBond = models.CharField(max_length=10)
    usBondPct = models.DecimalField(max_digits=6, decimal_places=2)
    worldBond = models.CharField(max_length=10)
    worldBondPct = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        db_table = "portfolio"


class etfs(models.Model):
    Ticker = models.CharField(max_length=8)
    etfName = models.CharField(max_length=30)
    category_choices = (('usStock','usStock'),
                ('worldStock','worldStock'),
                ('emerStock','emerStock'),
                ('sectorStock','sectorStock'),
                ('usBond','usBond'),
                ('worldBond','worldBond'))
    category = models.CharField(max_length=8,choices=category_choices)
    expenseRatio = models.DecimalField(max_digits=6, decimal_places=2)
    YTDreturn =  models.DecimalField(max_digits=6, decimal_places=2)
    yrReturn1 = models.DecimalField(max_digits=6, decimal_places=2)
    yrReturn3 = models.DecimalField(max_digits=6, decimal_places=2)
    yrReturn5 = models.DecimalField(max_digits=6, decimal_places=2)
    StdDev = models.DecimalField(max_digits=6, decimal_places=2)
    SharpeRatio = models.DecimalField(max_digits=6, decimal_places=2)
    class Meta:
        db_table = "etfs"

class etfPrices(models.Model):
    Ticker = models.ForeignKey('etfs',
    on_delete=models.CASCADE)
    date = models.DateField()
    opend = models.DecimalField(max_digits=6, decimal_places=2)
    close = models.DecimalField(max_digits=6, decimal_places=2)
    high = models.DecimalField(max_digits=6, decimal_places=2)
    low = models.DecimalField(max_digits=6, decimal_places=2)
    Volume = models.IntegerField()
    class Meta:
        db_table = "etfPrices"


