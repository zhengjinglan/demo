# _*_encoding:'utf-8' _*_
#导入unittest包
import unittest

class UnitForTest(unittest.TestCase):
    #class前置条件
    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')
    #class后置条件
    @classmethod
    def tearDownClass(cls) -> None:
        print('tesrDownClass')
    #前置条件
    def setUp(self) -> None:
        print('setUp')

    #后置条件
    def tearDown(self) -> None:
        print('tearDown')

    #定义测试用例
    def test_2(self):
        print("this is test2")

    def test_1(self):
        print("this is test1")

if __name__ == '__main__':
    unittest.main()