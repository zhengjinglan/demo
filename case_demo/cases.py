# _*_encoding:'utf-8' _*_
import unittest
from ddt import ddt, file_data
from selenium import webdriver

@ddt
class CaseDemo(unittest.TestCase):

    @file_data('../data/data2.yaml')
    def test_01(self, **kwargs):
        print(kwargs['url'])
        print(kwargs['params'])
        print(kwargs['method'])
        # print(kwargs.get('name'))
        # print(kwargs)
        # driver = webdriver.Chrome()
        # driver.get(kwargs['url'])
        # driver.find_element_by_id('kw').send_keys(kwargs['txt'])\
    @file_data('../data/login.yaml')
    def test_02(self, **kwargs):
        print(kwargs['userName'])
        print(kwargs['pwd'])

if __name__ == '__main__':
    unittest.main()