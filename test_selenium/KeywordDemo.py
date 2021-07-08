# _*_encoding:'utf-8' _*_
from selenium import webdriver

class KeywordDemo(object):
    #初始化
    def __init__(self, browser_type, url):
        self.browser_init(browser_type)
        self.visit(url)

    #创建webdriver对象
    def browser_init(self, browser_type):
        if browser_type == 'chrome':
            self.driver = webdriver.Chrome()
            return self.driver
        if browser_type == 'ff':
            self.driver = webdriver.Firefox()
            return self.driver
        else:
            self.driver = webdriver.Ie()
            return self.driver
    #访问url
    def visit(self, url):
        self.driver.get(url)

    #定位元素
    def locator(self):
       el = self.driver.find_element_by_id()
       return el
    #输入
    def input_text(self, value):
        self.locator().send_keys(value)

    #点击
    def click(self):
        self.locator().click()

if __name__ == '__main__':
    kd = KeywordDemo('chrome', 'https://www.baidu.com')