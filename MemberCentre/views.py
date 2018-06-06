##########################################################################################################################
##  
##  目前問題:
##      1.  同意條款及政策未實作
##      2.  會員修改資料未驗證(生日、姓名、目前職業、地址、手機號碼)
##      3.  刪除會員資料,應二次確認(管理員、會員)
##  
##  說明文件:  
##      1.index() => 管理員的空間
##      2.index_delete() => 管理員刪除會員
##      3.space() => 會員的空間
##      4.create() => 建立會員帳號
##      5.grade() => 驗證會員信箱
##      6.grade_forget() => 補寄驗證碼
##      7.update() => 會員與管理員更改會員資料
##      8.delete() => 會員刪除帳戶
##      9.login() => 會員與管理員登入
##      10.logout() => 會員與管理員登出
##      11.random_code() => 隨機驗證碼/密碼
##      12.send_email() => 寄送email
##      13.forget() => 忘記密碼
##      14.google_captcha() =>Google機器人api驗證
##
##
##########################################################################################################################


from django.shortcuts import render,redirect
from .models import MemberCentre
from django.http import HttpResponse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings
import datetime
import random
import smtplib
import json
import urllib





#管理員空間
def index(request,account):
    members = MemberCentre.objects.all()
    return render(request,'MemberCentre/index.html',locals())


#管理員刪除帳號
def index_delete(requset,account):
    member = MemberCentre.objects.get(account=str(account))
    member.delete()
    response = HttpResponse("<script>alert('刪除成功');location.href='/MemberCentre/index/aicoco'</script>")
    return response



#會員個人空間
def space(request,account):
    member = MemberCentre.objects.get(account=str(account))
    return render(request,'MemberCentre/space.html',locals())



