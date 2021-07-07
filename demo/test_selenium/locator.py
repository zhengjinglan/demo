# _*_encoding:'utf-8' _*_
from selenium import webdriver
from time import sleep

#创建一个浏览器对象
driver = webdriver.Chrome()
#基于id
# driver.find_element_by_id('id')
# #基于Neme
# driver.find_element_by_name()
#基于link text
# driver.get('http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html')
# driver.find_element_by_link_text('注册').click()
#基于partial link text
# driver.find_element_by_partial_link_text('首页').click()
#基于classname
# driver.find_element_by_class_name('am-radius').click()
#基于tagname
# dr = driver.find_elements_by_tag_name('a')
# for d in dr:
#     if d.text == '登录':
#         d.click()
#         break
#cssSelector定位
# driver.find_element_by_css_selector('body > div.am-g.my-content')
#xpath
driver.get('http://www.baidu.com')
sleep(2)
driver.find_element_by_xpath('//*[text()="百度热榜"]/..').click()