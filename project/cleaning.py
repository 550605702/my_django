from datetime import datetime, timedelta
from project.models import User,Fulltext,Paragraphtext
#清除所有超过30天的数据
def cleaning():
    nowtime = datetime.now().date()
    cleantime = (nowtime - timedelta(30))
    fulltext = Fulltext.objects.filter(time__lt=cleantime)
    for text in fulltext:
        Paragraphtext.objects.filter(textid=text).delete()
        text.delete()
    print(fulltext)