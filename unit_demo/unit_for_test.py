# _*_encoding:'utf-8' _*_
#导入unittest包
import unittest
from selenium import webdriver
from time import sleep

class UnitForTest(unittest.TestCase):
    #前置条件（初始化）
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html')
        self.driver.implicitly_wait(10)

    #后置条件(执行完成关闭浏览器页面）
    def tearDown(self) -> None:
        self.driver.quit()

    #定义测试用例校验账号密码2
    def test_2(self):
        # driver = webdriver.Chrome()
        # driver.get('http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html')
        # driver.implicitly_wait(10)
        self.driver.find_element_by_name('accounts').send_keys('123456')
        self.driver.find_element_by_name('pwd').send_keys('123456')
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()
        sleep(5)
    #校验账号密码1
    def test_1(self):
        # driver = webdriver.Chrome()
        # driver.get('http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html')
        # driver.implicitly_wait(10)
        self.driver.find_element_by_name('accounts').send_keys('666666')
        self.driver.find_element_by_name('pwd').send_keys('666666')
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()
        sleep(5)
if __name__ == '__main__':
    unittest.main()