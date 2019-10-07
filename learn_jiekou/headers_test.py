import requests

url = 'https://api.yonyoucloud.com/apis/pte/New_Issue_Bond_Information/New_Issue_Bond_Information?size=2'
headers = {'apicode': '0ec6701427a7418d860de8968d137114'}  # 添加请求头域

# post请求
resp = requests.post(url, headers=headers)
print(resp.text)
