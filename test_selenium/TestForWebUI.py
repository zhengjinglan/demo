# _*_encoding:'utf-8' _*_
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

#创建一个浏览器对象
driver = webdriver.Chrome()
#设置隐式等待,纯粹基于webdriver进行调用的
# driver.implicitly_wait(10)
#获取url路径
driver.get('http://www.baidu.com')
#通过id来获取元素信息
driver.find_element_by_id('kw').send_keys('虚竹')
#触发点击事件
driver.find_element_by_id('su').click()
#强制等待
# sleep(1)
#设置显式等待
locator = (By.XPATH, '//*[@id="1"]/h3/a')
WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located(locator))


#进入第一条链接
# driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()