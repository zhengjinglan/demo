# -*-coding:utf-8 -*-
import requests
get_url = 'http://127.0.0.1:8000/student_manage/'
'''
产生一个名为r的response对象，可以从这个对象中获取我们想要的信息；
get请求传参数时，使用params关键字
timeout参数用来设定停止等待响应的时间
'''
r = requests.get(url= get_url, timeout = 5)
print('r.url===', r.url) #返回请求url
# print('r.json===', r.json()) #以json格式解析响应内容
print('r.status_code===', r.status_code) #返回状态码
print('r.raise_for_status===', r.raise_for_status()) #如果发送了一个错误请求，如404、500等，可以通过raise_for_status()来抛出异常
print('r.encoding===', r.encoding) #查看requests使用了什么编码，同时可以用r.encoding属性来改变它
print('r.raw===', r.raw) #获取来自服务器的原始套接字响应
print('r.headers===', r.headers) #服务器返回给我们的响应头信息，也可以在传参时通过headers=XXX来定制请求头
print('r.request===', r.request) #获取原来创建的request对象
print('r.request.headers===', r.request.headers) #发送到服务器的请求头
