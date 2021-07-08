# _*_encoding:'utf-8' _*_
import unittest
from selenium import webdriver

class Ranzhi(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() #选择Chrome浏览器
    def test_ranzhi(self):
        # pass
        self.assertEqual("http://127.0.0.1/student_manage", self.driver.current_url,"查询跳转失败")
    def tearDown(self):
        self.driver.quit() #退出浏览器