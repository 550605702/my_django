# -----测试需要加载----
import math
import os;
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_my.settings")  # "auto_sale_spider.settings"改为setting文件位置
import django;
django.setup()
# -----测试需要加载----

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from project import funcInterface
# Create your views here.
# def index(request):
#     # -----中间放调用接口获得参数-------
#
#
#     # -----中间放调用接口获得参数-------
#
#     #直接返回一段文字
#     # return HttpResponse('hello word')
#     #返回html地址链接，html存在project包的templates文件夹，系统会自动识别
#     return render(request, "index.html",locals())
def login(request):
    # -----中间放调用接口获得参数-------
    # -----中间放调用接口获得参数-------

    #直接返回一段文字
    # return HttpResponse('hello word')
    #返回html地址链接，html存在project包的templates文件夹，系统会自动识别
    return render(request, "login.html",locals())

def rechecking(request):
    return render(request, "rechecking.html", locals())

#用户登陆实现
def userlogin(request):
    # -----中间放调用接口获得参数-------
    username = request.GET.get('username')
    password = request.GET.get('password')
    status = funcInterface.login(username,password)
    return JsonResponse(status)


#获取验证码
def getVerification(request):
    email = request.GET.get('email')
    status = funcInterface.getValidation(email)
    return JsonResponse(status)

#用户注册
def userregister(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    status = funcInterface.addUser(username,password,email)
    print(status)
    return JsonResponse(status)
    # print(str(username)+'---'+str(password)+'-------'+str(email))

#文本查重
def textRechecking(request):
    content = request.POST.get('content')
    title =request.POST.get('title')
    uid = request.POST.get('uid')
    number = len(content.replace(" ",""))
    number = math.ceil(number/1000)
    # print(number)
    status = funcInterface.updateIntegral(number,uid)
    if(status['statusCode']==200):
        funcInterface.queryText(content,title,uid)
        return JsonResponse(status)
    else:
        return JsonResponse(status)


