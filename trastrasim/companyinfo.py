import csv
from .models import COMP

class Companies():

    def update(self):
        comps= COMP.objects.all()
        with open('tw50.csv','rt') as f:
            CIF= csv.reader(f)
            rn=0
            for row in CIF:
                if not row[0] == 'StockSymbol':
                    if  not comps.filter(CompanyID= row[0]):
                        COMP.objects.create(CompanyID= row[0], CompanyName= row[1])       
                        print(row)
                        rn+=1

