import requests

url = 'https://ke.qq.com/cgi-bin/comment_new/course_comment_list'
param = {'cid': '396274', 'count': '1'}  # 1表示值显示一条数据
headers = {'Referer': 'https://ke.qq.com/course/396274'}  # 必要的头域参数
# get请求
resp = requests.get(url, params=param, headers=headers)
print(resp.text)