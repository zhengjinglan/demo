# _*_encoding:'utf-8' _*_
'''
loginpage类，专门用于实现登录页面对象的文件
主体内容包含：
1.核心的页面元素
    账号、密码、登录按钮
2.核心的业务流程
    用户的登录行为
'''
from dom.base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver

class LoginPage(BasePage):
    #核心元素
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'

    user = (By.NAME, 'accounts')
    password = (By.NAME, 'pwd')
    login_button = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')


    #核心业务流
    def login(self, username, pwd):
        self.visit()
        self.input_(self.user, username)
        self.input_(self.password, pwd)
        self.click(self.login_button)

#调试代码
# if __name__ == '__main__':
#    driver = webdriver.Chrome()
#    username = 'xuzhu666'
#    password = '123456'
#    lp = LoginPage(driver)
#    lp.login(username, password)