import HTMLTestRunnerNew
from test_case.test_register import TestRegister
import unittest
from common import project_path

# 新建一个测试集
suite = unittest.TestSuite()
# 添加用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestRegister))  # 添加注册用例

# 执行用例，生成测试报告
with open(project_path.report_path, 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title='特斯汀注册测试报告',
                                              description='注册模块测试报告',
                                              tester='Amy')

    runner.run(suite)  # 执行用例  传入收集的用例