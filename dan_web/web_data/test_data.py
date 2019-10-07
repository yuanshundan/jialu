'''数据准备 1.账号 2.密码 3.预期结果
用户分组依据：
手机号码为空，密码为空：请输入帐号
手机号码为空，密码不为空：请输入帐号
手机号码不为空，密码为空：请输入邮箱密码
手机号码不为空，密码不为空：帐号或密码有误，请重试'''

"""bid_test页面"""
invest_money = 100

"""bid_test页面"""
bid_user_info_success = {'username':"18684720553",'pwd':"python","expected":"我的帐户[小小鸟]"}


"""bid_test页面"""
user_info_success = [{'username':"18684720553",'pwd':"python","expected":"我的帐户[小小鸟]"}]
"""login_test页面"""
user_info_error = [{'username':"",'pwd':"","expected":"请输入手机号"},
                 {'username':"",'pwd':"123","expected":"请输入手机号"},
                 {'username':"12",'pwd':"123","expected":"请输入正确的手机号"}
]

x = {'username':"18684720553",'pwd':"123","expected":"此账号没有经过授权，请联系管理员！"}