import requests 

data = {
    "name":"xtt",
    "age":20
}

response = requests.get("http://httpbin.org/get",params=data) #get 传入参数

print(response.status_code) #状态码
print(response.text)
