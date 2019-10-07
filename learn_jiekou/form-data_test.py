import requests


url = 'http://www.testingedu.com.cn:8000/index.php/home/Uploadify/imageUp/savepath/head_pic/pictitle/banner/dir/images.html'
headers = {'multipart': "form-data"}  # 上传文件，头部默认添加:multipart/form-data
files = {'file': open('C://Users//HP//Desktop//test.jpg', 'rb')}  # 上传文件,form-data格式参数

# post请求
resp = requests.post(url, files=files, headers=headers)
print(resp.text)

# 得到结果:{"url":"\/public\/upload\/user\/\/head_pic\/\/d63d647289b9ce8cc7968c562629304b.jpg","title":"banner","original":"","state":"SUCCESS","path":"images"}


