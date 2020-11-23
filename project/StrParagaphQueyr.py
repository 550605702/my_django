# import time
# import queue
import random
from concurrent.futures import ThreadPoolExecutor
from project import ParagaphQuery, IPproxy

proxy = IPproxy.proxy()

# 字符串分段多线程查询
def StrParagaph(text):
    # 获取文档对象:
    data = []
    tes = [text[i:i + 48] for i in range(0, len(text), 48)]
    t = ThreadPoolExecutor(max_workers=5)  # 多线程最大设置数量应该为os.cpu_count()的五倍,尽量不要多
    # lst = []
    global proxy
    proxy =IPproxy.proxy()
    for result in t.map(query,tes):
        data.append(result)
    # for para in tes:
    #     th = t.submit(query,para, proxy)#MyThread(query, args=(para, proxy))
    #     lst.append(th)
    # t.shutdown()
    # for i in lst:
    #     data.append(i.result())
    return data

def query(para):
    data = []

    datt = ParagaphQuery.query(para, random.choice(proxy))
    if datt['repeat'] == 401:
        # 再次查询
        return ParagaphQuery.query(para, random.choice(proxy))
    return datt

