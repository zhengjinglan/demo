# _*_encoding:'utf-8' _*_
import requests
import unittest

class APITest11(unittest.TestCase):
    #测试网站https://www.juhe.cn/docs
    url = "http://httpbin.org"

    #发送请求-get:header, get, url
    def test_001(self):
        #请求参数
        url = self.url + "/get"
        #发送请求并接收响应
        resl = requests.get(url)
        #结果码：200，响应内容
        print(resl.status_code)
        print(resl.text) #响应内容

    def test_002(self):
        #请求参数
        url = self.url + "/get" + "?name=zhangsan&age=18"
        #发送请求并接收响应
        resl = requests.get(url)
        print(resl.status_code)
        print(resl.text)  # 响应内容


    def test_003(self):
        #请求参数
        url = self.url + "/get"
        parames = {"name":"zhangsan1", "age":18}
        #发送请求并接收响应
        resl = requests.get(url, params=parames)
        print(resl.status_code)
        print(resl.text)  # 响应内容

    #响应结果处理
    def test_004(self):
        #请求参数
        url = self.url + "/get"
        parames = {"name":"zhangsan1", "age":18}
        #发送请求并接收响应
        res1 = requests.get(url, params=parames)
        print(res1.status_code)
        print(res1.text)  # 响应内容
        print(res1.headers)
        print(res1.headers["Content-Type"])
        print(res1.cookies)
        print(res1.encoding)

    #编码
    def test_005(self):
        #请求参数
        url = self.url + "/get"
        parames = {"name":"张三", "age":18}
        #发送请求并接收响应
        res1 = requests.get(url, params=parames)
        if res1.status_code == 200:
            print(res1.text)  # 响应内容
            print(res1.content.decode('unicode-escape')) #自己解码,先通过获取到字节码然后进行deco，Unicode自己的解码方式
        else:
            print(res1.status_code)

        # 编码
    def test_006(self):
        # 发送请求并接收响应
        res1 = requests.get("http://www.baidu.com")
        if res1.status_code == 200:
            # print(res1.text)  # 响应内容
            print(res1.content.decode('utf8'))  # 自己解码,先通过获取到字节码然后进行deco，Unicode自己的解码方式
        else:
            print(res1.status_code)

    #编码方式查看
    def test_007(self):
        # 发送请求并接收响应
        res1 = requests.get("http://www.baidu.com")
        print(res1.apparent_encoding) #根据响应内容推断，推断结果可靠
        print(res1.encoding) #解码方式，根据header内容做推断，如果没有则默认：ISO-8859-1
        if res1.status_code == 200:
            print(res1.text)  # 响应内容，默认以encoding的方式解码
            print(res1.content.decode('utf8'))  # 自己解码,先通过获取到字节码然后进行deco，Unicode自己的解码方式
        else:
            print(res1.status_code)