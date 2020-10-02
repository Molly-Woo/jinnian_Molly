import requests
import json

def getpicture():
    url = "http://47.102.118.1:8089/api/problem?stuid=031802230"# 发送get请求
    r = requests.get(url)# 获取返回的json数据
    r = json.dumps(r.json())
    r = json.loads(r)
    return r

def sendpicture(thepath , theswap , theuuid) :
    import requests
    url = "http://47.102.118.1:8089/api/answer"
    anwser = {}
    anwser["operation"] = thepath
    anwser["theswap"] = theswap
    data = {}
    data["uuid"] = theuuid
    data["anwser"] = anwser
    json.dumps(data)
    #print(data)
    # 字符串格式
    res = requests.post(url=url, data=data)
    print(res.text)
