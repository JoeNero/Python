import requests

response = requests.post("http://httpbin.org/post") #post方法访问

print(response.status_code) #状态码

print(response.text)
