#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import requests
import json
import sys
import os
 
headers = {'Content-Type': 'application/json;charset=utf-8'}
api_url = "https://oapi.dingtalk.com/robot/send?access_token=a3b836895013157c419cc3148778f126580807bcc8cca626878d3ffa0e899085"
#api_url = "https://oapi.dingtalk.com/robot/send?access_token=25705a411b9b2fd1933254f522eaaccc9f834a708925265f69756831fe4d37c8"
 
def msg(text):
    json_text= {
     "msgtype": "text",
        "text": {
            "content": text
        },
        "at": {
            "atMobiles": [
                "1xxxxxxxxxxxxx"
            ],
            "isAtAll": False
        }
    }
    print requests.post(api_url,json.dumps(json_text),headers=headers).content
     
if __name__ == '__main__':
    text = sys.argv[1]
    msg(text)
