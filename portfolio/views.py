from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'portfilio'
    return render(request,'portfolio/index.html',locals())

def select(request):
    title = 'select'
    return render(request, 'portfolio/select.html',locals())