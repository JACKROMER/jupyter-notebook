#!/usr/bin/python
#coding=utf-8

'''
demo说明：使用output_stream_type为1的输出方式
注意：
    1.input_stream_list只能有两条可视输入，即音视频(input_type为0)、图片(2)、画布(3)、纯视频流(5)
    2.input_stream_list可以存在其他的音频流（总条数最多为16条）
    3.output_stream_id不存在于输入流id列表中
    4.output_stream_id不能是已存在的流id
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
        "mix_stream_template_id":10,
        "mix_stream_session_id" : "test_lewis_room_new",#修改为唯一的混流操作id
        "output_stream_id": "stream_lewis_new_1",#输出流id不在输入流id中
        "output_stream_type":1,
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
                    #模板10默认image_width为
                    #模板10默认image_height为
                    #模板10默认location_x为20
                    #模板10默认location_y为20
                    "image_layer": 2
                }
            }
               ]
    }}})
    print post(posturl,content)
