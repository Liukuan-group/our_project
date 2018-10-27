import re

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.urlresolvers import reverse

from celery_tasks.tasks import send_register_active_email
from clubShop import settings
from user.models import User
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# from itsdangerous import SignatureExpired

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
        user = User.objects.create_user(username=username,email=email,password=password)
        #将用户的初始状态设置为0,未激活状态
        # user.is_active = 0
        user.save()
        return redirect('/user/login/')
        # 发送激活邮件，包含激活链接: http://127.0.0.1:8000/user/active/3
        # 激活链接中需要包含用户的身份信息, 并且要把身份信息进行加密

        # 加密用户的身份信息，生成激活token 设置一小时的过期时间
    #     serializer = Serializer(settings.SECRET_KEY, 3600)
    #     info = {'confirm': user.id}
    #     token = serializer.dumps(info)
    #     # 生成的是字节格式，解码成字符串
    #     token = token.decode()
    #     # 调用发送邮件函数
    #     send_register_active_email(email, username, token)
    #
    #     return redirect(reverse('user:index'))
    #
    # class ActiveView(View):
    #     def get(self, request, token):
    #         '''进行用户激活'''
    #         # 进行解密，获取要激活的用户信息
    #         serializer = Serializer(settings.SECRET_KEY, 3600)
    #         try:
    #             # 解密之后得到的info是一个字典
    #             info = serializer.loads(token)
    #             user_id = info.get('confirm')
    #             # 根据user_id找到当前用户
    #             user = User.objects.get(id=user_id)
    #             # 将用户状态改为1，激活用户
    #             user.is_active = 1
    #             user.save()
    #             # 激活成功之后跳转登录页面
    #             return redirect(reverse('user:login'))
    #         except SignatureExpired as e:
    #             return HttpResponse('Activation link has expired')

class LoginView(View):
    def get(self,request):
        print('222222222222222222')
        return render(request,'login.html')
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        print(password)
        #验证登录页面信息是否完整
        if not all([username,password]):
            return render(request,'login.html',{'errormsg':'信息不完整'})
        #获取填写内容的用户
        # user = User.objects.filter(username=username,password=password).first()
        user = authenticate(username=username, password=password)
        print(user)
        #验证获取的用户是否存在
        if user is not None:
            #验证用户状态是否已经激活
            # if user.is_active == 1:
            return redirect('/')
            # return render(request, 'login.html', {'errormsg': '用户未激活'})
        return render(request, 'login.html', {'errormsg': '用户名或密码错误'})

