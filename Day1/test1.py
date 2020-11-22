import requests # 导入爬虫的库

response = requests.get("http://www.baidu.com") #生成一个response 对象
response.encoding = response.apparent_encoding #设置编码格式
print("状态码"+str(response.status_code)) #打印状态码
print(response.text)

