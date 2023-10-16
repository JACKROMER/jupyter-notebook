#!/usr/bin/python
#coding=utf-8

'''
demo说明：使用mix_streamv2.cancel_mix_stream接口取消混流
注意：
    1.不需要填写input_stream_list
'''

import urllib
import urllib2
import json
import hashlib
import time
import random

#需要用户修改appid以及key
appid = "XXX"
key = "xxxxxxx"

#计算sign值，t表示请求的过期时间，在当前时间基础上+60s偏移
t = str(int(time.time())+60)
key_t = "%s%s"%(key,t)# 字符串拼接
sign = hashlib.md5(key_t).hexdigest()

# 随机数，作为event id,范围无要求，demo中的范围仅用作演示
event_id=random.randint(10000000, 2100000000)

def post(url,data):
    req = urllib2.Request(url)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req,data)
    return response.read()

if '__main__' == __name__:
    posturl = "http://fcgi.video.qcloud.com/common_access?appid=%s&interface=Mix_StreamV2&sign=%s&t=%s"%(appid,sign,t)
    content = json.dumps({
        "timestamp":int(time.time()),#当前时间戳
        "eventId":event_id,
        "interface":
        {
        "interfaceName":"Mix_StreamV2",#固定值Mix_StreamV2
        "para":
            {
                "interface": "mix_streamv2.cancel_mix_stream",
                "app_id":int(appid),
                "domain":"",
                "path":"",
                "mix_stream_template_id":0,
                "mix_stream_session_id" : "test_lewis_room",#修改为需要取消的session id
                "output_stream_id": "stream_lewis01",# 修改为需要取消的session中输出流id
            }
        }})
    print post(posturl,content)

