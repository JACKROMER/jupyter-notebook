#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import urllib.request
import os
import re

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')
    response = urllib.request.urlopen(req,timeout=90)
    return response.read()

# 获取page页码 1........9
def get_page(url):
    html = url_open(url).decode('utf-8')
#     print(html)
#   https://image.baidu.com/
    pattern = r'href="([^"]*)"[^>]*>.+?' # 匹配href
    uuidArr = re.findall(pattern, html)
    uuidArrf = []
    for id in uuidArr:
        idstr = str(id)
        if idstr.find('?classid') != -1 : #筛选页码地址
            uuidArrf.append(idstr)
    print("最终页面pageId", uuidArrf)
    return uuidArrf

# 获取图片链接
def find_page(page_url):
#     src="//scpic.chinaz.net/Files/pic/pic9/202011/apic29096_s.jpg"
    pattern = r'href="([^"]*)"[^>]*>.+?' # 匹配href
    html = url_open(page_url).decode('utf-8')
#     print(html)
    img_addrs = re.findall(pattern,html)
    imgFarr = []
    for h in img_addrs :
        x = str(h)
        if x.find("stype=") != -1 :
            print("find one url", x)
            imgFarr.append(x)
    print("图片所在页面数组：" ,imgFarr)
    return imgFarr

# 获取图片链接
def find_vo(page_url):
#     src="//scpic.chinaz.net/Files/pic/pic9/202011/apic29096_s.jpg"
    pattern = r'src="([^"]*)"[^>]*>.+?' # 匹配href
    html = url_open(page_url).decode('utf-8')
    video_addrs = re.findall(pattern,html)
    #https://tutu.94zzh.com/d9/4281/428110-1.jpg
    imgFarr = []
    for h in video_addrs :
        x = str(h)
        if x.find("tutu") != -1 :
            print("find one pic", x)
            imgFarr.append(x)
    print("此页面图片数组：" ,imgFarr)
    save_imgs(imgFarr) #保存图片
            
                
# 保存图片到文件夹
def save_imgs(img_addrs):
    dirname ="wodexiazai"
    makeDir(str(dirname))
    os.chdir(str(dirname))
    for i in img_addrs:
        purlstr = str(i)
        print("下载图片地址：", purlstr)
        b = purlstr.split('/')
        filename = b[-1]
        image = url_open(purlstr)
        with open(filename,'wb') as f:
            f.write(filename)
            f.close()
            print("写入完成",purlstr)

def makeDir(folder):
    if os.path.exists(folder) :
        print(folder + "文件夹已存在")
        pass
    try:
        os.mkdir(folder)
    except OSError:
        pass
    
def download_mm(folder='ooxx',pages=10):
    print(folder)
    makeDir(folder) #新建文件夹
    os.chdir(folder) #跳转到文件夹
    folder_top = os.getcwd() #获取当前工作目录
#     url = 'https://sc.chinaz.com/tupian/meinvxiezhen_3.html'
    baseurl='https://www.a8e0e744fa9b81a7.com/piclist.x'
    url = 'https://www.a8e0e744fa9b81a7.com/piclist.x?classid=6'
    page_num = get_page(url) #获取网页最新的地址
    print(page_num)
    for page_id in page_num:
        print("页面URL：", page_id)
        page_url = baseurl + page_id #组合网页地址
        print("页面地址：", page_url)
        img_addrs = find_imgs(page_url) #获取图片地址
        # 进入页面找到播放地址
        for p in img_addrs:
            print("准备进入单个页面下载图片",baseurl + p)
            find_vo("https://www.a8e0e744fa9b81a7.com/" + p)
#             https://www.a8e0e744fa9b81a7.com/piclist.x?classid=7

if __name__ == '__main__':
    folder = input("Please enter a folder(default is 'ooxx'): " )
    pages = input("How many pages do you wan to download(default is 10): ")
    download_mm(str(folder),int(pages))


# In[22]:


import re

html = '<a href="/tag/qiaotun/index_2.html">2</a>'
pattern = r'href="([^"]*)"[^>]*>.+?' # 匹配href
print(re.findall(pattern,html))
pattern2 = r'src="([^"]*)"+?'
html2 ='<a href="/xinggan/21610.html" title="PartyCat轰趴猫 风骚翘臀少妇浴室性感蕾丝内衣摄影图片" target="_blank"><img src="https://xintu.crmvscrm.com/d/file/t/20201130/10/4ai2bpnkhlk.jpg" data-original="https://xintu.crmvscrm.com/d/file/t/20201130/10/4ai2bpnkhlk.jpg" alt="PartyCat轰趴猫 风骚翘臀少妇浴室性感蕾丝内衣摄影图片" style="display: inline;"></a>'
print(re.findall(pattern2,html2))
a = 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3075027813,1435505077&amp;fm=26&amp;gp=0.jpg'
b = a.split('/')
print(b[3])
mm = '/search/index?ct=201326592&amp;'
print(mm[17:30])


# In[30]:


print('/tag/qiaotun/index_2.html'.find('tag/qiaotun'))

