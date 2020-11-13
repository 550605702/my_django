
from project.models import User,Fulltext,Paragraphtext

#修改实现
def updateUser(username,password,newpassword):
    user = User.objects.filter(username=username,password=password)
    if user:
        stat = user.update(password=newpassword)
        status = {
            "statusCode": 200,
            "uid":user[0].id
        }
        print(status)
        return status
    else:
        status = {
            "statusCode":402,
        }
        return status
