import HTMLTestRunnerNew

from test_case import TestCases
import unittest
from common import project_path

# 新建一个测试集
suite = unittest.TestSuite()
# 添加用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestCases))

# 执行用例，生成测试报告
with open(project_path.report_path, 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title='case测试报告',
                                              description='测试报告',
                                              tester='dandan')

    runner.run(suite)  # 执行用例  传入收集的用例
