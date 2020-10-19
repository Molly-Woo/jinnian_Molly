import requests
import json

def getpicture():
    url = "http://47.102.118.1:8089/api/challenge/start/8b3e056e-3b03-4236-97d6-0da546b8dfc8"# 发送get请求
    data = {}
    data["teamid"] = 25
    data["token"] = "5da8346b-abca-4ec0-b490-8005e02599f4"
    res = requests.post(url=url, json=data)  # 发送post请求
    rest = json.loads(res.text)
    #r = requests.get(url)# 获取返回的json数据
    #rest = json.dumps(rest.json())
    return rest

def sendpicture(thepath , theswap , theuuid) :
    url = "http://47.102.118.1:8089/api/challenge/submit"

    answer = {}
    answer["operations"] = thepath
    answer["swap"] = theswap
    print (theswap)
    if theswap[0] == theswap[1] and theswap[0] == 0 :
        answer["swap"] = []
    data = {}
    data["uuid"] = theuuid
    data["teamid"] = 25
    data["token"] = "5da8346b-abca-4ec0-b490-8005e02599f4"
    data["answer"] = answer
    res = requests.post(url = url , json = data )#发送post请求
    print(res.text)
