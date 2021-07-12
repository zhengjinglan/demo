# _*_encoding:'utf-8' _*_
import unittest, os
from unit_demo.unit_for_test import UnitForTest
from HTMLTestRunner import HTMLTestRunner

#创建测试套件
suite = unittest.TestSuite()

#添加测试用例
# suite.addTest(UnitForTest('test_6'))
# suite.addTest(UnitForTest('test_5'))
# suite.addTest(UnitForTest('test_4'))
#添加测试用例2
# cases = [UnitForTest('test_6'), UnitForTest('test_5'), UnitForTest('test_4')]
# suite.addTests(cases)

#添加测试用例3
# test_dir = './'
# discover = unittest.defaultTestLoader.discover(start_dir= test_dir, pattern= 'unit_for*.py')

#添加测试用例4
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(UnitForTest))

#添加测试用例5
# suite.addTests(unittest.TestLoader().loadTestsFromName('unit_for_test.UnitForTest'))

#基于Runner来运行测试套件
# runner = unittest.TextTestRunner()
# runner.run(suite)

#集成测试报告
report_name = '测试报告'
report_title = '标题'
report_desc = '描述'
#保存路径
report_path = './report/'
report_file = report_path + 'report.html'

#判断文件夹是否存在，如果不存在就创建
if not os.path.exists(report_path):
    os.mkdir(report_path)
else:
    pass
#HTMLTestRunner使用
with open(report_file, 'wb') as report:
    suite.addTests(cases)
    runner = HTMLTestRunner(stream= report, title=report_title, description= report_desc)
    runner.run(suite)