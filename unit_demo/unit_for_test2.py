# _*_encoding:'utf-8' _*_
#导入unittest包
import unittest
from selenium import webdriver
from time import sleep
from ddt import ddt, data, unpack, file_data

def read_file():
    file = open('params.txt', 'r', encoding= 'utf8')
    # file = open('test1.yaml', 'r', encoding='utf8')
    li = []
    for line in file.readlines():
        # print(line)
        li.append(line.strip('\n').split(','))
    # for l in li:
        # print(l)
    file.close()
    return li

@ddt
class UnitForTest(unittest.TestCase):
    #前置条件（初始化）
    # def setUp(self) -> None:
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html')
    #     self.driver.implicitly_wait(10)
    #
    # #后置条件(执行完成关闭浏览器页面）
    # def tearDown(self) -> None:
    #     self.driver.quit()
    #
    # #定义测试用例校验账号密码2
    # # @data(['666666', '123456'], ['123456', '123456'], ['123456', '666666']) #传多个参数要用中括号
    # @data(*read_file())
    # @unpack #解包 @装饰器
    # def test_2(self, username, pwd):
    #     self.driver.find_element_by_name('accounts').send_keys(username)
    #     self.driver.find_element_by_name('pwd').send_keys(pwd)
    #     self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()
    #     sleep(2)
    #
    # #一般函数，用于让测试用例调用的函数，只有在调用的时候才会生效
    # def plus(self):
    #     s = 1
    #     b = 2
    #     return s + b

    #传入的参数是字典格式，不需要添加unpack进行数据的解包
    @file_data('test1.yaml')
    def test_1(self, **user):
        name = user.get('name')
        pwd = user.get('pwd')
        print(name)
        print(pwd)
        # if name == 123456:
        #     print('successful!')
        # else:
        #     print('fale')
        self.assertEqual(123456, name, msg= '我是msg')
        print('这是断言之后的打印内容')
        self.assertAlmostEqual(9.023456789, 9.02345679, msg= '这是一个大约值')
    #无条件跳过本条用例执行
    # @unittest.skip("不想执行")
    def test_3(self):
        print('2test3')
    #有条件跳过本条用例  = false等于false的时候才会执行
    # @unittest.skipUnless(1 < 2, '这是unless的理由')
    def test_4(self):
        print('2test4')
    #有条件跳过本条用例 = true 等于true的时候才会执行
    # @unittest.skipIf(1 > 2 , '这是if理由')
    def test_5(self):
        print('2test5')

    # @unittest.expectedFailure
    def test_6(self):
        print('2test6')
        self.assertEqual(123123, 222222, msg= 'Not Equal')
    def test_7(self):
        print('2test7')
        self.assertEqual(123123, 222222, msg='Not Equal')
# if __name__ == '__main__':
    # unittest.main()