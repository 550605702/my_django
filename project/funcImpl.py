from project import  StrParagaphQueyr,Storage,toQuery,toUpdate,EmailValidation,IPproxy,integralChange
from project.models import User,Fulltext,Paragraphtext
import random
def queryText(text,title,uid):
    try:
        #把文本先存入数据库，就算查重失败也不会导致乱扣积分，可通过记录得知查重结果
        uid = User.objects.get(id=uid)
        fulltext = Fulltext.objects.create(uid=uid, fulltext=text,title=title,fullrepeat=400)
    except Exception as err:
        status = {
            "statusCode": 409,
            "err": err
        }
        return status
    # 查询分段
    proxy = IPproxy.proxy()
    data = StrParagaphQueyr.StrParagaph(text,proxy)
    # 保存到数据库
    return Storage.creatText(data,fulltext)


def toUidQuery(uid):
    return toQuery.toUidQuery(uid)



def login(username,password):
    return toQuery.login(username,password)


def updateUser(username,password,newpassword):
    return toUpdate.updateUser(username,password,newpassword)


def getValidation(email):
    list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = random.sample(list, 6)
    code = ''.join(code)
    return EmailValidation.getValidation(email,code)

def addUser(username,password,email):
    if toQuery.nameQuery(username):
        status = {
            "statusCode": 405  # 用户名以存在
        }
        return  status
    if toQuery.emailQuery(email):
        status = {
            "statusCode": 406  # 邮箱已注册
        }
        return status
    return Storage.addUser(username,password,email);

def toNameUser(username):
    if toQuery.nameQuery(username=username):
        status = {
            "statusCode": 200
        }
        return status
    else:
        status ={
            "statusCode":405
        }
        return status

def getNameEmaiValidation(username,email):
    if toQuery.nameEmailUser(username,email):
        list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        code = random.sample(list, 6)
        code = ''.join(code)
        return EmailValidation.getValidation(email, code)
    else:
        status = {
            "statusCode": 407#邮箱与用户名不匹配
        }
        return status


def forgotPassword(username,newpassword):
    return toUpdate.forgotPassword(username,newpassword)


def updateIntegral(number,uid):
    return integralChange.updateIntegral(number,uid)