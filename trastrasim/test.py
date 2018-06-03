# from .modelSim import Simulator
import re


a= [1,2,3,4,5,6]
b= [2,2,3,4,5,'6']
c1= ['13,257','12,443,212.0','545,413.0','224.0','95.25','16.00']
c2= ['132,257','124,443,212.0','45,413.0','224.0','195.25','160.00']
c3= ['131,257','125,443,212.0','545,413.0','24.0','905.25','6.00']
c4= ['131,257','132,443,212.0','415,413.0','224.0','5.25','106.00']
d= [4,2,3,4,5,6]
# c1= [float(c1.replace(',','')) if c1.count(',') else float(c1) for c1 in c1]
# c1= filter(str.isdigit(),'c11ds5a6f4')
c1= [float(re.sub(r'[^\d.]','',c1)) for c1 in c1]
c2= [float(c2.replace(',','')) if c2.count(',') else float(c2) for c2 in c2]
c3= [float(c3.replace(',','')) if c3.count(',') else float(c3) for c3 in c3]
c4= [float(c4.replace(',','')) if c4.count(',') else float(c4) for c4 in c4]
# c= list(map(float,c.replace(',','') if c.count(',') else c))
# m= test(a,b,c,d)
strF=''
str= '1,234'
strL= str.split(',')
for i in range(len(strL)):
    strF+= strL[i]
ed= str.replace(',','')
# print(str)
# print(ed)
# print(strF)
# print(m.open)
# print(max(a))
# print(max(b))
print(c1)
# print(max(c1))


# e= Simulator(c1,c2,c3,c4)
# print(e.K)