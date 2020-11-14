
# -----测试需要加载----
import os;
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_my.settings")  # "auto_sale_spider.settings"改为setting文件位置
import django;
django.setup()
# -----测试需要加载----
from project.models import Integral,User
import datetime
def addintegral(integral,uid):
    date = datetime.date.today()+datetime.timedelta(days=30)
    date = date.strftime("%Y-%m-%d %H:%M:%S")
    print(date)
    us = User.objects.get(id=1)
    Integral.objects.create(uid=us,number=integral,overtime=date)
    # print(user[0].id)



# def updateIntegral()


if __name__ == '__main__':
    addintegral(30,1)