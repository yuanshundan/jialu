import unittest
from common.project_path import case_path
from common.do_excel import DoExcel
from common.my_log import MyLog
from web_test.test_login import TestLogin
from ddt import ddt, data

test_data = DoExcel(case_path, 'login').read_data()
my_log = MyLog()


@ddt
class TestCases(unittest.TestCase):

    @data(*test_data)
    def test_case(self, case):
        # 执行测试
        # global TestResult
        url = case['Url']
        param = eval(case['Params'])
        # 3.发起测试
        my_log.info('----正在测试{}模块第{}条测试用例：{}----'.format(case['Module'], case['CaseID'], case['Title']))
        my_log.info('测试数据是：{}'.format(case))
        res = TestLogin().test_2_login_success(url, param['user'], param['pwd'])
        try:
            self.assertEqual(case['ExpectedResult'], res)
            TestResult = 'Pass'
        except AssertionError as e:
            TestResult = 'Failed'
            my_log.error('登录失败：{}'.format(e))
            raise e  # 将异常抛出
        finally:
            # 写回结果
            t = DoExcel(case_path, 'login')
            t .write_back(case['CaseID'] + 1, 7, res)  # 写回实际结果
            t .write_back(case['CaseID'] + 1, 8, TestResult)  # 写回测试结论
        my_log.info('实际结果是：{}'.format(res))

