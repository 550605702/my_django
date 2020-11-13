from project import  StrParagaphQueyr,Storage,toQuery,toUpdate,EmailValidation
import random
def queryText(text,uid):
    proxy = "";
    # 查询分段
    data = StrParagaphQueyr.ParagaphQuery(text,proxy)
    # 保存到数据库
    return Storage.creatText(data,uid,text)

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