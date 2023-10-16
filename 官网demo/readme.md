# 1.运行环境
python 2.6.6
# 2. 名词含义
|名词|含义|
|:-:|:-:|
|stream|音视频流|
|video|纯视频流|
|audio|纯音频流|
|canvas|画布|
|picture|图片|
# 3.demo列表
|文件名|演示的功能|
|-|-|
|demo_audio.py|纯音频混流|
|demo_audio_16.py|最大16条纯音频混流|
|demo_audio_and_canvas.py|1纯音频+1画布混流|
|demo_cancel_output_newly.py|取消混流输出新流类型的混流(A+B->C)|
|demo_cancel_output_overly.py|取消混流输出叠加流类型的混流(A+B->A)|
|demo_cancel.py|取消混流（使用取消混流接口|
|demo_output_newly.py|输出流为新流类型的混流(A+B->C)|
|demo_position_percent_1.py|输入流参数中长、宽参数为百分比|
|demo_position_percent_2.py|输入流参数中location x、y坐标为百分比|
|demo_position_pixel.py|输入流参数中长、宽参数为像素|
|demo_stream1_and_audio15.py|1音视频+15纯音频混流| 
|demo_streams_16.py|最大16条音视频混流|
|demo_stream_and_audio.py|1音视频+1纯音频混流|
|demo_stream_and_canvas.py|1画布+2音视频混流|
|demo_stream_and_picture.py|1音视频+1图片混流|
|demo_stream_and_video.py|1音视频+1纯视频混流|
|demo_stream_crop.py|带有裁剪参数的音视频混流|
|demo_template_10.py|使用模板10混流|
|demo_template_20.py|使用模板20混流|
|demo_template_30.py|使用模板30混流|
|demo_template_310.py|使用模板310混流| 
|demo_template_390.py|使用模板390混流| 
|demo_template_391.py|使用模板391混流| 
|demo_template_40.py|使用模板40混流|
|demo_template_410.py|使用模板410混流| 
|demo_template_50.py|使用模板50混流|
|demo_template_510.py|使用模板510混流| 
|demo_template_590.py|使用模板590混流| 
|demo_template_610.py|使用模板610混流| 
|demo_template_610_canvas.py|使用模板610混流，其中一条输入为画布|
|demo_template_and_position.py|使用模板同时使用自定义参数的情况|
# 4.常见错误码及排查建议
|错误码|原因|排查建议|
|--|----|--------|
|-1|解析输入参数错误|检查请求体body json格式是否正确 <br>检查interface name是否为mix_streamv2.start_mix_stream_advanced<br>检查input_stream_list是否为空|
|-2|输入参数错误|检查appid、eventid是否为0<br>未设置模板，检查画面参数是否溢出|
|-3|流数目错误|检查输入流数目是否在[1，16]范围内|
|-4|流参数错误|检查输入输出长宽在（0，3000）范围内<br>检查输入流数目是否在（0,16]范围内<br>检查输入流是否携带layout_params<br>检查input_type是否支持（合法数值：0，2，3，4，5）<br>检查流id长度是否满足（1，80）|
|-11|图层错误|检查图层个数与输入流个数是否一致<br>检查图层id是否重复<br>检查图层id是否在（0，16]之间|
|-20|输入参数与接口不匹配|检查输入流条数是否匹配模板id<br>检查颜色参数是否正确|
|-21|混流输入流条数错误|检查输入流的条数是否至少为两条|
|-28|获取背景长宽失败|如果设置画布，检查画布的长宽是否设置<br>检查背景流是否存在（推流后需等待5s再混流）|
|-29|裁剪参数错误|检查裁剪位置是否超出流的长宽|
|-33|水印图片id错误|检查输入图片id是否设置|
|-34|获取水印图片url失败|检查图片是否上传成功，是否已经生成url|
|-300|输出流id已经被使用|检查当前输出流是否已经是另一个混流的输出流|
|-505|输入流无法在upload查到|重新推流后再试|
|-507|流长宽参数查询失败|检查画布宽、高是否设置<br>检查推流是否已经成功，建议推流后5s再开始混流|
|-508|输出流id错误|检查是否存在同样sessionid使用不同输出流id的情况|
|-10031|触发混流失败|建议推流后等待5s再混流|
|-30300<br>-31001<br>-31002|取消混流时sessionid不存在|检查输入流是否都已断开|
|-31003|取消混流时输出流id与session中输出流id不匹配|检查取消混流时填入的输出流id|
|-31004|输出流码率不合法|检查输出流码率是否在[1，50000]|