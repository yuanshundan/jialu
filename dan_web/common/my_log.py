import logging
from common import project_path
from common.read_config import ReadConfig


class MyLog:
    # def __init__(self):
    #     self.logger_name = ReadConfig().get_data()

    def mylog(self, level, msg):
        my_logger = logging.getLogger('log')  # 1：定义一个日志收集器并设置级别
        my_logger.setLevel('DEBUG')  # 1：定义一个日志收集器并设置级别

        formatter = logging.Formatter('[%(asctime)s]-[%(''levelname)s]-[%(filename)s]-[%(''name)s]-[日志信息：%(message)s]')   # 3：对接:取步骤1和步骤2的交集
        ch = logging.StreamHandler()  # 2.(1):制定输出渠道并设置级别（输出到控制台），可设置输出渠道的格式
        ch.setLevel('DEBUG')  # 设置级别
        ch.setFormatter(formatter)  # 设置格式

        fh = logging.FileHandler(project_path.log_path, encoding='utf-8')  # 写入到指定的文件里面
        fh.setLevel('DEBUG')  # 设置级别
        fh.setFormatter(formatter)  # 设置格式

        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)
        my_logger.removeHandler(ch)

    def debug(self, msg):
        self.mylog('DEBUG', msg)

    def info(self, msg):
        self.mylog('INFO', msg)

    def warning(self, msg):
        self.mylog('WARNING', msg)

    def error(self, msg):
        self.mylog('ERROR', msg)

    def critical(self, msg):
        self.mylog('CRITICAL', msg)


if __name__ == '__main__':
    MyLog().debug('停电')