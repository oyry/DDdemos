import requests
import json
from Loginfo import log

logging = log.get_logger()
def change_type(value):

    try:
        if isinstance(eval(value), str):
            return value
        if isinstance(eval(value), dict):
            result = eval(json.dumps(value))
            return result
    except:
        logging.error("类型问题")

def api(method,url,querystring,data,header):

    global results
    try:
        if method == ("post" or "POST"):
            results = requests.post(url=url,params=querystring,data=data,headers=header,timeout=8,verify=False)
        if method == ("get" or "GET"):
            results = requests.get(url=url,params=querystring,data=data,headers=header,timeout=8,verify=False)
        response = results.json()
        code = response.get("code")
        return code
    except:
        logging.error("service is error")


def content(method,url,querystring,data,header):

    global results
    try:
        if method == ("post" or "POST"):
            results = requests.post(url=url,params=querystring,data=data,headers=header,timeout=8,verify=False)
        if method == ("get" or "GET"):
            results = requests.get(url=url,params=querystring,data=data,headers=header,timeout=8,verify=False)
        response = results.json()
        message = response.get("message")
        result = response.get("result")
        content = {"message": message, "result": result}
        return content
    except:
        logging.error("请求失败")