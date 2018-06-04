from django.shortcuts import render, redirect
from .models import COMP, STPR
from .modelSim import Simulator
from . import companyinfo
import pyquery, requests, time, re, os, json

# Create your views here.
def index(request):
    title = "StockP"
    if request.method == "POST":
        StockTicker = request.POST['StockTicker']
        comps = COMP.objects.all()
        datas = STPR.objects.all()
        st = comps[int(StockTicker)-1].CompanyID
  
    return render(request, 'trastrasim/index.html', locals())


def company_info(request):
    title = "Company Infomations"
    comps= COMP.objects.all()          

    return render(request, 'trastrasim/comps.html', locals())    


def strategy_choice(request,id):
    title= "StockS"
    comp= COMP.objects.get(CompanyID=id)
    datas= STPR.objects.filter(CompanyID=id)
    Simulator(datas).showchart()
    if request.method =="POST":
        choice= request.POST['StockChoice']
        net= strategy(choice,id)
        res= net[0]
        buy= net[1]
        buyP= net[2]
        costC= net[3]
        sell= net[4]
        sellP= net[5]
        benefit= net[6]
        # scripts= net[7]
        # div= net[8]
        netBCR= round(res/costC*100,2)
        return render(request,'trastrasim/strategy.html',locals())
        
    return render(request,'trastrasim/strategychoice.html',locals())

def strategy(choice,id):
    title= "Strategy"
    datas= STPR.objects.filter(CompanyID=id)
    
    if choice == '1':
        net= Simulator(datas).strategy1()
   
    if choice == '2':
        net= Simulator(datas).strategy2()

    return net

def stocks_price_update(request):
    comps= COMP.objects.all()
    for comp in comps:
        for year in range(2016,2019):
            for month in range(1,13):
                stockNo= comp.CompanyID
                print('stockNo: {}'.format(stockNo))               
                zero= '0' if month < 10 else ''   
                date= '{}{}{}01'.format(year,zero,month)           
                dbase= STPR.objects.filter(CompanyID= stockNo, Date__iregex= r'105/0*{}/[0-9]+'.format(month))  

                if not dbase:  
                    print("Requesting")
                    url= 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={}&stockNo={}'.format(date,stockNo)       
                    response= requests.get(url)
                    time.sleep(3)
                    print('Date: {}'.format(date))
                    if response.status_code == 200:
                        datas= json.loads(response.text)           
                        print(datas['stat'])

                        if datas['stat'] == "OK":  
                            for row in range(len(datas['data'])):
                                    STPR.objects.create(CompanyID= COMP.objects.get(CompanyID= stockNo), Date= datas['data'][row][0],TradingVolume= datas['data'][row][1], TurnOverinvalue= datas['data'][row][2], OpeningPrice= datas['data'][row][3], HighestPrice= datas['data'][row][4], LowestPrice= datas['data'][row][5],ClosingPrice= datas['data'][row][6], PriceDifference= datas['data'][row][7], NumberofTransactions= datas['data'][row][8])
                            print('Done')
                        
                        else:
                            print("No Data")

                else:
                    print("Read already")

    return redirect('/trastrasim')


def company_info_update(request):    
    a= companyinfo.Companies()
    a.update()        
        
    return redirect('/trastrasim')
    
