from django.shortcuts import render, redirect
from .models import etfs, portfolio
from django.db import connection
from django.http import HttpResponse
from . import calculate

# Create your views here.
def index(request):
        # return redirect("portfolio/select/")
    return render(request,'portfolio/index.html',locals())



def select(request):
    #     # memberID = request.POST["memberID"]
    objective = request.POST["objective"]
    duration = int(request.POST["duration"])
    targetFV = request.POST["targetFV"]
    startDeposit = request.POST["startDeposit"]
    risk_choices = request.POST["risk_choices"]    

    risk_total = calculate.my_risk(objective, duration, risk_choices)
    usStockPct = calculate.portfolio_weight(risk_total)[0]
    worldStockPct = calculate.portfolio_weight(risk_total)[1]
    emerStockPct = calculate.portfolio_weight(risk_total)[2]
    sectorStockPct = calculate.portfolio_weight(risk_total)[3]
    usBondPct = calculate.portfolio_weight(risk_total)[4]
    worldBondPct = calculate.portfolio_weight(risk_total)[5]
    # print("worldBondPct is {:}".format(worldBondPct))

    usStocks = etfs.objects.filter(category='usStock')   
    worldStocks = etfs.objects.filter(category='worldStock')
    emerStocks = etfs.objects.filter(category='emerStock')
    sectorStocks = etfs.objects.filter(category='sectorStock')
    usBonds = etfs.objects.filter(category='usBond')
    worldBonds = etfs.objects.filter(category='worldBond')
    return render(request, 'portfolio/select.html',locals())

def analyze(request):
    p = portfolio()
    # p.memberId_id = 2
    p.objective = request.POST["objective"]
    p.duration = int(request.POST["duration"])
    p.targetFV = request.POST["targetFV"]
    p.startDeposit = request.POST["startDeposit"]
    p.risk = request.POST["risk_choices"]

    risk_total = calculate.my_risk(p.objective, p.duration, p.risk)
    
    usStockPct = calculate.portfolio_weight(risk_total)[0]
    worldStockPct = calculate.portfolio_weight(risk_total)[1]
    emerStockPct = calculate.portfolio_weight(risk_total)[2]
    sectorStockPct = calculate.portfolio_weight(risk_total)[3]
    usBondPct = calculate.portfolio_weight(risk_total)[4]
    worldBondPct = calculate.portfolio_weight(risk_total)[5]

    if usStockPct !=0:
        p.usStock = request.POST['usStock']
    if worldStockPct !=0:
        p.worldStock = request.POST['worldStock']
    if emerStockPct !=0:
        p.emerStock = request.POST['emerStock']
    if sectorStockPct !=0:
        p.sectorStock = request.POST['sectorStock']
    if usBondPct !=0:
        p.usBond = request.POST['usBond']
    if worldBondPct !=0:
        p.worldBond = request.POST['worldBond']
    print("可以儲存")
    p.save()
    print('已經儲存')
    return redirect('/portfolio/result/')

def result(request):
    # if request.method == 'POST':
    p = portfolio.objects.get(id=1)

    objective = p.objective
    duration = p.duration
    targetFV = p.targetFV
    startDeposit = p.startDeposit
    risk_choices = p.risk
    
    risk_total = calculate.my_risk(objective, duration, risk_choices)

    usStockPct = calculate.portfolio_weight(risk_total)[0]
    worldStockPct = calculate.portfolio_weight(risk_total)[1]
    emerStockPct = calculate.portfolio_weight(risk_total)[2]
    sectorStockPct = calculate.portfolio_weight(risk_total)[3]
    usBondPct = calculate.portfolio_weight(risk_total)[4]
    worldBondPct = calculate.portfolio_weight(risk_total)[5]  
    
    mylist =[]
    if usStockPct !=0:
        # usStock = etfs.objects.get(Ticker=p.usStock)
        mylist.append(p.usStock)
        usS
    if worldStockPct !=0:
        # worldStock = etfs.objects.get(Ticker=p.worldStock)
        mylist.append(p.worldStock)
    if emerStockPct !=0:
        # emerStock = etfs.objects.get(Ticker=p.emerStock)
        mylist.append(p.emerStock)
    if sectorStockPct !=0:
        # sectorStock = etfs.objects.get(Ticker=p.sectorStock)
        mylist.append(p.sectorStock)
    if usBondPct !=0:
        # usBond = etfs.objects.get(Ticker=p.usBond)
        mylist.append(p.usBond)
    if worldBondPct !=0:
        # worldBond = etfs.objects.get(Ticker=p.worldBond)
        mylist.append(p.worldBond)
    
    etfsInPort=[]
    print(mylist)
    for item in mylist:
        etfsInPort.append(etfs.objects.get(Ticker=item))

    print(etfsInPort)
    return render(request, 'portfolio/result.html',locals())

def detail(request):
    Ticker = request.GET["Ticker"]
    etf = etfs.objects.get(Ticker=Ticker)

    return render(request, 'portfolio/detail.html',locals())