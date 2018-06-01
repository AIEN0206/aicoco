# ########################################################################################################################
##  
##  1.  管理員刪除帳號,沒辦法自動導向回管理員介面,目前導向首頁
##  2.  修改資料未驗證(update)
##  3.  刪除會員資料,應二次確認(管理員、會員)
##  4.  會員空間底部空間導入圖表
##  5.  會員空間頭像上傳問題
##  6.  同意條款及政策未實作
##  7.  上次登入時間未實作
##  8.  上次登入ip未實作
##  9.  創建此帳號ip未實作
##  10. 創建此帳號時間未實作
##
##########################################################################################################################

from django.shortcuts import render,redirect
from .models import MemberCentre
from django.http import HttpResponse
import datetime

#建立查詢方法 => data輸出所有user資料 => 回傳
#限定管理者帳號才可以查詢
def index(request,account):#管理員空間
    #從DB讀取整張table的data存進members變數
    members = MemberCentre.objects.all()
    #local()方法會將變數傳進呼叫index方法的html
    return render(request,'MemberCentre/index.html',locals())



def index_delete(requset,account):#管理員刪除帳號的方法
    member = MemberCentre.objects.get(account=str(account))
    #刪除DB會員資料
    member.delete()
    return HttpResponse("<script>alert('刪除會員成功');location.href='/'</script>")



#建立查詢方法 => 驗證user資料 => data輸出該user資料 => 回傳
def space(request,account):#個人空間
    #從資料庫以account做索引抓取資料丟進相應變數回傳至使用者空間
    member = MemberCentre.objects.get(account=str(account))
    return render(request,'MemberCentre/space.html',locals())



#建立創建方法 => 接收user輸入資料 => 驗證user輸入資料 => data輸入資料 => 網址轉向
def create(request): #創建會員帳號  
    #如果有接收到user輸入的值時.......
    if request.method == "POST":
        #將接收到的值丟進相應變數
        account = request.POST["account"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        birth = request.POST["birth"]
        agree = request.POST["agree"]
        #比對資料庫帳號密碼是否重複
        account_filter=MemberCentre.objects.filter(account=account)
        email_filter=MemberCentre.objects.filter(email=email)
        #驗證帳號資料庫是否重複
        if len(account_filter)>0 :  
            return HttpResponse("<script>alert('帳號已有人使用,請重新輸入');location.href='/MemberCentre/create'</script>")
        #驗證email資料庫是否重複
        elif len(email_filter)>0 :  
            return HttpResponse("<script>alert('email已註冊過,請重新輸入');location.href='/MemberCentre/create'</script>")  
        #驗證密碼是否輸入正確
        elif password != password2 :
            return HttpResponse("<script>alert('密碼比對不符,請重新輸入');location.href='/MemberCentre/create'</script>")
        elif birth =="":
            return HttpResponse("<script>alert('請選取生日');location.href='/MemberCentre/create'</script>")
        #判定是否同意條款及政策
        elif agree != "checked" :
            return HttpResponse("<script>alert('請勾選同意條款及政策');location.href='/MemberCentre/create'</script>")
        else :       
            MemberCentre.objects.create(account=account,email=email,password=password,birth=birth)
            response = HttpResponse("<script>alert('帳號新增成功,請重新登入');location.href='/'</script>")
            #刪除已登入cookie,讓user重新登入
            response.delete_cookie("account")
            return response
        
    return render(request,'MemberCentre/create.html',locals())



#建立更新方法 => 從資料庫拉資料出來顯示在更改頁面 =>接收user修改的資料 => 修改資料庫資料 =>轉換頁面到管理介面
def update(request,account): #修改會員資料
    if request.method == "POST":
        #將接收到的值丟進相應變數
        # account = request.POST["account"] => 帳號不准修改
        email = request.POST["email"]
        password = request.POST["password"]
        name = request.POST["name"]
        cellphone = request.POST["cellphone"]
        # birth = request.POST["birth"]  => 生日也不准修改
        address = request.POST["address"]
        gender = request.POST["gender"]
        education = request.POST["education"]
        job = request.POST["job"]
        member = MemberCentre.objects.get(account=str(account))
        #修改資料庫中的會員資料,並儲存
        # member.account = account
        member.password = password
        member.email = email
        member.name = name
        member.cellphone = cellphone
        # member.birth = birth
        member.address = address
        member.gender = gender
        member.education = education
        member.job = job
        member.save()
        #修改完成轉回首頁
        return HttpResponse("<script>alert('帳號修改成功');location.href='/'</script>")

    member = MemberCentre.objects.get(account=str(account))
    return render(request,'MemberCentre/update.html',locals())



#建立刪除方法 => 接收user請求參數account => 比對資料庫account => 作為索引執行delete()方法
def delete(request,account): #刪除會員資料
    member = MemberCentre.objects.get(account=str(account))
    #刪除DB會員資料
    member.delete()
    #導向創建帳號
    response = HttpResponse("<script>alert('刪除成功');location.href='/MemberCentre/create'</script>")
    #刪除會員cookie
    response.delete_cookie("account")
    return response



#建立登入方法 =>判斷request.method是否符合POST傳輸 =>與資料庫比對帳號密碼是否輸入正確 => 比對是否有選擇登入時間
def login(request):  #登入會員資料
    if request.method == "POST":
        account = request.POST['account']
        password = request.POST['password']
        rememberme = request.POST['rememberme']
        #利用過濾器方法filter比對data資料與使用者輸入資料是否相符，並取資料表中username的欄位的值(用來顯示在user登入後頁面)
        member = MemberCentre.objects.filter(account=account,password=password).values("account")
        #過濾器方法filter比對成功後.....
        if member :
            #直接回傳user,並使用HttpResponse方法(可加入html.css.js語法)
            response = HttpResponse("<script>alert('登入成功');location.href='/'</script>")
            #導入時區package,並使用方法now()取得現在時間,再使用timedelta加上所需天數
            onehour = datetime.datetime.now()+datetime.timedelta(seconds=60)
            onedate = datetime.datetime.now()+datetime.timedelta(days=1)
            oneweek = datetime.datetime.now()+datetime.timedelta(days=7)
            onemonth = datetime.datetime.now()+datetime.timedelta(days=30)
            if rememberme == 'nostore' :
                response.set_cookie("account",member[0]["account"])
            elif rememberme == 'onehour' :
                response.set_cookie("account",member[0]["account"],expires=onehour)
            elif rememberme == 'onedate' :
                response.set_cookie("account",member[0]["account"],expires=onedate)
            elif rememberme == 'oneweek' :
                response.set_cookie("account",member[0]["account"],expires=oneweek)
            elif rememberme == 'onemonth' :
                response.set_cookie("account",member[0]["account"],expires=onemonth)
        else:
            #如果過濾器方法filter比對失敗(帳密輸入錯誤),回傳....
            response = HttpResponse("<script>alert('登入失敗');location.href='/MemberCentre/login'</script>")
        return response    
    return render(request,'MemberCentre/login.html',locals())



#建立登出方法 => alert登出成功 => 轉向login頁面 =>刪掉登入key值
def logout(request): #登出會員資料
    # 回傳user....
    response = HttpResponse("<script>alert('登出成功');location.href='/MemberCentre/login'</script>")
    #執行刪除cookie方法
    response.delete_cookie("account")

    return response
