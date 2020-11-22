import requests #先导入爬虫的库

response = requests.get("http://www.zhihu.com")

print("第一次访问，不设置头部信息，状态码"+str(response.status_code))

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36"
}

response = requests.get("http://www.zhihu.com",headers=headers) #get 方法访问
print(response.status_code)
print(response.text)
