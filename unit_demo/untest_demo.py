# _*_encoding:'utf-8' _*_
import unittest
from unit_demo.unit_for_test import UnitForTest

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
suite.addTests(unittest.TestLoader().loadTestsFromName('unit_for_test.UnitForTest'))

#基于Runner来运行测试套件
runner = unittest.TextTestRunner()
runner.run(suite)
