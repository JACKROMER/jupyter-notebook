#!/usr/bin/python
#coding=utf-8

'''
demo说明：pk场景
注意：
    1.示例为双人pk
'''

import urllib
import urllib2
import json
import hashlib
import time
import random

#需要用户修改appid以及key
appid = "1255516392"
key = "cee491af9d286ff3d3ca3ec6a1d2d621"

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
        "mix_stream_template_id":390,
        "mix_stream_session_id" : "szpc_77_playUrl",#修改为唯一的混流操作id
        #若不填写output_stream_type，则输出流id必须与一条输入流id相同
        #若output_stream_type为1，请参考demo_output_newly.py使用
        "output_stream_id": "szpc_77_playUrl",
        "input_stream_list":[
        {
                "input_stream_id":"canvas1",#修改为画布的id
                "layout_params":
                {   
                    # image_layer为1的作为混流的背景
                    # 若画布不指定宽高, 则使用image_layer最小的流的宽高，作为画布的宽高
                    "image_layer": 1,
                    "input_type":3,
                    "image_width":400,
                    "image_height":640,
                    "color":"0x000000"
                }
            },   
            {   
                "input_stream_id":"1400321747_77_180_main",#修改为输入流2的id
                "layout_params":
                {
                    #模板默认image_width和image_height与背景流宽、高，该流原始宽、高等因素相关，以下说明为大致值，并不完全准确
                    #模板390小画面1默认image_width为背景width/2
                    #模板390小画面1默认image_height为背景height/2
                    #模板390小画面1默认location_x为20
                    #模板390小画面1默认location_y为(背景height-流height)/2
                    "image_layer": 2
                }
            },  
            {   
                "input_stream_id":"1400321747_77_1_main",#修改为输入流3的id
                "layout_params":
                {
                    #模板默认image_width和image_height与背景流宽、高，该流原始宽、高等因素相关，以下说明为大致值，并不完全准确
                    #模板390小画面2默认image_width为背景width/2
                    #模板390小画面2默认image_height为背景height/2
                    #模板390小画面2默认location_x为背景width-流width
                    #模板390小画面2默认location_y为(背景height-流height)/2
                    "image_layer": 3
                }
            }
               ]
    }}})
    print post(posturl,content)
