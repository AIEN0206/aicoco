import re
from .models import COMP
from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.embed import file_html
from math import pi
import pandas as pd
from bokeh.plotting import figure, show, output_file, ColumnDataSource
from bokeh.sampledata.stocks import MSFT
from bokeh.models import HoverTool
import numpy as np

class Simulator():

    def __init__(self,datas):
        self.datas= datas.filter(Date__icontains= '/', ClosingPrice__regex= r'[[:digit:]]+')
        self.date= [str(int(date.split('/')[0])+1911)+date.split('/')[1]+date.split('/')[2] for date in self.datas.values_list('Date', flat=True)]
        self.open= [float(re.sub(r'[^\d.]','',open)) for open in self.datas.values_list('OpeningPrice', flat=True)]
        self.close= [float(re.sub(r'[^\d.]','',close)) for close in self.datas.values_list('ClosingPrice', flat=True)]
        self.high= [float(re.sub(r'[^\d.]','',high)) for high in self.datas.values_list('HighestPrice', flat=True)]
        self.low= [float(re.sub(r'[^\d.]','',low)) for low in self.datas.values_list('LowestPrice', flat=True)]
        
        # self.ma20= list(pd.Series.rolling(self.close,20).mean())
        # self.ma20= pd.Series.rolling(self.close,20).mean()
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
        # df["ma20"] = self.ma20
        df["ma20"] = df["close"].rolling(20).mean()

        inc = df.close > df.open
        dec = df.open > df.close
        bth = df.close != df.open
        w = 12*60*60*1000 # half day in ms

        source = ColumnDataSource(data={
            'date':  df["date"][inc],
            'dated':  df["date"][dec],
            'open': df["open"][inc],
            'opend': df["open"][dec],
            'close': df["close"][inc],
            'closed': df["close"][dec],
            'high': df["high"][inc],
            'highd': df["high"][dec],
            'low': df["low"][inc],
            'lowd': df["low"][dec],
            'ma20': df["ma20"][inc],
            'ma20d': df["ma20"][dec],
        })

        TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

        p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title = "Profit vs. time")
        p.xaxis.major_label_orientation = pi/4
        p.grid.grid_line_alpha=0.3

        p.segment(df.date, df.high, df.date, df.low, color="black")
        p.line('dated', 'ma20d', source=source, color= 'navy', line_width= 1, legend= '20日平均線')
        p.legend.location = "top_left"
        p.vbar('date', w,'open', 'close', fill_color="#D5E1DD", line_color="black", source=source)
        p.vbar('dated', w, 'opend', 'closed', fill_color="#F2583E", line_color="black", source=source)

        # p.vbar(df.date[inc], w, df.open[inc], df.close[inc], fill_color="#D5E1DD", line_color="black")
        # p.vbar(df.date[dec], w, df.open[dec], df.close[dec], fill_color="#F2583E", line_color="black")

        p.add_tools(HoverTool(
            tooltips=[
                ( 'date',   '@date{%F}'            ),
                ( 'open',  '$@open{%0.2f}' ), # use @{ } for field names with spaces
                ( 'close',  '$@close{%0.2f}' ), # use @{ } for field names with spaces
                ( 'high',  '$@high{%0.2f}' ), # use @{ } for field names with spaces
                ( 'low',  '$@low{%0.2f}' ), # use @{ } for field names with spaces
            ],

            formatters={
                'date'      : 'datetime', # use 'datetime' formatter for 'date' field
                'open' : 'printf',   # use 'printf' formatter for 'adj close' field
                'close' : 'printf',   # use 'printf' formatter for 'adj close' field
                'high' : 'printf',   # use 'printf' formatter for 'adj close' field
                'low' : 'printf',   # use 'printf' formatter for 'adj close' field
                                        # use default 'numeral' formatter for other fields
            },
        # display a tooltip whenever the cursor is vertically in line with a glyph
        mode='vline'))


        html = file_html(p, CDN, "my plot")
        with open(r'trastrasim\templates\out.html','w') as f:
            f.write(html)

    def strategy1(self):
        cont= []
        netBC= []
        buy= []
        buyP= []
        sell= []
        sellP= []
        ben= []
        benS= []
        index= 0
        costC= 0
        costO= 0
        benefitC= 0
        benefitO= 0
        own= 0
        netBC= 0
        for data in self.datas:            
            while index < len(self.datas) and index >= 1:

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
                        netBC+= round(benefitC-costC,2)
                        netBCP= netBC/costC
                        own= not own
                        ben.append(round(benefitC-costC,2))
                        benS.append(round(sum(ben),2))
                
                cont.append(index)        
                break
            index+= 1
                
        netBO= benefitO-costO
        netBOP= netBO/costO

        source = ColumnDataSource(data={
            'date': pd.to_datetime(sell),
            'profit': ben,
        })

        TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
        hover= HoverTool(
            tooltips=[
                ( 'date',   '@date{%F}'            ),
                ( 'profit',  '$@profit{%0.2f}' ), # use @{ } for field names with spaces
            ],

            formatters={
                'date'      : 'datetime', # use 'datetime' formatter for 'date' field
                'profit' : 'printf',   # use 'printf' formatter for 'adj close' field
                                        # use default 'numeral' formatter for other fields
            },
        # display a tooltip whenever the cursor is vertically in line with a glyph
        mode='vline')
        p= figure(x_axis_type="datetime", tools=[hover], plot_width=1000, plot_height=300, title = "{} Candlestick".format('COMP'))
        p.xaxis.major_label_orientation = pi/4
        p.grid.grid_line_alpha=0.3
        # p.segment(sell, color="black")
        p.circle('date', 'profit', fill_color="white", size=8, source=source)
        p.line('date', 'profit', line_width= 2, color='navy', alpha=0.5, source=source)

        # line(x,y, color="#0000FF", tools="pan,wheel_zoom,box_zoom,reset",name="line_example", plot_width=800, plot_height=300)
        html = file_html(p, CDN, "my plot")
        with open(r'trastrasim\templates\out.html','w') as f:
            f.write(html)

        return netBC,buy,buyP,costC,sell,sellP,ben,benS,cont
        
    def strategy2(self):
        cont= [1]
        netBC= []
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
                    buy.append(self.date[index])
                    buyP.append(self.close[index])
                    cost0=  self.close[index]
                    costC+= self.close[index]
                    costO+= self.open[index]
                    own= 1

                elif self.close[index] >= cost0:                         
                    sell.append(self.date[index])
                    sellP.append(self.close[index])    
                    benefitC+= self.close[index]*own
                    benefitO+= self.open[index]*own
                    netBC+= round(benefitC-costC,2)      
                    netBCP= netBC/costC                                  
                    own= 0
                    benS.append(round(sum(ben),2))                    
                
                else:
                    buy.append(self.date[index])
                    buyP.append(self.close[index])
                    costC+= self.close[index]
                    costO+= self.open[index]
                    own+= 1
                
                index+= 1
                break

        netBO= benefitO-costO
        netBOP= netBO/costO

        TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
        p= figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, plot_height=300, title = "{} Candlestick".format('COMP'))
        p.circle(self.datetime(sell), ben, fill_color="white", size=8)
        p.line(self.datetime(sell), ben, line_width= 2, color='navy', alpha=0.5)
        # line(x,y, color="#0000FF", tools="pan,wheel_zoom,box_zoom,reset",name="line_example", plot_width=800, plot_height=300)
        html = file_html(p, CDN, "my plot")
        with open(r'trastrasim\templates\out.html','w') as f:
            f.write(html)
    
        return netBC,buy,buyP,costC,sell,sellP,ben,benS,cont

   
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
        