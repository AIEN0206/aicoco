# from .modelSim import Simulator
import re


a= [4,5,3,4,5,6]
b= [7,8,5,3,4,8]
c= a > b
d= a < b
print(c)
print(a[c])
print(a[d])
print(b[c])
print(b[d])
c1= ['13,257','12,443,212.0','545,413.0','224.0','95.25','16.00']
c2= ['132,257','124,443,212.0','45,413.0','224.0','195.25','160.00']
c3= ['131,257','125,443,212.0','545,413.0','24.0','905.25','6.00']
c4= ['131,257','132,443,212.0','415,413.0','224.0','5.25','106.00']
d= [4,2,3,4,5,6]
# c1= [float(c1.replace(',','')) if c1.count(',') else float(c1) for c1 in c1]
# c1= filter(str.isdigit(),'c11ds5a6f4')
c1= [c1 for c1 in c1]
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
# print(str)s
# print(ed)
# print(strF)
# print(m.open)
# print(max(a))
# print(max(b))
print(c1)
# print(max(c1))


# # e= Simulator(c1,c2,c3,c4)
# # print(e.K)

# import numpy as np

# from bokeh.layouts import row, widgetbox
# from bokeh.models import CustomJS, Slider
# from bokeh.plotting import figure, output_file, show, ColumnDataSource

# x = np.arange(-5, 5, 0.1)
# y = np.sin(x)

# source = ColumnDataSource(data=dict(x=x, y=y))

# plot = figure(y_range=(-10, 10), plot_width=400, plot_height=400)

# plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

# callback = CustomJS(args=dict(source=source), code="""
#     var data = source.data;
#     var A = amp.value;
#     var k = freq.value;
#     var phi = phase.value;
#     var B = offset.value;
#     x = data['x']
#     y = data['y']
#     for (i = 0; i < x.length; i++) {
#         y[i] = B + A*Math.sin(k*x[i]+phi);
#     }
#     source.change.emit();
# """)
# from bokeh.plotting import figure
# from bokeh.embed import components

# plot = figure()
# plot.circle([1,2], [3,4])

# # script, div = components(plot)
# x=1.28
# ans= x**(1/30)

# ans2= ans**30
# print(ans)
# print(ans2)

#  <td><a class="btn btn-light" href="{% url 'trastrasim:strategychoice' data.CompanyID %}" role="button"><i class="fas fa-arrow-circle-right"></i></a></td>

#          <form class="form-inline">
#               <label for="ticker" class="sr-only">Ticker Number</label>
#               <input type="text" class="form-control" id="ticker" placeholder="Enter here">
#             </div>
#             <button type="submit" class="btn btn-primary mb-2">Search</button>
#           </form> 