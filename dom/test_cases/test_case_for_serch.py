# _*_encoding:'utf-8' _*_

import unittest
from selenium import webdriver
from dom.page_object.login_page import LoginPage
from dom.page_object.index_page import IndexPage
from time import sleep
from ddt import ddt, file_data, data

#测试用例的设计
@ddt
class TestCaseForSerch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.ip = IndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @file_data('../data/user.yaml')
    def test_1_login(self , username, password, ttt):
        txt = self.lp.login(username, password, ttt)
        # print(txt)
        sleep(3)
        self.assertEqual(txt, ttt)

    @data('手机', '衣服', '电脑')
    def test_2_serch(self, txt):
        self.ip.serch(txt)
        sleep(3)

if __name__ == '__main__':
    unittest.main()