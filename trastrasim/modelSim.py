import re
from .models import COMP
from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.embed import file_html
from math import pi
import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.stocks import MSFT
import numpy as np

class Simulator():

    def __init__(self,datas):
        self.datas= datas.filter(Date__icontains= '107/', ClosingPrice__regex= r'[[:digit:]]+')
        self.date= [str(int(date.split('/')[0])+1911)+date.split('/')[1]+date.split('/')[2] for date in self.datas.values_list('Date', flat=True)]
        self.open= [float(re.sub(r'[^\d.]','',open)) for open in self.datas.values_list('OpeningPrice', flat=True)]
        self.close= [float(re.sub(r'[^\d.]','',close)) for close in self.datas.values_list('ClosingPrice', flat=True)]
        self.high= [float(re.sub(r'[^\d.]','',high)) for high in self.datas.values_list('HighestPrice', flat=True)]
        self.low= [float(re.sub(r'[^\d.]','',low)) for low in self.datas.values_list('LowestPrice', flat=True)]
        # self.highn= max(self.high)
        # self.lown= max(self.low)
        # self.K= (self.close[-1] - self.lown ) / (self.highn - self.lown)

    def datetime(self,x):
        return np.array(x, dtype=np.datetime64)

    def showchart(self):    
        df = pd.DataFrame()
        df["date"] = self.date
        df["date"] = pd.to_datetime(df["date"])      
        df["open"] = self.open
        df["close"] = self.close
        df["high"] = self.high
        df["low"] = self.low

        inc = df.close > df.open
        dec = df.open > df.close
        w = 12*60*60*1000 # half day in ms

        TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

        p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title = "Profit vs. time")
        p.xaxis.major_label_orientation = pi/4
        p.grid.grid_line_alpha=0.3

        p.segment(df.date, df.high, df.date, df.low, color="black")
        p.vbar(df.date[inc], w, df.open[inc], df.close[inc], fill_color="#D5E1DD", line_color="black")
        p.vbar(df.date[dec], w, df.open[dec], df.close[dec], fill_color="#F2583E", line_color="black")

        html = file_html(p, CDN, "my plot")
        with open(r'trastrasim\templates\out.html','w') as f:
            f.write(html)

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
        netBC= 0
        for data in self.datas:            
            while index < len(self.datas) and index > 1:

                if self.close[index] > self.open[index] and self.open[index] > self.close[index-1]:                    
                    if not own:                    
                        buy.append(self.date[index])
                        buyP.append(self.close[index])
                        costC+= self.close[index]
                        costO+= self.open[index]
                        own= not own

                elif self.close[index] < self.open[index] and self.open[index] < self.close[index-1]:                              
                    if own:
                        sell.append(self.date[index])
                        sellP.append(self.open[index])    
                        benefitC+= self.close[index]
                        benefitO+= self.open[index]                 
                        netBC= round(benefitC-costC,2)
                        netBCP= netBC/costC
                        own= not own
                        ben.append(round(benefitC-costC,2))
                        
                break
            index+= 1  
                
        netBO= benefitO-costO
        netBOP= netBO/costO

        TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
        p= figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title = "{} Candlestick".format('COMP'))
        p.circle(self.datetime(sell), ben, fill_color="white", size=8)
        p.line(self.datetime(sell) ,ben)
        html = file_html(p, CDN, "my plot")
        with open(r'trastrasim\templates\out.html','w') as f:
            f.write(html)

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

   
    def strategy3(self):
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
            while index < len(self.datas) and index > 2:

                if self.close[index] > self.close[index-1] and self.close[index-1] > self.close[index-2]:                    
                    if not own:                    
                        buy.append(data.Date)
                        buyP.append(self.close[index])
                        costC+= self.close[index]
                        costO+= self.open[index]
                        own= not own

                elif self.close[index] < self.close[index-1] and self.close[index-1] < self.close[index-2]:                         
                    if own:
                        sell.append(data.Date)
                        sellP.append(self.open[index])    
                        benefitC+= self.close[index]
                        benefitO+= self.open[index]                 
                        netBC= round(benefitC-costC,2)
                        netBCP= netBC/costC
                        own= not own
                        ben.append(round(benefitC-costC,2))
                        
                break
            index+= 1
                  
        netBO= benefitO-costO
        netBOP= netBO/costO
    
        return netBC,buy,buyP,costC,sell,sellP,ben
        