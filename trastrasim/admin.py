from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from .models import TSMC,FOXC,COMP

# Register your models here.

# @admin.register(TSMC)
# class Admin(ImportExportModelAdmin):
#     list_display = ("Date","TradingVolume","TurnOverinvalue","OpeningPrice","Highestprice","Lowestprice","Closingprice","Pricedifference","NumberofTransactions")

# @admin.register(FOXC)
# class Admin(ImportExportModelAdmin):
#     list_display = ("Date","TradingVolume","TurnOverinvalue","OpeningPrice","Highestprice","Lowestprice","Closingprice","Pricedifference","NumberofTransactions")

# @admin.register(COMP)
# class Admin(ImportExportModelAdmin):
#      list_display = ('CompanyID','CompanyName',)