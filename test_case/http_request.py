import requests


class HttpRequest:
    """完成http的get和post请求"""

    def http_request(self, method, url, param, **kwargs):
        """根据您请求方法来决定发起get或者post请求
        method：get或者post的http请求方式
        url：发送请求的接口地址
        param：随接口发送的请求参数
        rtype：有返回值，返回结果是响应报文"""

        if method == 'GET':
            try:
                resp = requests.get(url, params=param, **kwargs)
            except Exception as e:
                print("get请求出错了:{}".format(e))
        elif method == 'POST':
            try:
                resp = requests.post(url, data=param, **kwargs)
            except Exception as e:
                print("post请求出错了:{}".format(e))
        else:
            resp = None
        return resp


if __name__ == '__main__':
    url = 'http://www.testingedu.com.cn/inter/HTTP/auth'
    resp = requests.post(url)
    print(resp.text)
    print(eval(resp.text)['token'])

    method = 'POST'
    url_1 = 'http://www.testingedu.com.cn/inter/HTTP//register'
    param_1 = {'username': 'abb', 'pwd': '123456', 'nickname': 'abb'}
    headers = {'token': eval(resp.text)["token"]}
    resp_1 = HttpRequest().http_request(method, url_1, param_1, headers=headers)
    print(resp_1.text)







