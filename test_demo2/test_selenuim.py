# _*_encoding:'utf-8' _*_
from selenium import webdriver
#调用selenium浏览器驱动，获取浏览器句柄
driver = webdriver.Chrome()
#通过句柄访问url
first_url = 'http://www.baidu.com'
driver.get(first_url)
#通过句柄控制页面元素
driver.find_element_by_id("kw").send_keys("selenium") #在搜索框输入selenium
driver.find_element_by_id("su").click() #点击百度一下