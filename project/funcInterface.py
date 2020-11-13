from project import funcImpl


# 查询文本,掉用这个接口需要提供，全文文本字符串形式，和用户id
def queryText(text,uid):
    return funcImpl.queryText(text, uid)


#通过uid查询查重记录返回status=200和数据表示成功，401表示用户不存在
def toUidQuery(uid):
    return funcImpl.toQuery(uid)


#登陆，返回状态码200，和uid表示登陆成功,返回402表示用户名和密码不匹配字段为status{"statusCode":200,"uid":uid}
def login(username,password):
    return funcImpl.login(username, password)


#通过旧密码改密码，返回状态码200，表示修改成功，返回状态码402表示用户名密码不匹配
def updateUser(username,password,newpassword):
    return funcImpl.updateUser(username,password,newpassword)


#获取验证码，返回状态码200表示成功，validationCode=验证码，返回403表示邮箱验证失败
def getValidation(email):
    return funcImpl.getValidation(email)

#增加用户返回状态码200表示成功，404 状态码返回用户注册失败，405 状态码返回用户名已存在，406 状态码返回邮箱已存在
def addUser(username,password,email):
    return funcImpl.addUser(username,password,email)

#通过用户名查找用户是否存在
def toNameUser(username):
    return funcImpl.toNameUser(username)

#验证用户名邮箱是否匹配，匹配邮箱发送验证码，并获取。不匹配返回，406状态码邮箱用户名不匹配
def getNameEmaiValidation(username,email):
    return funcImpl.getNameEmaiValidation(username, email)

#忘记密码改密码
def forgotPassword(username,newpassword):
    return funcImpl.forgotPassword(username,newpassword)