from project import funcImpl


# 查询文本,掉用这个接口需要提供，全文文本字符串形式，和用户id
def queryText(text,uid):
    return funcImpl.queryText(text, uid)


#通过uid查询查重记录返回status=200和数据表示成功，401表示用户不存在
def toUidQuery(uid):
    return funcImpl.toQuery(uid)


#返回状态码200，和uid表示登陆成功,返回402表示用户名和密码不匹配字段为status{"statusCode":200,"uid":uid}
def login(username,password):
    return funcImpl.login(username, password)


#返回状态码200，表示修改成功，返回状态码402表示用户名密码不匹配
def updateUser(username,password,newpassword):
    return funcImpl.updateUser(username,password,newpassword)


#返回状态码200表示成功，validationCode=验证码，返回403表示邮箱验证失败
def getValidation(email):
    return funcImpl.getValidation(email)

#返回状态码200表示成功，404 状态码返回用户注册失败，405 状态码返回用户名已存在，406 状态码返回邮箱已存在
def addUser(username,password,email):
    return funcImpl.addUser(username,password,email)