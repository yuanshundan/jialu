import requests

url = 'https://www.tianqiapi.com/api/'
param = {'appid': 'nalan358', 'appsecret': '123456789', 'version': 'v1', 'city': '宜春'}  # city可选参数

# get请求
resp = requests.get(url, params=param)
print(resp.text)
