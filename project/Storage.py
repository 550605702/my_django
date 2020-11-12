
import os;
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_my.settings")  # "auto_sale_spider.settings"改为setting文件位置
import django;
django.setup()

from project.models import User


def storage(data):
    # User(username='hulei',password='123456')
    # User.save()
    #增加用户
    # User.objects.create(username='hulei',password='123456')

    #查询用户
    # data =  User.objects.get(username='hulei') #一条信息
    # data = User.objects.filter(username='hulei')#多条信息

    #删除用户
    # User.objects.filter(id=2).delete()
    # print(data.username)
    pass;

if __name__ == '__main__':
    storage('11')