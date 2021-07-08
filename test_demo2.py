# _*_encoding:utf-8 _*_
import re #引入正则工具库
import requests #引入第三方requests库
import os

'''获取网页图片'''
#浏览器链接地址
# url = 'https://tieba.baidu.com/p/5738152382'
url = 'http://www.qqjay.com/keaitupian/98803.html'

#获取贴吧源码
result = requests.get(url)
# print(result)
# res = result.text  #获取源码
# print(res)

#提取数据
# photos = re.findall('src="(http.*?.jpg)"', result.text)
photos = re.findall('src="(http.*?.jpg)"', result.text)
print(photos)

num = 0
filename = 'D:\Python\爬取图片'  # 图片保存位置
if not os.path.exists(filename):  # 判断是否有这个文件夹
    os.makedirs(filename)  # 如果没有这个文件夹，就创建
#保存数据
for i in photos:
    res = requests.get(i)
    with open(filename + '\图片{}.jpg'.format(num), 'wb') as f:
        f.write(res.content)
        print('第{}次保存'.format(num))
        num = num + 1

