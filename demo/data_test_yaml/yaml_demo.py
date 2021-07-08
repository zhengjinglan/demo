# _*_encoding:'utf-8' _*_
from selenium import webdriver
import yaml

#读取文件
file = open('../data/data1.yaml', 'r', encoding= 'utf-8')
data = yaml.load(stream= file, Loader=yaml.FullLoader)
#数据类型的展示
print(type(data))
print(data)
#数据内容的展示
print(data['dict'])
