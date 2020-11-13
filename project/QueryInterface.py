from project import QueryImpl

# 查询文本,掉用这个接口需要提供，全文文本字符串形式，和用户id
def queryText(text,uid):
    QueryImpl.queryText(text,uid)
    return 100

# 查询文档
def queryWord(word):
    return 100