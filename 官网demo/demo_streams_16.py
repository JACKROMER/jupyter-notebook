#!/usr/bin/python
#coding=utf-8

'''
demo说明：16条音视频流混流
注意：
    1.对每条流分别设置location_x,location_y，所有画面才会完整显示，如果不设置，会出现所有画面叠在一起的情况
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
        "interface":{
        "interfaceName":"Mix_StreamV2",#固定值Mix_StreamV2
        "para":
        {
        "interface": "mix_streamv2.start_mix_stream_advanced",#固定值mix_streamv2.start_mix_stream_advanced
        "app_id":int(appid),
        "domain":"",
        "path":"",
        "mix_stream_template_id":0,
        "mix_stream_session_id" : "test_lewis_room",#修改为唯一的混流操作id
        #若不填写output_stream_type，则输出流id必须与一条输入流id相同
        #若output_stream_type为1，请参考demo_output_newly.py使用
        "output_stream_id": "stream_lewis01",
        "input_stream_list":[
            {
                "input_stream_id":"stream_lewis01",#修改为输入流1的id
                "layout_params":
                {   
                    "image_layer": 1 #必填参数（纯音频也必须填）
                }   
            },  
            {   
                "input_stream_id":"stream_lewis02",#修改为输入流2的id
                "layout_params":
                {
                    "image_layer": 2
                }
            },  
            {   
                "input_stream_id":"stream_lewis03",
                "layout_params":
                {
                    "image_layer": 3
                }
            },  
            {   
                "input_stream_id":"stream_lewis04",
                "layout_params":
                {
                    "image_layer": 4
                }
            },  
            {   
                "input_stream_id":"stream_lewis05",
                "layout_params":
                {
                    "image_layer": 5
                }
            },  
            {   
                "input_stream_id":"stream_lewis06",
                "layout_params":
                {
                    "image_layer": 6
                }
            },  
            {   
                "input_stream_id":"stream_lewis07",
                "layout_params":
                {
                    "image_layer": 7
                }
            },  
            {   
                "input_stream_id":"stream_lewis08",
                "layout_params":
                {
                    "image_layer": 8
                }
            },
            {
                "input_stream_id":"stream_lewis09",
                "layout_params":
                {   
                    "image_layer": 9
                }   
            },  
            {   
                "input_stream_id":"stream_lewis10",
                "layout_params":
                {
                    "image_layer": 10
                }
            },  
            {   
                "input_stream_id":"stream_lewis11",
                "layout_params":
                {
                    "image_layer": 11
                }
            },  
            {   
                "input_stream_id":"stream_lewis12",
                "layout_params":
                {
                    "image_layer": 12
                }
            },  
            {   
                "input_stream_id":"stream_lewis13",
                "layout_params":
                {
                    "image_layer": 13
                }
            },  
            {   
                "input_stream_id":"stream_lewis14",
                "layout_params":
                {
                    "image_layer": 14
                }
            },  
            {   
                "input_stream_id":"stream_lewis15",
                "layout_params":
                {
                    "image_layer": 15
                }
            },  
            {   
                "input_stream_id":"stream_lewis16",
                "layout_params":
                {
                    "image_layer": 16
                }
            }
               ]
    }}})
    print post(posturl,content)
