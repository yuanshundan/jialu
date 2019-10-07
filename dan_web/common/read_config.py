from configparser import ConfigParser
from common.project_path import conf_path


class ReadConfig():
    """读取配置文件"""

    def __init__(self, file_name):  # 配置文件的地址
        self.cf = ConfigParser()  # 创建对象
        self.cf.read(file_name, encoding='utf-8')  # 打开文件

    def get_boolean(self, section, option):
        """从配置文件读取一个布尔值"""
        value = self.cf.getboolean(section, option)
        return value

    def get_int(self, section, option):
        """从配置文件读取一个整数"""
        value = self.cf.getint(section, option)
        return value

    def get_float(self, section, option):
        """从配置文件读取一个浮点数"""
        value = self.cf.getfloat(section, option)
        return value

    def get_str(self, section, option):
        """从配置文件读取一个字符串"""
        value = self.cf.get(section, option)
        return value

    def get_data(self, section, option):
        """从配置文件中读取一个列表"""
        value = self.cf.get(section, option)
        return eval(value)  # 如果已经是一个字符串就不需要eval


if __name__ == '__main__':
    case_id = ReadConfig(conf_path).get_data('CASE', 'case_id')
    print(case_id)