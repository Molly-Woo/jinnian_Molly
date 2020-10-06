import requests
import json

def getpicture():
    url = "http://47.102.118.1:8089/api/problem?stuid=031802230"# 发送get请求
    r = requests.get(url)# 获取返回的json数据
    r = json.dumps(r.json())
    r = json.loads(r)
    return r

def sendpicture(thepath , theswap , theuuid) :
    url = "http://47.102.118.1:8089/api/answer"

    answer = {}
    answer["operations"] = thepath
    answer["swap"] = theswap

    data = {}
    data["uuid"] = theuuid
    data["answer"] = answer
    print(json.dumps(data) )
    # 字符串格式
    res = requests.post(url = url , json = data )
    print(res.text)
