#!/usr/bin/python
#coding=utf-8

'''
demo说明：使用自定义位置参数（百分比）
注意：
    1.自定义位置参数，需检查画面是否会溢出背景画面
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
                    "image_layer": 1,#必填参数（纯音频也必须填）
                    # 背景流width和height参数可不填，不填默认使用原始流的width和height
                    "image_width":480,
                    "image_height":270
                }   
            },  
            {   
                "input_stream_id":"stream_lewis02",#修改为输入流2的id
                "layout_params":
                {
                    "image_layer": 2,
                    # 百分比建议范围0.01~0.99
                    # 若没有裁剪参数
                    # 显示的image_width = 百分比*流width
                    # 显示的image_height = 百分比*流height
                    # 有裁剪参数的情况，请参考demo_stream_crop.py
                    "image_width":0.3,
                    "image_height":0.3,
                    "location_x": 100,
                    "location_y": 0
                }
            }
               ]
    }}})
    print post(posturl,content)
