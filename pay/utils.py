# -*- coding: utf-8 -*-
import datetime
import os
import random
from alipay import AliPay

private_key_string = '''-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEApNZyqxPGS3xs/p6lpgffgnbvELjReMRz3y2WGhynDeY/vwODsafKy7XDvYPvE6iGXegz4vxtJINOBJprPXqamQvPJq20z/R3CZlCsOEy75Pr77ZRGZbMvzVXGkuavnLQoH40FuRbQYMXt8rLR1GnBS+5Bs5tWNfy94f4x4VroEZ80zVDnQEkzy46fmoi6lZ5r6N/7iXFo0fXdFWlvZJ0EDBF0BdSnHz7nSi6gbAix+VRU2mhyxh/C3ziF8GSuffzfolPORAKj/ws/UCLyBEio6OR0LJPPiulEEYR1cOsm784GHqCh+7C8MWoRmF1UWZ7nwVR+87Ezaq+ksxLxlKwYwIDAQABAoIBACc0RdOAgYIEltu8GcP2Lx1MnO+CNXfWqYRkEDYnqGe64mBo0pKXSLlIgsR5M4xmYYbGKkkLJl4vyId5vpXBqjFKSLt3RvDKwOEMjXsKJJYshUne/8zpO8siQZQkdSpknk/9lB/5seaT6jkxR0WwGtw17Hi88e7WdZf/w+CYT++vUNDR3thzhGSzgXvfrWppP4XMDnW75HJY+MgRo591vsbLwuQgEMTRqaroU1i5+ivDRak6KhKsiJ3QKJYUO1a+0AUTZMuoOo1Vhyn1qYiaRASYov73vK0WZDLd5/K8anBxWXKVwxj5IBivXcotrlaEQzvvcdu/HxH6+WT4VKQHq5kCgYEA9VFat/q6hGGoSgP3byl2ZbqohoEB2dGFGwgoXKGt8wO2tLhJCAGeyU4uLRAGTk6eO9qnAVr7ZsGmEQ1yaMOwRmatJLZze9yjQufkKOkInrXvVUebXdvRmeUtJ4l0NqtrmkrNcJw49HNR0pjSOhN6R9BGUd75l/P/hU3yjoFF7n0CgYEArAPz8UDYvq1ZKico2vjrWIrnsDpvDsgx8L+i73LzKrL9B3ZTimW+7wsIcWhQF1s27qMnQFPjKbEuqWOTi92TbV7BYXbAyQND0V+y0Txbfs54rGwB2A+0kVTP+sLA/x0mqnek3P2gAsl4p9A5A37rNGESgM64hLd5NOauH60S8F8CgYAixyzQRf2txNaB37wVY1BoraS0pNdpVN3E7kwijb1GZXFif3nDC8/CBDZhpxLtyRF/tMjWVVqsv6lWY4yjs5Jq+KV1PfRzS91NX+ilsBvLvEk40tUA4mf9pFLZdxAlq/muPwqO+2bLqQmheI7JMvez9J/zfWPvGeVQtbM8ZrFOVQKBgQCY+nr8V5trGGdv4ZuoAi/rcr1SMOWL0+b2ILgbE7PGiaAV/tmU/5+qn7lGgmqYGvrjiB3kS7Z+4aCJ7JDPlqMCZX692wrguhKaJe21v2Pvhlgzn2qUaINBrJe6f3F8cMRuXjE0iCrBz8OKGthZj4pF7v6xpybagQE+VtkMOrPZKQKBgDQh5Q4510y+ta+mFPb3tum4cXKBAUeRTS6+Us/0wvNVGpvnPGKzIcP+rGXlAO0Nl7O/PTBgejcIILjcS9AuyxPSfSWhlt5DjjzeQ8/J4yrgVAwQeNC28jkmnKBe5K3R+++Si++nYq4/nZ1WEyyginFf2nvQrW2G+rkzMOKvtRn/
-----END RSA PRIVATE KEY-----'''


publice_key_string = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApNZyqxPGS3xs/p6lpyVImg1XELjReMRz3y2WGhynDeY/vwODsafKy7XDvYPvE6iGasegz4vxtJINOBJprPXqamQvPJq20z/R3CZlCsOEy75Pr77ZRGZbMvzVXGkuavnLQoH40FuRbQYMXt8rLR1GnBS+5Bs5tWNfy94f4x4VroEZ80zVDnQEkzy46fmoi6lZ5r6N/7iXFo0fXdFWlvZJ0EDBF0BdSnHz7nSi6gbAix+VRU2mhyxh/C3ziF8GSuffzfolPORAKj/ws/UCLyBEio6OR0LJPPiulEEYR1cOsm784GHqCh+7C8MWoRmF1UWZ7nwVR+87Ezaq+ksxLxlKwYwIDAQAB
-----END PUBLIC KEY-----'''

# udbble1952@sandbox.com
## 获取支付宝url
def get_alipay_url(order_id, order_amount, subject):
    alipay = AliPay(
          appid="888888888888", # 沙箱appid
          app_notify_url=None, # 默认回调url
          app_private_key_string=private_key_string,
          # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
          alipay_public_key_string=publice_key_string,
          sign_type="RSA2", # RSA 或者 RSA2
          debug=True, # 默认False,我们是沙箱，所以改成True(让访问沙箱环境支付宝地址)
    )
    # 调用支付接口
    # 电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
    order_string = alipay.api_alipay_trade_page_pay(
          out_trade_no=order_id, # 订单id，应该从前端获取生成链接地址如下
          total_amount=str(order_amount), # 订单总金额
          subject=subject, # 付款标题信息
          return_url='http://127.0.0.1:8888/payment/callback/', # 付款成功回调地址(可以为空)
          notify_url=None # 付款成功后异步通知地址（可以为空）
    )
    pay_url = "https://openapi.alipaydev.com/gateway.do?" + order_string
    return pay_url # 将这个url复制到浏览器，就会打开支付宝支付页面


# 获取订单唯一id
def get_order_id():
    """
    SYL202008241212121200005/24
    生成订单号: 格式: SYL + 年月日时分秒 + 5位随机数
    :return:
    """
    d = datetime.datetime.now()
    base = 'SYL'
    time_str = '%04d%02d%02d%02d%02d%02d' % (d.year, d.month, d.day, d.hour,
    d.minute, d.second)
    # 1.4 syl/setings.py中配置支付相关参数
    # 2.测试
    # 请求地址
    # 携带参数
    # 返回数据
    rand_num = str(random.randint(10000, 99999))
    return base + time_str + rand_num


