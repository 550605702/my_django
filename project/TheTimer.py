#定时器

import datetime
import threading
from project import cleaning
#定时一天执行一次，86400秒为一天
def func():
    # print("haha")
    cleaning.cleaning()
    # 如果需要一天循环调用，就要添加以下方法timer(秒，执行方法。)
    timer = threading.Timer(86400, func)
    timer.start()

def timefunc():

    # 获取现在时间
    now_time = datetime.datetime.now()
    # 获取明天时间
    next_time = now_time + datetime.timedelta(days=+1)
    next_year = next_time.date().year
    next_month = next_time.date().month
    next_day = next_time.date().day
    # 获取明天3点时间
    next_time = datetime.datetime.strptime(str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " 03:00:00",
                                       "%Y-%m-%d %H:%M:%S")
    # # 获取昨天时间
    # last_time = now_time + datetime.timedelta(days=-1)

    # 获取距离明天3点时间，单位为秒
    timer_start_time = (next_time - now_time).total_seconds()
    # 54186.75975

    print("1111")
    # 定时器,参数为(多少时间后执行，单位为秒，执行的方法)在此次的意思是，在明天3点是执行func方法,然后进入func方法，每一天执行一次
    timer = threading.Timer(timer_start_time, func)
    timer.start()

