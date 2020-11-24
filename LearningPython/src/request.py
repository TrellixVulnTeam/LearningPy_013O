import pip._vendor.requests as requests
url = 'https://www.baidu.com'
r=requests.get(url)
print(r.status_code)
print(r.text)
# 读取返回的内容
print(type(r.text))