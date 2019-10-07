import requests

from common.my_log import MyLog
from ddt import ddt, data
import unittest
from common.do_excel import DoExcel
from common.project_path import case_path
from test_case.http_request import HttpRequest
test_data = DoExcel(case_path, 'login').read_data()
my_log = MyLog()


def jianquan():
    url = 'http://www.testingedu.com.cn/inter/HTTP/auth'
    resp = requests.post(url)
    return eval(resp.text)['token']

@ddt
class TestRegister(unittest.TestCase):
    """测试testing网站注册"""

    @data(*test_data)
    def test_register(self, case):
        # 执行测试
        # global TestResult
        # global token  # 声明全局变量
        method = case['Method']
        url = case['Url']
        param = eval(case['Params'])
        h = {'token': jianquan()}
        # 3.发起测试
        my_log.info('----正在测试{}模块第{}条测试用例：{}----'.format(case['Module'], case['CaseID'], case['Title']))
        my_log.info('测试数据是：{}'.format(case))
        resp = HttpRequest().http_request(method, url, param=param, headers=h)
        try:
            self.assertEqual(case['ExpectedResult'], resp.text)
            TestResult = 'Pass'
        except Exception as e:
            TestResult = 'Failed'
            my_log.error('注册失败：{}'.format(e))
            raise e  # 将异常抛出
        finally:
            # 写回结果
            t = DoExcel(case_path, 'login')
            t .write_back(case['CaseID'] + 1, 8, resp.text)  # 写回实际结果
            t .write_back(case['CaseID'] + 1, 9, TestResult)  # 写回测试结论
        my_log.info('实际结果是：{}'.format(resp.text))