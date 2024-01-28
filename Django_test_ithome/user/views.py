from datetime import datetime
import json
import uuid
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from user.models import UserProfile
from django.contrib import auth     #新增
from django.contrib.sessions.models import Session#新增

@csrf_exempt
def register(request):
    message = {}
    if request.method == "POST": 
        try:
            data = json.loads(bytes.decode(request.body,"utf-8")) 
            account = data["account"]
            password = data["password"]
            email = data["email"]
            phone = data["phone"]
            id = uuid.uuid5(uuid.NAMESPACE_DNS,account)
            check_account = UserProfile.objects.filter(account=account).first()
            if check_account is None :
                user = UserProfile.objects.create_user(id=id,username=account,account=account,email=email,phone=phone)
                user.set_password(password)
                user.save()
                message = {"status" : "註冊成功"}
            else :
                message = {"status" : "註冊失敗，帳號已註冊"}
        except Exception as e:
            message = {"status" : "error"}
    return JsonResponse(message)

@csrf_exempt
def login(request):
    message = {}
    if request.method == "POST":
        data = json.loads(bytes.decode(request.body,"utf-8"))
        try:
            account = data['account']
            password = data['password']
            auth_obj = auth.authenticate(username = account,password = password)#驗證帳號對錯
            if auth_obj is not None:#驗證成功
                if request.user.is_authenticated == False:#驗證是否有帳號登入/新增開始
                    auth_obj.check_password(password)#檢查輸入與驗證返回user對象密碼是否府和
                    request.session.create()
                    auth.login(request,auth_obj)
                    message = {"status":"登入成功"}
                else:
                    message = {"status":"帳號已登入"}
            else:
                message = {"status":"帳號密碼輸入錯誤"}
        except:
            message = {"status":"登入失敗"}

        return JsonResponse(message)

@csrf_exempt
def logout(request):
    message = {}
    try:
        auth.logout(request)
        message = {"status":"登出成功"}
    except:
        message = {"status":"登出失敗"}
    return JsonResponse(message)

