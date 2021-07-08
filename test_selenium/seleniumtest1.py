# _*_encoding:'utf-8' _*_
from selenium import webdriver

#基本的selenium
#创建webdriver对象
driver = webdriver.Chrome()
#访问url
driver.get('http://www.baidu.com')
#定位到输入文本框进行输入
driver.find_element('id', 'kw').send_keys('虚竹')
#定位到百度一下按钮,进行点击
driver.find_element('id', 'su').click()
