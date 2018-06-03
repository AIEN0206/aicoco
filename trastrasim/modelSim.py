from .models import COMP
import re

class Simulator():

    def __init__(self,datas):
        self.datas= datas.filter(ClosingPrice__regex= r'[[:digit:]]+')
        self.open= [float(re.sub(r'[^\d.]','',open)) for open in self.datas.values_list('OpeningPrice', flat=True)]
        self.close= [float(re.sub(r'[^\d.]','',close)) for close in self.datas.values_list('ClosingPrice', flat=True)]
        self.high= [float(re.sub(r'[^\d.]','',high)) for high in self.datas.values_list('HighestPrice', flat=True)]
        self.low= [float(re.sub(r'[^\d.]','',low)) for low in self.datas.values_list('LowestPrice', flat=True)]
        self.highn= max(self.high)
        self.lown= max(self.low)
        self.K= (self.close[-1] - self.lown ) / (self.highn - self.lown)

    def strategy1(self):
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
        for data in self.datas:            
            while index < len(self.datas):

                if self.close[index] > self.open[index] and self.open[index] > self.close[index-1]:                    
                    if not own:                    
                        buy.append(data.Date)
                        buyP.append(self.close[index])
                        costC+= self.close[index]
                        costO+= self.open[index]
                        own= not own

                elif self.close[index] < self.open[index] and self.open[index] < self.close[index-1]:                              
                    if own:
                        sell.append(data.Date)
                        sellP.append(self.open[index])    
                        benefitC+= self.close[index]
                        benefitO+= self.open[index]                 
                        netBC= round(benefitC-costC,2)
                        netBCP= netBC/costC
                        own= not own
                        ben.append(round(benefitC-costC,2))
                        
                index+= 1
                break
                
        netBO= benefitO-costO
        netBOP= netBO/costO
    
        return netBC,buy,buyP,costC,sell,sellP,ben
        
    def strategy2(self):
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
        for data in self.datas:            
            while index < len(self.datas):

                if not own:                                        
                    buy.append(data.Date)
                    buyP.append(self.close[index])
                    cost0=  self.close[index]
                    costC+= self.close[index]
                    costO+= self.open[index]
                    own= 1

                elif self.close[index] >= cost0:                         
                    sell.append(data.Date)
                    sellP.append(self.close[index])    
                    benefitC+= self.close[index]*own
                    benefitO+= self.open[index]*own
                    netBC= round(benefitC-costC,2)      
                    netBCP= netBC/costC                                  
                    own= 0
                    ben.append(round(benefitC-costC,2))
                
                else:
                    buy.append(data.Date)
                    buyP.append(self.close[index])
                    costC+= self.close[index]
                    costO+= self.open[index]
                    own+= 1
                
                index+= 1
                break

        netBO= benefitO-costO
        netBOP= netBO/costO
    
        return netBC,buy,buyP,costC,sell,sellP,ben