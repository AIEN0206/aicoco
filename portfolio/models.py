from django.db import models

#----------------portfolio models -----------------

class portfolio(models.Model):
    # memberId = models.ForeignKey('membercentre', on_delete=models.CASCADE)
    objective = models.CharField(max_length=20)
    duration = models.IntegerField()
    targetFV = models.IntegerField()
    risk = models.CharField(max_length=20)
    startDeposit = models.IntegerField()
    monthlyDeposit = models.IntegerField()
    usStock = models.CharField(max_length=10)
    worldStock = models.CharField(max_length=10)
    emerStock = models.CharField(max_length=10)
    sectorStock = models.CharField(max_length=10)
    usBond = models.CharField(max_length=10)
    worldBond = models.CharField(max_length=10)
    
    class Meta:
        db_table = "portfolio"


class etfs(models.Model):
    Ticker = models.CharField(max_length=8)
    etfName = models.CharField(max_length=200)
    category_choices = (('usStock','usStock'),
                ('worldStock','worldStock'),
                ('emerStock','emerStock'),
                ('sectorStock','sectorStock'),
                ('usBond','usBond'),
                ('worldBond','worldBond'))
    category = models.CharField(max_length=20,choices=category_choices)
    expenseRatio = models.DecimalField(max_digits=6, decimal_places=2)
    YTDreturn =  models.DecimalField(max_digits=6, decimal_places=2)
    yrReturn1 = models.DecimalField(max_digits=6, decimal_places=2)
    yrReturn3 = models.DecimalField(max_digits=6, decimal_places=2)
    yrReturn5 = models.DecimalField(max_digits=6, decimal_places=2)
    StdDev = models.DecimalField(max_digits=6, decimal_places=2)
    SharpeRatio = models.DecimalField(max_digits=6, decimal_places=2)
    class Meta:
        db_table = "etfs"

class etfprices(models.Model):
    ticker = models.ForeignKey('Etfs', models.DO_NOTHING, db_column='ticker', primary_key=True)
    date = models.DateField()
    opend = models.DecimalField(max_digits=6, decimal_places=2)
    high = models.DecimalField(max_digits=6, decimal_places=2)
    low = models.DecimalField(max_digits=6, decimal_places=2)
    close = models.DecimalField(max_digits=6, decimal_places=2)
    volume = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'etfprices'
        unique_together = (('ticker', 'date'),)


