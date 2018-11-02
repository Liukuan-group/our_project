import re

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.core.mail import send_mail

from utils import all_show
from clubShop import settings
from goods.models import Category
from show.models import article
from user.models import User,Address
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired

#发送激活邮件，包含激活链接: http://127.0.0.1:8000/user/active/3
# 激活链接中需要包含用户的身份信息, 并且要把身份信息进行加密
# 加密用户的身份信息，生成激活token 设置30天的过期时间
from utils import cart


def sendEmail(user,email,username):
    serializer = Serializer(settings.SECRET_KEY, 30*24*3600)
    info  = {'confirm': user.id}
    token = serializer.dumps(info)
    # 生成的是字节格式，解码成字符串
    token = token.decode()
    # 调用发送邮件函数
    subject  = '注册账户激活链接'
    message     = ''
    sender   = settings.EMAIL_FROM
    receiver = [email]
    html_message  = '<h1>%s,欢迎您成为我们的注册会员!</h1>请点击下面的链接激活您的账户<br/><a href="http://10.35.165.28:8000/user/active/%s">http://10.35.165.28:8000/user/active/%s</a>' % (username, token, token)
    send_mail(subject,message,sender,receiver,html_message=html_message)
    return redirect('/user/login/')
#/user/register
class RegisterView(View):

    def get(self,request):
        #注册
        cates, essaies, all_class = all_show.all_show1(request)
        return render(request,'register.html', locals())
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        email = request.POST.get('email')
        #注册处理
        #验证数据完整性
        if not all([username,password,repassword,email]):
            return render(request,'register.html',{'errormsg': '信息填写不完善'})
        #验证用户名长度
        if len(username)< 6:
            return render(request,'register.html',{'errormsg': '用户名长度不足6位'})
        # 验证密码长度
        if len(password) < 8:
            return render(request, 'register.html', {'errormsg': '密码长度不足8位'})
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
        user.is_active = 0
        user.save()
        sendEmail(user,email,username)
        return redirect('/')
class ActiveView(View):
    def get(self, request, token):
        '''进行用户激活'''
        # 进行解密，获取要激活的用户信息
        serializer = Serializer(settings.SECRET_KEY, 30*24*3600)
        try:
            # 解密之后得到的info是一个字典
            info = serializer.loads(token)
            user_id = info.get('confirm')
            # 根据user_id找到当前用户
            user = User.objects.get(id=user_id)
            # 将用户状态改为0，激活用户
            user.is_active = 1
            user.save()
            # 激活成功之后跳转登录页面
            # return redirect(reverse('user:login'))
            return HttpResponse('账户激活成功，可以去登录啦！！！')
        except SignatureExpired as e:
            return HttpResponse('激活链接已过期')

#/user/login
class LoginView(View):

    def get(self,request):
        cates, essaies, all_class = all_show.all_show1(request)
        return render(request,'login.html', locals())
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        print(password)
        #验证登录页面信息是否完整
        if not all([username,password]):
            return render(request,'login.html',{'errormsg':'信息不完整'})
        # 验证用户状态是否已经激活
        user1 = User.objects.filter(username=username).first()
        if user1 and user1.is_active == 0:
            return render(request, 'login.html', {'errormsg': '用户还未激活，先去邮箱激活它吧'})
        #获取填写内容的用户
        # user = User.objects.filter(username=username,password=password).first()
        user = authenticate(username=username, password=password)
        #验证获取的用户是否存在
        if user is not None:
            login(request,user)
            request.session['user_login'] = username

            request.session['cart_cnt'] = cart.count_cart(user.id)
            return redirect('/')
        else:
            return render(request, 'login.html', {'errormsg': '用户名或密码错误'})

#/user/logout
def log_out(request):
    #退出登录
    request.session.clear()
    logout(request)

    return redirect('/')

'''收货地址功能'''
#/user/address
def showaddress(request,name):
    cates, essaies, all_class = all_show.all_show1(request)
    #展示收货地址
    user = User.objects.get(username=name)
    address_list = Address.objects.filter(user_id=user.id)
    return render(request, 'addrshow.html', locals())

#/user/add
class AddressView(View):
    #添加收货地址
    def get(self,request,name):
        cates, essaies, all_class = all_show.all_show1(request)
        return render(request,'address.html',locals())
    def post(self,request,name):
        receiver = request.POST.get('receiver')
        addr = request.POST.get('addr')
        code = request.POST.get('code')
        phone = request.POST.get('phone')
        if not all([receiver, addr, phone]):
            return render(request, 'address.html', {'errormsg': '数据不完整'})
            # 校验手机号
        if not re.match(r'^1[3-8]\d{9}$', phone):
            return render(request, 'address.html', {'errormsg': '手机格式不正确'})
        user = User.objects.get(username=name)
        Address.objects.create(receiver=receiver,addr=addr,code=code,phone=phone,user=user)
        return redirect('/user/address/'+name+'/')

#/user/update/<id>  修改收货地址
class UpdateView(View):
    def get(self,request,name,aid):
        cates, essaies, all_class = all_show.all_show1(request)
        #点击修改，根据点击的地址id获取当前地址
        address = Address.objects.get(id=aid)
        return render(request,'updateaddress.html',locals())
    def post(self,request,name,aid):
        address = Address.objects.get(id=aid)
        #获取修改之后的表单数据给获取到的address每个属性重新赋值
        receiver = request.POST['receiver']
        addr = request.POST['addr']
        code = request.POST['code']
        phone = request.POST['phone']
        address.receiver = receiver
        address.addr = addr
        address.code = code
        address.phone = phone
        address.save()
        return redirect('/user/address/'+ name +'/')

def delete(request,name,aid):
    Address.objects.get(id=aid).delete()
    return redirect('/user/address/'+ name +'/')