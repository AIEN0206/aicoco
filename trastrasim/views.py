from django.shortcuts import render, redirect
from .models import COMP, STPR
from .modelSim import Simulator
from . import companyinfo
import pyquery, requests, time, re, os, json

# from .models import stocksprice

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
    if request.method =="POST": 
        comps= COMP.objects.all()    

    return render(request, 'trastrasim/comps.html', locals())    


def strategy_choice(request,id):
    title= "StockS"

    comp= COMP.objects.get(CompanyID=id)
    datas= STPR.objects.filter(CompanyID=id)
    
    if request.method =="POST":
        choice= request.POST['StockChoice']
        print(choice)
        net= strategy(choice,id)
        res= net[0]
        buy= net[1]
        buyP= net[2]
        costC= net[3]
        sell= net[4]
        sellP= net[5]
        benefit= net[6]
        netBCR= round(res/costC*100,2)
        # print(netBC)
        return render(request,'trastrasim/strategy.html',locals())
        
        
    return render(request,'trastrasim/strategychoice.html',locals())

def strategy(choice,id):
    title= "Strategy"
    datas= STPR.objects.filter(CompanyID=id)
    if choice == '1':
        net= Simulator([data.OpeningPrice for data in datas],[data.ClosingPrice for data in datas],[data.HighestPrice for data in datas],[data.LowestPrice for data in datas]).strategy1(datas)
    if choice == '2':
        net= Simulator([data.OpeningPrice for data in datas],[data.ClosingPrice for data in datas],[data.HighestPrice for data in datas],[data.LowestPrice for data in datas]).strategy2(datas)

    return net

def stocks_price_update(request):
    comps= COMP.objects.all()
    for comp in comps:
        for month in range(12):
            stockNo= comp.CompanyID
            print(stockNo)
            date= '20180{}01'.format(month+1)
            url= 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={}&stockNo={}'.format(date,stockNo)
            
            response= requests.get(url)
            time.sleep(2)
            print(month+1)

            if response.status_code == 200:
                datas= json.loads(response.text)
                
                print(datas['stat'])
                if datas['stat'] == "OK":

                    dbase= STPR.objects.filter(CompanyID= stockNo, Date= datas['data'][0][0])                    
                    key= datas['data'][0][0]
                    print(key)
                    # dbk= STPR.objects.get(Date=key)
                    # # dbk= datasIndb[0].Date
                    # print(dbase)
                    # print(COMP.objects.get(CompanyID= stockNo).CompanyID)
                    if not dbase:           
                        for row in range(len(datas['data'])):
                                STPR.objects.create(CompanyID= COMP.objects.get(CompanyID= stockNo), Date= datas['data'][row][0],TradingVolume= datas['data'][row][1] ,TurnOverinvalue= datas['data'][row][2],OpeningPrice= datas['data'][row][3],HighestPrice= datas['data'][row][4],LowestPrice= datas['data'][row][5],ClosingPrice= datas['data'][row][6],PriceDifference= datas['data'][row][7],NumberofTransactions= datas['data'][row][8])
                        print('Done')
                else:
                    print("No Data")
                    break
    return redirect('/trastrasim')


def company_info_update(request):    

    a= companyinfo.Companies()
    a.update()        
        
    return redirect('/trastrasim')
    