#創建會員帳號
def create(request): 
    if request.method == "POST":
        #將接收到的值丟進相應變數
        account = request.POST["account"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        birth = request.POST["birth"]
        agree = request.POST["agree"]
        grade = "未驗證會員"
        #調用google_captcha()google回傳user是否為機器人
        gcaptcha = request.POST.get('g-recaptcha-response')
        result = google_captcha(gcaptcha)
        #比對資料庫帳號和email是否重複
        account_filter = MemberCentre.objects.filter(account = account)
        email_filter = MemberCentre.objects.filter(email = email)
        if len(account_filter)>0 : 
            return HttpResponse("<script>alert('帳號已有人使用,請重新輸入');location.href='/MemberCentre/create'</script>")
        elif len(email_filter)>0 :  
            return HttpResponse("<script>alert('email已註冊過,請重新輸入');location.href='/MemberCentre/create'</script>")  
        #驗證密碼是否輸入正確
        elif password != password2 or len(password) < 6 :
            return HttpResponse("<script>alert('密碼不得小於六位數或是比對不符,請重新輸入');location.href='/MemberCentre/create'</script>")
        #生日不得為空值
        elif birth =="":
            return HttpResponse("<script>alert('請選取生日');location.href='/MemberCentre/create'</script>")
        #是否同意條款及政策
        elif agree != "checked" :
            return HttpResponse("<script>alert('請勾選同意條款及政策');location.href='/MemberCentre/create'</script>")
        #判定用戶是否為機器人
        elif result == False :
            return HttpResponse("<script>alert('未通過機器人驗證');location.href='/MemberCentre/create'</script>")
        else :
            #產生亂數驗證碼
            tpassword = random_code()
            whoscall = "驗證碼"
            #執行寄送驗證email
            send_email(tpassword,email,whoscall,account)
            #將資料寫進DB
            MemberCentre.objects.create(account = account, email = email, password = password, birth = birth, grade = grade,vcode = tpassword)
            response = HttpResponse("<script>alert('帳號已新增,驗證碼已寄送信箱,請重新登入後進會員空間驗證');location.href='/MemberCentre/grade'</script>")
            #刪除已登入cookie,讓user重新登入
            response.delete_cookie("account")
            return response 
    return render(request,'MemberCentre/create.html',locals())



#驗證會員信箱
def grade(request) :
    if request.method == "POST":
        #將接收到的值丟進相應變數
        user_email = request.POST["email"]
        user_account = request.POST["account"]
        user_vcode = request.POST["vcode"]
        #filter過濾器比對email和account
        member = MemberCentre.objects.filter(account=user_account,email=user_email)
        if member :
            members = MemberCentre.objects.get(account=str(user_account))
            #比對驗證碼是否相符
            if members.vcode == user_vcode :
                members.grade = "已驗證會員"
                members.save()
                return HttpResponse("<script>alert('信箱驗證成功');location.href='/MemberCentre/login/'</script>")
            else :
                return HttpResponse("<script>alert('驗證失敗,請重新輸入');location.href='/MemberCentre/grade/'</script>")
        else :
            return HttpResponse("<script>alert('帳號或email輸入錯誤,請重新輸入');location.href='/MemberCentre/grade/'</script>")
    return render(request,'MemberCentre/grade.html',locals())



#補寄驗證碼
def grade_forget(request) :
    if request.method == "POST":
        #將接收到的值丟進相應變數
        user_email = request.POST["email"]
        user_account = request.POST["account"]
        member = MemberCentre.objects.filter(account=user_account,email=user_email)
        if member :
            members = MemberCentre.objects.get(account=str(user_account))
            #亂數編碼
            tpassword = random_code()
            #將亂數編碼寫進DB更新舊的驗證碼
            account = members.account
            email = members.email
            members.vcode = tpassword
            members.save()
            whoscall = "驗證碼"  
            #執行寄email密碼的動作
            send_email(tpassword,email,whoscall,account)
            return HttpResponse("<script>alert('新驗證碼已寄出');location.href='/MemberCentre/grade/'</script>")
        else :
            return HttpResponse("<script>alert('帳號或email輸入錯誤,請重新輸入');location.href='/MemberCentre/grade_forget'</script>")
    return render(request,'MemberCentre/grade_forget.html',locals())



#管理員或會員修改個人資料
def update(request,account): 
    if request.method == "POST":
        #將接收到的值丟進相應變數
        # account = request.POST["account"] => 帳號不准修改
        # email = request.POST["email"] =>email 不准修改
        password = request.POST["password"]
        name = request.POST["name"]
        cellphone = request.POST["cellphone"]
        # birth = request.POST["birth"]  => 生日也不准修改
        address = request.POST["address"]
        gender = request.POST["gender"]
        education = request.POST["education"]
        job = request.POST["job"]
        member = MemberCentre.objects.get(account=str(account))
        #驗證用戶修改的資料
        if password =="" or len(password) < 6 :  
            return HttpResponse("<script>alert('密碼不得為空且不得小於6位數');location.href='/MemberCentre/update/{}'</script>".format(account)) 
        else :
            #修改資料庫中的會員資料,並儲存
            # member.account = account
            member.password = password
            # member.email = email
            member.name = name
            member.cellphone = cellphone
            # member.birth = birth
            member.address = address
            member.gender = gender
            member.education = education
            member.job = job
            member.save()
            return HttpResponse("<script>alert('帳號修改成功');location.href='/MemberCentre/space/{}'</script>".format(account))
    member = MemberCentre.objects.get(account=str(account))
    return render(request,'MemberCentre/update.html',locals())



#會員刪除資料
def delete(request,account): 
    member = MemberCentre.objects.get(account=str(account))
    #刪除DB會員資料
    member.delete()
    response = HttpResponse("<script>alert('刪除成功');location.href='/MemberCentre/create'</script>")
    #刪除會員cookie
    response.delete_cookie("account")
    return response



#google機器人驗證
def google_captcha(gcaptcha) :
    url = 'https://www.google.com/recaptcha/api/siteverify'
    values = {'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,'response': gcaptcha}
    data = urllib.parse.urlencode(values).encode()
    req =  urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode())
    atlast = result['success']
    return atlast



#管理員或會員登入
def login(request):  
    if request.method == "POST":
        account = request.POST['account']
        password = request.POST['password']
        rememberme = request.POST['rememberme']
        #調用google_captcha(gcaptcha)回傳user是否為機器人
        gcaptcha = request.POST.get('g-recaptcha-response')
        result = google_captcha(gcaptcha)
        #過濾器方法filter比對輸入帳號和密碼是否相符，並取得資料表中account的欄位值
        member = MemberCentre.objects.filter(account=account,password=password).values("account")
        if member :
            members = MemberCentre.objects.get(account=str(account))
            usergrade = members.grade
        #驗證user是否為機器人和已通過驗證
        if member and (usergrade =="管理員" or usergrade =="已驗證會員") and result == True :
            response = HttpResponse("<script>alert('登入成功');location.href='/'</script>")
            #讓user選擇cookie過期時間
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
        elif member and usergrade =="未驗證會員" :
            response = HttpResponse("<script>alert('帳號未啟用，請先驗證email');location.href='/MemberCentre/login'</script>")
        else:
            response = HttpResponse("<script>alert('帳號密碼輸入錯誤或未通過機器人驗證');location.href='/MemberCentre/login'</script>")
        return response
    return render(request,'MemberCentre/login.html',locals())



#管理員或會員登出
def logout(request): 
    response = HttpResponse("<script>alert('登出成功');location.href='/MemberCentre/login'</script>")
    #刪除cookie
    response.delete_cookie("account")
    return response



#隨機密碼或驗證碼
def random_code() :
    #產生的密碼長度
    codelength = 6
    char = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(char)-1
    string = ''
    for i in range(codelength) :
        string += char[random.randint(0,length)]
    return string



#寄email
def send_email(tpassword,email,whoscall,account) :
    host = "smtp.gmail.com"
    port = 587
    username = "aien.aicoco0206@gmail.com"
    password = "aicoco0206"
    from_email = "AICOCO"
    to_list = ["{}".format(email)]
    # 建立SMTP連線
    email_conn = smtplib.SMTP(host,port)
    # 試試看能否跟Gmail Server溝通
    print(email_conn.ehlo())
    # TTLS安全認證機制
    email_conn.starttls()
    # 登入Gmail
    print(email_conn.login(username,password))
    the_msg = MIMEMultipart("alternative")
    the_msg['Subject'] = "AICOCO 帳號驗證-{}".format(whoscall)
    the_msg["From"] = from_email
    the_msg["To"] = to_list[0]
    html_txt = """\
    <html>
        <head></head>
        <body>
            <p>AICOCO會員---{2}---您好!
                <br>
                <br>
                您的{0} : <b id="01">{1}</b>
                <br>
                <br>
                <br>
                <b>請注意不要複製到空格</b>
                <br>
                <br>
                <br>
                此為系統主動發送信函，請勿直接回覆此封信件。
                <br>
                <br>
                AICOCO-----<a href='http://localhost:8000/'>請點擊回到AICOCO首頁</a>
                <br>
                若您是<b>創建帳號</b>收到此郵件，請登入後至會員空間輸入驗證碼
                <br>
                若您是<b>忘記密碼</b>收到此郵件，請登入後請盡快修改您的密碼
                <br>
                <br>
            </p>
        </body>
    </html>
    """.format(whoscall,tpassword,account)
    part_2 = MIMEText(html_txt, 'html', 'utf-8')
    the_msg.attach(part_2)
    # 檢查信件內容
    print(the_msg.as_string())
    # 發送信件
    email_conn.sendmail(from_email, to_list, the_msg.as_string())
    email_conn.quit()



#建立忘記密碼函數
def forget(request) :
    if request.method == "POST":
        account = request.POST['account']
        email = request.POST['email']
        #過濾器方法filter比對user輸入帳號和email是否相符
        members = MemberCentre.objects.filter(account=account,email=email)
        if members :
            member = MemberCentre.objects.get(account=str(account))
            #亂數編碼
            tpassword = random_code()
            #將亂數編碼寫進DB,當作此用戶的新密碼
            member.password = tpassword
            member.save()
            whoscall = "新密碼"
            #執行寄email密碼的動作
            send_email(tpassword,email,whoscall,account)
            response = HttpResponse("<script>alert('新密碼已寄出');location.href='/MemberCentre/forget'</script>")
        else :
            response = HttpResponse("<script>alert('帳號或email不正確');location.href='/MemberCentre/forget'</script>")
        return response
    return render(request,'MemberCentre/forget.html',locals())