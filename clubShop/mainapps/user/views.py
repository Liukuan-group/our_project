import re
from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.urlresolvers import reverse
from user.models import User

#/user/register
class RegisterView(View):
    def get(self,request):
        #注册
        return render(request,'register.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        email = request.POST.get('email')
        #注册处理
        #验证数据完整性
        if not all([username,password,repassword,email]):
            return render(request,'register.html',{'errormsg': '信息填写不完善'})
        #验证两次密码的一致性
        if repassword != password:
            return render(request,'register.html',{'errormsg': '两次输入密码不一致'})
        #验证邮箱的有效性
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$',email):
            return render(request,'register.html',{'errormsg': '邮箱格式不正确'})
        #验证用户名是否存在
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        if user:
            return render(request,'register.html',{'errormsg': '用户名已存在'})
        user = User.objects.create_user(username,email,password)
        #将用户的初始状态设置为0,未激活状态
        user.is_active = 0
        user.save()
        return redirect(reverse('user:login'))

class LoginView(View):
    def get(self,request):
        return render(request,'login.html')