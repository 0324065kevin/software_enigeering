from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from Member.forms import RegisterForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login as auth_login
import hashlib

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            authenticated_user = authenticate(username=new_user.username,
                                             password=request.POST['password1'])
            print(authenticated_user)

            return HttpResponseRedirect('/login/')

    context = {'form': form}
    return render(request, 'register.html', context)

def ticketsale(request):
    return render(request, "ticketsales.html", locals())

def index(request):
    if request.user.is_authenticated:
        name = request.user.username
    return render(request,"index.html",locals())

def login(request):
    if request.method == 'POST':   #如果是 <login.html> 按登入鈕傳送
        name = request.POST['inputaccount']   #取得表單傳送的帳號、密碼
        password = request.POST['inputPassword']
        user = auth.authenticate(username=name, password=password) #使用者驗證
        if user is not None:         #若驗證成功，以 auth.login(request,user) 登入
            if user.is_active:
                request.session['id']= name
                auth.login(request,user)
                return HttpResponseRedirect('/index/')  #登入成功產生一個 Session，重導到<index.html>
                message = '登入成功!'
            else:
                message = '帳號尚未啟用!'
        else:
            message = '登入失敗!'
    return render(request,"login.html",locals())  #登入失敗則重導回<login.html>

def logout(request):
    auth.logout(request)  #登出成功清除 Session，重導到<index.html>
    request.session.flush()
    return redirect('/index/')