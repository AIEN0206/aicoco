from django.shortcuts import render,redirect
from .models import Consultant
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):  
    
    title = "投顧老師"

    #todo 讀取顧問資料傳給index.html
    consultants = Consultant.objects.all()
    # print(list(consultants))

    return render(request,'consultant/index.html',locals())

def create(request):
    if request.method == 'POST':
        姓名 = request.POST["姓名"]
        學歷 = request.POST["學歷"]
        經歷 = request.POST["經歷"]
        證照 = request.POST["證照"]

        #todo 接收到的顧問資料寫進資料庫
        Consultant.objects.create(姓名=姓名,學歷=學歷,經歷=經歷,證照=證照)
        
        #todo 新增完成後轉到http://localhost:8000/consultant
        return redirect("/consultant")
       
    title = "會員新增" 
    return render(request,'consultant/create.html',locals())

def update(request,id):
    if request.method == 'POST':        
        姓名 = request.POST["姓名"] 
        學歷 = request.POST["學歷"]      
        經歷 = request.POST["經歷"]
        證照 = request.POST["證照"]

        #todo 修改資料庫中的顧問資料
        consultant = Consultant.objects.get(id=int(id))
        consultant.姓名 = 姓名
        consultant.學歷 = 學歷
        consultant.經歷  = 經歷
        consultant.證照 = 證照
        consultant.save()
        
        #todo 修改完成後轉到http://localhost:8000/consultant
        return redirect('/consultant')

    title = "會員修改"

    #todo 根據會員編號取得會員資料傳給update.html
    consultant = Consultant.objects.get(id=int(id))
    return render(request,'consultant/update.html',locals())

def delete(request,id):
    #todo 根據會員編號刪除會員資料
    consultant = Consultant.objects.get(id=int(id))
    consultant.delete()

    #todo 刪除完成後轉到http://localhost:8000/consultant
    return redirect('/consultant')