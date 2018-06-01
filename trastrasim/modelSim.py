from django.db import connection
from django.shortcuts import render,redirect
from .models import TSMC,FOXC,COMP

# from django.shortcuts import render
class Simulator():

    def __init__(self,open,close,high,low):
        self.open=open   
        self.close=close   
        self.high=high 
        self.low=low   

    def strategy1(self,datas):
        buy= []
        buyP= []
        sell= []
        sellP= []
        ben= []
        index= 0
        costC= 0
        costO= 0
        benefitC= 0
        benefitO= 0
        own= 0
        for data in datas:            
            while index < len(datas):

                if self.close[index] > self.open[index] and self.open[index] > self.close[index-1]:                    
                    if not own:                    
                        buy.append(data.Date)
                        buyP.append(data.ClosingPrice)
                        costC+= float(data.ClosingPrice.replace(',',''))
                        costO+= float(data.OpeningPrice.replace(',',''))
                        own= not own

                elif self.close[index] < self.open[index] and self.open[index] < self.close[index-1]:                              
                    if own:
                        sell.append(data.Date)
                        sellP.append(data.ClosingPrice)    
                        benefitC+= float(data.ClosingPrice.replace(',',''))
                        benefitO+= float(data.OpeningPrice.replace(',',''))
                        own= not own
                        ben.append(round(benefitC-costC,2))
                        
                index+= 1
                break
                
        if own:
            sell.append(data.Date)
            sellP.append(data.ClosingPrice)    
            benefitC+= float(data.ClosingPrice.replace(',',''))
            benefitO+= float(data.OpeningPrice.replace(',',''))
            own= not own
            ben.append(round(benefitC-costC,2))

        netBC= round(benefitC-costC,2)
        netBCP= netBC/costC
        netBO= benefitO-costO
        netBOP= netBO/costO
    
        return netBC,buy,buyP,costC,sell,sellP,ben
        
    def strategy2(self,datas):
        buy= []
        buyP= []
        sell= []
        sellP= []
        ben= []
        index= 0
        costC= 0
        costO= 0
        benefitC= 0
        benefitO= 0
        own= 0
        for data in datas:            
            while index < len(datas):

                if not own:                                        
                    buy.append(data.Date)
                    buyP.append(data.ClosingPrice)
                    cost=  float(data.ClosingPrice.replace(',',''))
                    costC+= float(data.ClosingPrice.replace(',',''))
                    costO+= float(data.OpeningPrice.replace(',',''))
                    own= 1

                elif float(self.close[index]) >= cost:                         
                    sell.append(data.Date)
                    sellP.append(data.ClosingPrice)    
                    benefitC+= float(data.ClosingPrice.replace(',',''))*own
                    benefitO+= float(data.OpeningPrice.replace(',',''))*own
                    own= 0
                    ben.append(round(benefitC-costC,2))
                
                else:
                    buy.append(data.Date)
                    buyP.append(data.ClosingPrice)
                    cost=  float(data.ClosingPrice.replace(',',''))
                    costC+= float(data.ClosingPrice.replace(',',''))
                    costO+= float(data.OpeningPrice.replace(',',''))
                    own+= 1
                
                index+= 1
                break
                
        if own:
            sell.append(data.Date)
            sellP.append(data.ClosingPrice)    
            benefitC+= float(data.ClosingPrice.replace(',',''))
            benefitO+= float(data.OpeningPrice.replace(',',''))
            own= not own
            ben.append(round(benefitC-costC,2))

        netBC= round(benefitC-costC,2)
        netBCP= netBC/costC
        netBO= benefitO-costO
        netBOP= netBO/costO
    
        return netBC,buy,buyP,costC,sell,sellP,ben