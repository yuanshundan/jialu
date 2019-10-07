import requests

url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php'
param = {'query': '12.123.12.1', 'resource_id': '6006'}

# get请求
resp = requests.get(url, params=param)
print(resp.text)

#得到结果：{"status":"0","t":"","set_cache_time":"","data":[{"location":"美国加利福尼亚旧金山","titlecont":"IP地址查询","origip":"12.123.12.1","origipquery":"12.123.12.1","showlamp":"1","showLikeShare":1,"shareImage":1,"ExtendedLocation":"","OriginQuery":"12.123.12.1","tplt":"ip","resourceid":"6006","fetchkey":"12.123.12.1","appinfo":"","role_id":0,"disp_type":0}]}
"""
请求部分：
在接口测试中，接口请求信息中，需关注4大信息
接口URL地址、请求方法、请求头、请求参数

响应部分：
在接口测试中，接口响应验证，需关注3大信息
HTTP状态码、检查返回头域、查看返回内容
"""