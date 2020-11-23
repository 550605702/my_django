
from project.models import Integral,User
import datetime
def addintegral(integral,uid):
    try:
        date = datetime.date.today()+datetime.timedelta(days=30)
        date = date.strftime("%Y-%m-%d %H:%M:%S")
        us = User.objects.get(id=1)
        Integral.objects.create(uid=us,number=integral,overtime=date)
        status = {
            "statusCode": 200,
        }
        return status
    except Exception as err:
        status = {
            "statusCode": 404,
            "err": err
        }
        return status


def updateIntegral(number,uid):
    date = datetime.datetime.now()
    date = date.strftime("%Y-%m-%d %H:%M:%S")
    # print(date)
    integtal = Integral.objects.filter(overtime__gte=date,uid=uid)
    if integtal:
        numberall = 0;
        for ing in integtal:
            numberall=numberall+ing.number
        if numberall >= number:
            # print("可以查询"+str(numberall)+str(number))
            num = number;
            for ins in integtal:
                if ins.number>=num:
                    ins.number = ins.number-num
                    ins.save(update_fields=['number'])
                    status = {
                        "statusCode": 200,
                    }
                    return status
                    return
                else:
                    num = number-ins.number
                    ins.number = 0
                    ins.save(update_fields=['number'])
        else:
            status = {
                "statusCode": 408,#用户积分不足
            }
            return status
    else:
        status = {
            "statusCode": 408,  # 用户积分不足
        }
        return status

