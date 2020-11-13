from project import  StrParagaphQueyr,Storage

def queryText(text,uid):
    proxy = "";
    # 查询分段
    data = StrParagaphQueyr.ParagaphQuery(text,proxy)
    # 保存到数据库
    Storage.creatText(data,uid,text)
    return data

