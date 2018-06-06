from django.shortcuts import render, redirect
from .models import etfs, portfolio, etfprices
from django.db import connection
from django.http import HttpResponse
import numpy as np
import pandas as pd
from . import calculate, news_crawler
import MySQLdb as db

# Create your views here.
def index(request):
        # return redirect("portfolio/select/")
    return render(request,'portfolio/index.html',locals())



def select(request): 
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

    usStocks = etfs.objects.filter(category='usStock')   
    worldStocks = etfs.objects.filter(category='worldStock')
    emerStocks = etfs.objects.filter(category='emerStock')
    sectorStocks = etfs.objects.filter(category='sectorStock')
    usBonds = etfs.objects.filter(category='usBond')
    worldBonds = etfs.objects.filter(category='worldBond')
    return render(request, 'portfolio/select.html',locals())

def analyze(request):
    #建立一個portfolio 資料庫物件
    p = portfolio()

    #取得POST來的Portfolio資料
    p.objective = request.POST["objective"]
    p.duration = int(request.POST["duration"])
    p.targetFV = request.POST["targetFV"]
    p.startDeposit = request.POST["startDeposit"]
    p.risk = request.POST["risk_choices"]

    #呼叫計算風險分數的module, 取得投資組合的項目權重
    risk_total = calculate.my_risk(p.objective, p.duration, p.risk)
    usStockPct = calculate.portfolio_weight(risk_total)[0]
    worldStockPct = calculate.portfolio_weight(risk_total)[1]
    emerStockPct = calculate.portfolio_weight(risk_total)[2]
    sectorStockPct = calculate.portfolio_weight(risk_total)[3]
    usBondPct = calculate.portfolio_weight(risk_total)[4]
    worldBondPct = calculate.portfolio_weight(risk_total)[5]

    #如果投資組合權重不是0，則取得POST資料
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
    #存入資料庫
    p.save()
    #取出剛剛存入資料庫portfolio Table的id, 導入result頁
    return redirect('/portfolio/result/?id=%s' % (p.id))

def result(request):
    #取得全部的portfolios顯示在前台
    portfolios = portfolio.objects.all()
    
    #取得此次result要用的Portfolio資料 放入物件p
    pid = int(request.GET['id'])
    p = portfolio.objects.get(id=pid)

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
    portRate = 0

    # 設定連結mySQL
    database = db.connect('localhost','aicoco','aicoco','aicoco') 
    frames = []
    portWeight = []

    if usStockPct !=0:
        mylist.append(p.usStock)
        usStock = etfs.objects.get(ticker=p.usStock)
        portRate += usStock.yrReturn3*usStockPct #計算usStock 3年獲利XPortfoio內的百分比
        df = pd.read_sql('select date,close from etfprices where ticker = "%s"' % p.usStock, con=database)    
        portWeight.append(usStockPct/100) 
        
    if worldStockPct !=0:
        mylist.append(p.worldStock)
        worldStock = etfs.objects.get(ticker=p.worldStock)
        portRate += worldStock.yrReturn3*worldStockPct
        df_worldStock = pd.read_sql('select close from etfprices where ticker = "%s"' % p.worldStock, con=database)
        df = pd.concat([df,df_worldStock], axis=1)
        portWeight.append(worldStockPct/100)

    if emerStockPct !=0:
        mylist.append(p.emerStock)
        emerStock = etfs.objects.get(ticker=p.emerStock)
        portRate += emerStock.yrReturn3*emerStockPct
        df_emerStock = pd.read_sql('select close from etfprices where ticker = "%s"' % p.emerStock, con=database)
        df = pd.concat([df,df_emerStock], axis=1)
        portWeight.append(emerStockPct/100)

    if sectorStockPct !=0:
        mylist.append(p.sectorStock)
        sectorStock = etfs.objects.get(ticker=p.sectorStock)
        portRate += sectorStock.yrReturn3*sectorStockPct
        df_sectorStock = pd.read_sql('select close from etfprices where ticker = "%s"' % p.sectorStock, con=database)
        df = pd.concat([df,df_sectorStock], axis=1)
        portWeight.append(sectorStockPct/100)

    if usBondPct !=0:
        mylist.append(p.usBond)
        usBond = etfs.objects.get(ticker=p.usBond)
        portRate += usBond.yrReturn3*usBondPct
        df_usBond = pd.read_sql('select close from etfprices where ticker = "%s"' % p.usBond, con=database)
        df = pd.concat([df,df_usBond], axis=1)
        portWeight.append(usBondPct/100)

    if worldBondPct !=0:
        mylist.append(p.worldBond)
        worldBond = etfs.objects.get(ticker=p.worldBond)
        portRate += worldBond.yrReturn3*worldBondPct
        df_worldBond = pd.read_sql('select close from etfprices where ticker = "%s"' % p.worldBond, con=database)
        df = pd.concat([df,df_worldBond], axis=1)
        portWeight.append(worldBondPct/100)
    
    portRate = portRate/100
    
    etfsInPort=[]
    for item in mylist:
        etfsInPort.append(etfs.objects.get(ticker=item))


    # Backtest 圖表資料產生
    # 計算Portfolio過去每期的值 (本期-第一期)/第一期*etf百分比
    df = df.set_index("date")
    percent = (df - df.iloc[0])/df.iloc[0]
    percent_weighted = percent * portWeight
    final = percent_weighted.sum(axis=1)
    yrReturn5 = round(final[-1]*100)
    annualRet = round(((final[-1]+1)**(1/5)-1)*100,2)
    # print(final)


    # Portfolio Forecast 圖標資料產生-
    mPayment = calculate.monthlyPay(annualRet, startDeposit, targetFV, duration)
    portNet = startDeposit
    #  計算每期net worth    
    chartdata = [portNet,]
    for t in range(1, duration*12+1):
        portNet = round((portNet+mPayment)*(annualRet/100/12+1))
        chartdata.append(portNet)

    return render(request, 'portfolio/result.html',locals())

def delete(request):
    del_id = request.GET['del_id']
    ret_id = request.GET['ret_id']
    p = portfolio.objects.get(id=del_id)
    p.delete()
    return redirect('/portfolio/result/?id=%s' % (ret_id))

def detail(request):
    ticker = request.GET["ticker"]
    etf = etfs.objects.get(ticker=ticker)
    news = news_crawler.news(ticker)
    print("news: {:}".format(news))
    return render(request, 'portfolio/detail.html',locals())