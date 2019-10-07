class GetData:
    """可以动态的更改  删除 获取数据"""
    COOKIE = None
    LOAD_ID = None
# 查看类属性
# print(GetData.COOKIE)
# print(GetData().COOKIE)

# 利用反射的方法来拿值
getattr(GetData, 'COOKIE')  # 查看类属性
hasattr(GetData, 'COOKIE')  # 判断类是否有属性存在，返回布尔值
setattr(GetData, 'COOKIE', '123456')  # 设置类的属性，没有返回值
delattr(GetData, 'COOKIE')  # 删除类的某个属性