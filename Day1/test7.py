import requests 

data = {
    "name":"xtt",
    "age":20
}

response = requests.post("http://httpbin.org/post",params=data) #get 传入参数

print(response.status_code) #状态码
print(response.text)
