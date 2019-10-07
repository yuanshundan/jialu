import requests
url = "http://httpbin.org/post"
headers = {'content-type': "application/xml"}
# 第一种方式
with open('body.xml', encoding='utf-8') as fp:
    data = fp.read()  # 使用open函数对xml进行读取

resp = requests.post(url, data=data.encode("utf-8"))  # 设置编码，utf-8可支持中英文
print(resp.text)

# 第二种方式
# python3字符串换行，在右边加个反斜杠
# body = '<?xml version="1.0" encoding = "UTF-8"?>' \
#         '<COM>' \
#         '<REQ name="北京-宏哥">' \
#         '<USER_ID></USER_ID>' \
#         '<COMMODITY_ID>123456</COMMODITY_ID>' \
#         '<SESSION_ID>absbnmasbnfmasbm1213</SESSION_ID>' \
#         '</REQ>' \
#         '</COM>'
#
# resp = requests.post(url, data=body.encode("utf-8"))
# print(resp.text)

