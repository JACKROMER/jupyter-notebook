#!/usr/bin/python
#coding=utf-8

'''
demo说明：使用裁剪功能
注意：
    1.裁剪出的画面不能溢出原始画面
    2.裁剪与缩放都存在时，先裁剪出需要大小的画面，再缩放到指定长宽
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
                "input_stream_id":"canvas1",#填写画布id
                "layout_params":
                {   
                    "image_layer": 1,
                    "input_type":3,
                    "color":"0x000000",
                    # 若画布作为背景不指定宽高
                    # 则使用image_layer最小的流的宽高，作为画布的宽高
                    "image_height":540,
                    "image_width":960
                }   
            },  
            {   
                "input_stream_id":"stream_lewis01",#修改为输入流1的id
                "layout_params":
                {
                    "image_layer": 2,#必填参数（纯音频也必须填）
                    "image_width":480,
                    "image_height":200,
                    "location_x":0,
                    "location_y":0
                },
                "crop_params":
                {
                    # 确定crop_width+crop_x小于输入流的width
                    # 确定crop_height+crop_y小于输入流的height
                    "crop_width":200, #裁剪后的宽度
                    "crop_height":200,#裁剪后的高度
                    "crop_x":240,     #裁剪的x轴坐标
                    "crop_y":0        #裁剪的y轴坐标
                }
            },
            {   
                "input_stream_id":"stream_lewis02",#修改为输入流2的id
                "layout_params":
                {
                    "image_layer": 3,
                    "image_width":480,
                    "image_height":200,
                    "location_x":480,
                    "location_y":0
                },
                "crop_params":
                {
                    "crop_width":200,
                    "crop_height":200,
                    "crop_x":240,
                    "crop_y":0
                }
            }
    ]
    }}})
    print post(posturl,content)
