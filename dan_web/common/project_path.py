import os


# 文件的路径放在这里
project_path = os.path.realpath(__file__)  # 获取当前路径
project_path_1 = os.path.split(os.path.realpath(__file__))[0]  # 切割
project_path_2 = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# 测试用例的路径
case_path = os.path.join(project_path_2, 'web_data', 'test.xlsx')  # 拼接

# 测试报告路径
report_path = os.path.join(project_path_2, 'web_Result', 'test_report', 'test_report.html')

# 测试日志路径
log_path = os.path.join(project_path_2, 'web_Result', 'test_log', 'test.log')

# 配置文件路径
conf_path = os.path.join(project_path_2, 'conf', 'case.conf')