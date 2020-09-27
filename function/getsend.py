import requests
import json

def getpicture():
    url = "http://47.102.118.1:8089/api/problem?stuid=031802230"# 发送get请求
    r = requests.get(url)# 获取返回的json数据
    r = json.dumps(r.json())
    r = json.loads(r)
    return r