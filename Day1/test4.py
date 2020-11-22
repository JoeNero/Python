import requests #导入爬虫库

response = requests.get("http://httpbin.org/get?name=hezhi&age=20") #get 传参数

print(response.status_code) #状态码
print(response.text)
