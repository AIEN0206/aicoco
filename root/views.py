from django.shortcuts import render

# Create your views here.
def index(request):
    pageTitle = "AICOCO首頁"
    return render(request, "root/index.html", locals())

def empty(request):
    pageTitle = "AICOCO空白頁面"
    return render(request, "root/__empty.html", locals())