# -----测试需要加载----
import os;
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_my.settings")  # "auto_sale_spider.settings"改为setting文件位置
import django;
django.setup()
# -----测试需要加载----


from project.models import User,Fulltext,Paragraphtext
def creatText(datas,uid,fulltext):
    try:
        uid = User.objects.get(id=uid)
        fulltext = Fulltext.objects.create(uid=uid,fulltext=fulltext,fullrepeat="99%")
        print(fulltext.id)
        for data in datas:
            Paragraphtext.objects.create(textid=fulltext,paragraph=data['paragraph'],repeat=data['repeat'],link=data['link'])
        return 200
    except Exception as err:
        if str(err) == "User matching query does not exist.":
            print("用户不存在")
            return 401
    pass;



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
    datas = [
        {
            "paragraph":"sadadwqdq",
            "repeat":"98%",
            "link":"链接1",
        },{
            "paragraph": "aaaaaaa",
            "repeat": "92%",
            "link": "链接2",
        }
    ]

    creatText(datas,2,"sdadqwdcvzcas")