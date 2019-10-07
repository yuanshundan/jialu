import requests

url = 'http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=do_login&t=0.6454778738518367'
headers = {'content-type': "application/x-www-form-urlencoded"}  # 头部添加:application/x-www-form-urlencoded
data = {'username': '18011901256@163.com', 'password': '123456', 'verify_code': '1'}  # x-www-form-urlencoded类型参数
# post请求
resp = requests.post(url, data=data, headers=headers)
print(resp.text)  # 得到的结果需进行unicode转码
# 得到结果：{"status":-1,"msg":"\u8d26\u53f7\u4e0d\u5b58\u5728!"}