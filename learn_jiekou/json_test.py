import requests
import json
# 第一种方式
url = 'https://b.zhulogic.com/designer_api/account/login_quick_pc'
headers = {'content-type': "application/json"}  # 添加请求头域为json格式
data = json.dumps({"phone": "18011901356", "code": "", "messageType": 3, "registration_type": 1, "channel": "zhulogic", "unionid": ""})#添加body为json格式
# post请求
resp = requests.post(url, data=data, headers=headers)
print(resp.text)
print(type(resp.text))
# 得到结果：
# {"status_code":1001,"message":"验证码不能为空！","data":null}
# <class 'str'>

# 第二种方式
# url = 'https://b.zhulogic.com/designer_api/account/login_quick_pc'
# headers = {'content-type': "application/json"}  # 添加请求头域
# body = {"phone": "18011901356", "code": "", "messageType": 3, "registration_type": 1,"channel": "zhulogic", "unionid": ""}#添加body为json格式
# # post请求
# resp = requests.post(url, json=body, headers=headers)
# print(resp.text)