from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        # memberID = request.POST["memberID"]
        objective = request.POST["objective"]
        duration = request.POST["duration"]
        targetFV = request.POST["targetFV"]
        startDeposit = request.POST["startDeposit"]
        risk_choices = request.POST["risk_choices"]
        #todo 接收到的會員資料寫進資料庫
        # Member.objects.create(username=username, password=password, useremail=useremail, userbirth=userbirth)

        #將資料轉到select
        return render(request, 'portfolio/select.html',locals())

    title = 'portfilio'
    return render(request,'portfolio/index.html',locals())

def select(request):
    title = 'select'
    return render(request, 'portfolio/select.html',locals())

def result(request):
    title = 'select'
    return render(request, 'portfolio/result.html',locals())

def detail(request):
    title = 'select'
    return render(request, 'portfolio/detail.html',locals())