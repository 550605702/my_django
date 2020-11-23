
# -----测试需要加载----
import os;
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_my.settings")  # "auto_sale_spider.settings"改为setting文件位置
import django;
django.setup()
# -----测试需要加载----


from project.models import User,Fulltext,Paragraphtext


#把查询结果存入数据库
def creatText(datas,fulltext):
    try:
        repeat = 0
        for data in datas:
            if(data['repeat']!=401):
                repeat= repeat+len(data['repeat'])
        repeat = repeat / len(datas)
        fulltext.fullrepeat = repeat
        fulltext.save(update_fields=['fullrepeat'])
        # fulltext = fulltext.save().update(fullrepeat=repeat)
        # print(fulltext.id)
        for data in datas:
            Paragraphtext.objects.create(textid=fulltext,paragraph=data['paragraph'],repeat=data['repeat'],link=data['link'])
        status = {
            "statusCode": 200,
        }
        return status
    except Exception as err:
        if str(err) == "User matching query does not exist.":
            print("用户不存在")
            status = {
                "statusCode": 401,
            }
            return status
        print(err)


def addUser(username,password,email):
    try:
        user = User.objects.create(username=username,password=password,email=email)
        status = {
            "statusCode":200,
            "uid":user.id
        }
        return status
    except Exception as err:
        status = {
            "statusCode":404,
            "err":err
        }
        return status



def test():
    # User(username='hulei',password='123456')
    # User.save()
    # 增加用户
    # User.objects.create(username='hulei',password='123456')

    # 查询用户
    # data =  User.objects.get(username='hulei') #一条信息
    # data = User.objects.filter(username='hulei')#多条信息

    # 删除用户
    # User.objects.filter(id=2).delete()
    # print(data.username)
    pass


if __name__ == '__main__':
    # addUser("ming","1231231","asdasd")
    reat = 401
    datas = [
        {
            "paragraph":"sadadwqdq",
            "repeat":reat,
            "link":"链接1",
        },{
            "paragraph": "aaaaaaa",
            "repeat": reat,
            "link": "链接2",
        }
    ]

    repeat = 0
    for data in datas:
        if (data["repeat"] != 401):
            repeat = repeat + int(data["repeat"])
    print(repeat)
    repeat = repeat / len(datas)
    print(repeat)
    # fulltext = Fulltext.objects.create(uid=uid, fulltext=fulltext, fullrepeat=repeat)
    # creatText(datas,2,"sdadqwdcvzcas")