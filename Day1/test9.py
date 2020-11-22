import requests

url = "http://www.baidu.com"

response = requests.get(url)

response.encoding = "utf-8" #设置接受编码的格式

print("\nr的类型"+str(type(response)))
print("\n状态码是:"+str(response.status_code))
print("\n头部信息:"+str(response.headers))
print("\n响应内容:")

print(response.text)

#保存文件
file = open("爬虫/1.txt","w",encoding="utf") #打开一个文件,w是文件不存在则新建一个文件,这里不用wb是因为不用保存成二进制

file.write(response.text)

file.close()
