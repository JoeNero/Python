import requests

response = requests.get("http://httpbin.org/get") #get方法
print(response.status_code) #状态码
print(response.text)
