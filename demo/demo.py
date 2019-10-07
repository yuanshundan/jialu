import time

import requests


# 发起鉴权post请求
url = 'http://www.testingedu.com.cn/inter/HTTP/auth'
resp = requests.post(url)
print(resp.text)
print(eval(resp.text)['token'])

# 发起注册post请求
# url_1 = "http://www.testingedu.com.cn/inter/HTTP//register"
# data = {'username': 'abb', 'pwd': '123456', 'nickname': 'abb'}
# headers = {'token': eval(resp.text)["token"]}
# resp_1 = requests.post(url_1, data=data, headers=headers)
# print(resp_1.text)

# 发起登录post请求
url_2 = "http://www.testingedu.com.cn/inter/HTTP/login"
headers_2 = {'token': eval(resp.text)["token"]}
data = {'username': 'abb', 'password': '123456'}
resp_2 = requests.post(url_2, data=data, headers=headers_2)
print(resp_2.text)
time.sleep(2)
url_3 = "http://www.testingedu.com.cn/inter/HTTP/login"
headers_3 = {'token': eval(resp.text)["token"]}
data_3 = {'username': 'abb', 'password': '123456'}
resp_3 = requests.post(url_3, data=data_3, headers=headers_3)
print(resp_2.text)
#
#
# # 发起查询post请求
# url_3 = "http://www.testingedu.com.cn/inter/HTTP/getUserInfo"
# data_3 = {'id': eval(resp_2.text)["userid"]}
# headers_3 = {'token': eval(resp.text)["token"]}
# resp_3 = requests.post(url_3, data=data_3, headers=headers_3)
# print(resp_3.text)
#
#
# # 发起退出post请求
# url_4 = 'http://www.testingedu.com.cn/inter/HTTP//logout'
# headers_4 = {'token': eval(resp.text)["token"]}
# resp_4 = requests.post(url_4, headers=headers_4)
# print(resp_4.text)

