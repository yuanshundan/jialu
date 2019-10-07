import re

from common.read_config import ReadConfig
from common.project_path import conf_path

class GetData:
    """可以动态的更改  删除 获取数据"""
    token = None  # 设置token初始值为None
    user = ReadConfig(conf_path).get_str('data', 'user')  # user=18011901256
    pwd = ReadConfig(conf_path).get_str('data', 'pwd')  # pwd=123456
    id = ReadConfig(conf_path).get_str('data', 'id')  # id=120

def replace(string):
    # string = "{'user':'#user#','pwd':'#pwd#',id='#id#'}"  # 目标字符串
    pattern = "#(.*?)#"  # 正则表达式
    while re.search(pattern, string):  # 找到参数化的字符串就返回match对象：True
        m = re.search(pattern, string)  # 只返回第一次找到的值
        key = m.group(1)  # 第一次找到user，第二次找到pwd
        value = getattr(GetData, key)  # 拿到需要替换的值，为什么要使用反射？因为要替换多次
        string = re.sub(pattern, value, string, count=1, flags=0)
    return string  # {'user':'18011901256','pwd':'123456',id='120'}

# # 利用反射的方法来拿值
# getattr(GetData, 'token')  # 查看类属性
# hasattr(GetData, 'token')  # 判断类是否有属性存在，返回布尔值
# setattr(GetData, 'ken', '123456')  # 设置类的属性，没有返回值，如果没有该属性就直接创建一个新的属性
# # delattr(GetData, 'token')  # 删除类的某个属性
# # 查看类属性
# print(GetData.ken)
# # print(GetData().COOKIE)