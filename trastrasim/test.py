class test():

    def __init__(self,open,close,high,low):
        self.open=open   
        self.close=close   
        self.high=high 
        self.low=low   


a= [1,2,3,4,5,6]
b= [2,2,3,4,5,6]
c= [3,2,3,4,5,6]
d= [4,2,3,4,5,6]

m= test(a,b,c,d)
strF=''
str= '1,234'
strL= str.split(',')
for i in range(len(strL)):
    strF+= strL[i]
ed= str.replace(',','')
print(str)
print(ed)
print(strF)
print(m.open)