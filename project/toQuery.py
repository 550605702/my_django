
from project.models import User,Fulltext,Paragraphtext

#通过uid查询用户历史记录
def toUidQuery(uid):
    try:
        user = User.objects.get(id=uid)
        fulltext = Fulltext.objects.filter(uid=user)
        status = {
            "statusCode": 200,
            "fulltext": fulltext
        }
        return status
    except Exception as err:
        if str(err) == "User matching query does not exist.":
            print("用户不存在")
            status = {
                "statusCode": 401,
            }
            return status

#用户登陆
def login(username,password):
    user = User.objects.filter(username=username,password=password)
    if user:#判断是否为空。列表为空是false
        status = {
            "statusCode": 200,
            "uid":user[0].id
        }
        return status
    else:
        #用户名密码未查找到，返回402用户名密码不匹配
        status = {
            "statusCode":402
        }
        return status

#通过用户名查询是否存在用户
def nameQuery(username):
    return User.objects.filter(username=username)

#通过邮箱查询是否存在用户
def emailQuery(email):
    return User.objects.filter(email=email)