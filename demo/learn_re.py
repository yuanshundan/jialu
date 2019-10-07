import re
from common.get_data import GetData
# string = "{'user':'#user#','pwd':'#pwd#'}"  # 目标字符串
# pattern = "#(.*?)#"  # 正则表达式
# # m = re.search(pattern, string)  # 扫描目标字符串，找到1次后不再进行查找
# # print(m)
# # print(m.group(1))  # 传入参数1，返回后为 ：user，不传入1，则返回：#user#
# # mm = re.findall(pattern, string)  # 扫描目标字符串，找到所有符合条件的值
# # print(mm)  # 无论找到几个值，都返回一个列表:['user', 'pwd']
# # string_1 = re.sub(pattern, '15678552', string, count=1, flags=0)  # 替换目标字符串
# # print(string_1)  # {'user':'15678552','pwd':'#pwd#'}

string = "{'user':'#user#','pwd':'#pwd#',id='#id#'}"  # 目标字符串
pattern = "#(.*?)#"  # 正则表达式
while re.search(pattern, string):  # 找到参数化的字符串就返回match对象：True
    m = re.search(pattern, string)  # 只返回第一次找到的值
    key = m.group(1)  # 第一次找到user，第二次找到pwd
    value = getattr(GetData, key)  # 拿到需要替换的值，为什么要使用反射？因为要替换多次
    string = re.sub(pattern, value, string, count=1, flags=0)
print(string)  # {'user':'18011901256','pwd':'123456',id='120'}

