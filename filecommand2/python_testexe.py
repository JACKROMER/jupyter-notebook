#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 批量重命名，且复制文件到指定目录中去
import os
import shutil #文件复制操作
# import py2exe 

perfix = 'ipynb'
path = os.getcwd()
#友好提示
print('the files in this %s will be renamed ' % os.getcwd())
allfiles = os.listdir(path)
print([f for f in allfiles if os.path.isfile(f)])# 输出所有文件的名字不包括文件夹
inputs = input('press y to continue.')
renamefile = input('please input the filename you want to rename and move.')
if inputs.lower() != 'y':
    exit()

oldname = path + "\\" + renamefile + '.ipynb'#需要命名的文件
if os.path.exists(oldname):
    newname = path + "\\filecommand2\\" + renamefile+ ".py" ## 需要生成的文件
    shutil.copyfile(oldname,newname)
    print('rename %s to py end.' % oldname)
else:
    print('file %s is not here.' % oldname)
    exit()

