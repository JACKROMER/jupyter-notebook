{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 文件和文件系统"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-01-22T06:17:50.294261Z",
     "start_time": "2019-01-22T06:17:50.287253Z"
    },
    "collapsed": true
   },
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'file' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-b52fea201080>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#open 函数\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m open(file,#filename\n\u001b[0m\u001b[0;32m      3\u001b[0m      \u001b[0mmode\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'r'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;31m#file open way\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m      \u001b[0mbuffering\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;31m#缓冲区大小\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m      \u001b[0mencoding\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;31m#file encode\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'file' is not defined"
     ]
    }
   ],
   "source": [
    "#open 函数\n",
    "open(file,#filename\n",
    "     mode='r',#file open way\n",
    "     buffering = -1,#缓冲区大小\n",
    "     encoding=None,#file encode\n",
    "     errors=None,#the way to process,when error ocous.\n",
    "     newline = None,#控制通用换行符模式的行为\n",
    "     closefd=True,#控制关闭文件时是否彻底关闭文件\n",
    "     opener=None)\n",
    "\n",
    "# mode：r w a b x + t  rt rb  wt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-01-22T06:49:01.946223Z",
     "start_time": "2019-01-22T06:49:01.940237Z"
    },
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "count: 1 111 111\n",
      "\n",
      "count: 2 222 222\n",
      "\n",
      "count: 3 333 333\n",
      "\n",
      "count: 4 444 444\n",
      "\n",
      "count: 5 555 555\n",
      "\n",
      "count: 6 666 666\n",
      "\n",
      "count: 7 777 777\n",
      "\n",
      "count: 8 888 888\n",
      "\n",
      "count: 9 999 999\n"
     ]
    }
   ],
   "source": [
    "def file_hal(name='python_test2.txt'):\n",
    "    with open(name) as f:#使用with语句管理文件的打开和关闭\n",
    "        count = 0\n",
    "        for line in f:\n",
    "            count += 1\n",
    "            print('count:',count,line.strip(),line)\n",
    "#         f.close()\n",
    "if __name__ == '__main__':\n",
    "    file_hal()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-01-22T07:01:16.133076Z",
     "start_time": "2019-01-22T07:01:16.126081Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "has read to 1 line > file filecommand/python_test2.txt line 1:\n",
      "111\n",
      "has read to 2 line > file filecommand/python_test2.txt line 2:\n",
      "222\n",
      "has read to 3 line > file filecommand/python_test2.txt line 3:\n",
      "333\n",
      "has read to 4 line > file filecommand/python_test2.txt line 4:\n",
      "444\n",
      "has read to 5 line > file filecommand/python_test2.txt line 5:\n",
      "555\n",
      "has read to 6 line > file filecommand/python_test2.txt line 6:\n",
      "666\n",
      "has read to 7 line > file filecommand/python_test2.txt line 7:\n",
      "777\n",
      "has read to 8 line > file filecommand/python_test2.txt line 8:\n",
      "888\n",
      "has read to 9 line > file filecommand/python_test2.txt line 9:\n",
      "999\n",
      "has read to 10 line > file filecommand/python_test.txt line 1:\n",
      "qqq\n",
      "has read to 11 line > file filecommand/python_test.txt line 2:\n",
      "www\n",
      "has read to 12 line > file filecommand/python_test.txt line 3:\n",
      "eee\n",
      "has read to 13 line > file filecommand/python_test.txt line 4:\n",
      "rrr\n",
      "has read to 14 line > file filecommand/python_test.txt line 5:\n",
      "ttt\n",
      "has read to 15 line > file filecommand/python_test.txt line 6:\n",
      "yyy\n",
      "has read to 16 line > file filecommand/python_test.txt line 7:\n",
      "uuu\n",
      "has read to 17 line > file filecommand/python_test.txt line 8:\n",
      "iii\n",
      "has read to 18 line > file filecommand/python_test.txt line 9:\n",
      "ooo\n",
      "has read to 19 line > file filecommand/python_test.txt line 10:\n",
      "ppp\n"
     ]
    }
   ],
   "source": [
    "## fileinput模块\n",
    "import fileinput\n",
    "def demo_fileinput():\n",
    "    with fileinput.input(['filecommand/python_test2.txt','filecommand/python_test.txt']) as lines:# 文件位置数组\n",
    "        for line in lines:\n",
    "            print('has read to %d line >'  % fileinput.lineno(),'file %s line %d:' % (fileinput.filename(),fileinput.filelineno()))\n",
    "            print(line.strip())\n",
    "if __name__ == '__main__':\n",
    "    demo_fileinput()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 常用文件和目录操作"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-01-22T07:42:24.448434Z",
     "start_time": "2019-01-22T07:42:24.442449Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "E:\\Python\\jupyter\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os\n",
    "print(os.getcwd())\n",
    "path = os.getcwd()\n",
    "os.listdir(path)#获取指定目录中的内容\n",
    "# os.mkdir('E:\\\\Python\\\\jupyter\\\\filecommand2') ##使用双斜杠\n",
    "# os.mkdir(path + '\\\\filecommand3')\n",
    "\n",
    "#删除目录\n",
    "# os.rmdir(path + '\\\\filecommand3')\n",
    "#判断是否是目录 os.path.isdir()\n",
    "# os.path.isdir(path + '\\\\filecommand2')\n",
    "os.path.isfile(path + '\\\\filecommand\\\\python_test.txt')\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-01-22T07:48:38.021904Z",
     "start_time": "2019-01-22T07:48:38.010897Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('E:\\\\Python\\\\jupyter', ['.ipynb_checkpoints', 'filecommand', 'filecommand2', 'ipynb', 'myproject', 'pydata', 'pyfile', '__pycache__'], ['python 函数.ipynb', 'python 匿名函数lambda.ipynb', 'PYTHON-CLASSES.ipynb', 'python-dict-字典.ipynb', 'python-if-else等控制语句执行流程.ipynb', 'python-list-tuple数组和元组.ipynb', 'python-math-str-字符串和math.ipynb', 'python-上下文管理器.ipynb', 'python-模块.ipynb', 'python-装饰器.ipynb', 'python-进阶.ipynb', 'python-迭代器iter-生成器-yield.ipynb', 'python-面向对象-继承-异常处理.ipynb', '文件和文件系统.ipynb'])\n",
      "('E:\\\\Python\\\\jupyter\\\\.ipynb_checkpoints', [], ['python 函数-checkpoint.ipynb', 'python 匿名函数lambda-checkpoint.ipynb', 'PYTHON-CLASSES-checkpoint.ipynb', 'python-dict-字典-checkpoint.ipynb', 'python-if-else等控制语句执行流程-checkpoint.ipynb', 'python-list-tuple数组和元组-checkpoint.ipynb', 'python-math-str-字符串和math-checkpoint.ipynb', 'python-上下文管理器-checkpoint.ipynb', 'python-模块-checkpoint.ipynb', 'python-装饰器-checkpoint.ipynb', 'python-进阶-checkpoint.ipynb', 'python-迭代器iter-生成器-yield-checkpoint.ipynb', 'python-面向对象-继承-异常处理-checkpoint.ipynb', '文件和文件系统-checkpoint.ipynb'])\n",
      "('E:\\\\Python\\\\jupyter\\\\filecommand', [], ['python_test.txt', 'python_test2.txt'])\n",
      "('E:\\\\Python\\\\jupyter\\\\filecommand2', [], [])\n",
      "('E:\\\\Python\\\\jupyter\\\\ipynb', [], [])\n",
      "('E:\\\\Python\\\\jupyter\\\\myproject', ['.ipynb_checkpoints', 'python_classes', 'python_data', 'python_function', '__pycache__'], ['__init__.py'])\n",
      "('E:\\\\Python\\\\jupyter\\\\myproject\\\\.ipynb_checkpoints', [], ['__init__.py-checkpoint.ipynb'])\n",
      "('E:\\\\Python\\\\jupyter\\\\myproject\\\\python_classes', ['__pycache__'], ['creature_person.py', '__init__.py'])\n",
      "('E:\\\\Python\\\\jupyter\\\\myproject\\\\python_classes\\\\__pycache__', [], ['__init__.cpython-37.pyc'])\n",
      "('E:\\\\Python\\\\jupyter\\\\myproject\\\\python_data', [], ['__init__.py'])\n",
      "('E:\\\\Python\\\\jupyter\\\\myproject\\\\python_function', [], ['__init__.py'])\n",
      "('E:\\\\Python\\\\jupyter\\\\myproject\\\\__pycache__', [], ['__init__.cpython-37.pyc'])\n",
      "('E:\\\\Python\\\\jupyter\\\\pydata', ['.ipynb_checkpoints'], ['lists.txt'])\n",
      "('E:\\\\Python\\\\jupyter\\\\pydata\\\\.ipynb_checkpoints', [], [])\n",
      "('E:\\\\Python\\\\jupyter\\\\pyfile', ['.ipynb_checkpoints', '__pycache__'], ['creature_person.py', 'creature_persons.py', 'python-面向对象-继承-异常处理.py', 'python_foofun.py', 'test.py', '未命名.ipynb'])\n",
      "('E:\\\\Python\\\\jupyter\\\\pyfile\\\\.ipynb_checkpoints', [], ['test-checkpoint.py', '未命名-checkpoint.ipynb'])\n",
      "('E:\\\\Python\\\\jupyter\\\\pyfile\\\\__pycache__', [], ['creature_person.cpython-37.pyc', 'creature_persons.cpython-37.pyc', 'python_foofun.cpython-37.pyc'])\n",
      "('E:\\\\Python\\\\jupyter\\\\__pycache__', [], ['creature_person.cpython-37.pyc', 'PYTHON_CLASSES.cpython-37.pyc'])\n"
     ]
    }
   ],
   "source": [
    "# 遍历目录下所有文件和目录\n",
    "import os\n",
    "path  = os.getcwd()\n",
    "files = os.walk(path)\n",
    "for i in files:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-01-22T09:28:10.577387Z",
     "start_time": "2019-01-22T09:28:10.570393Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "成功生成！\n"
     ]
    }
   ],
   "source": [
    "## 用文件名批量获取姓名和考号并导入到Excel中\n",
    "import os\n",
    "thispath = os.getcwd()\n",
    "filenames = []\n",
    "for a,b,files in os.walk(thispath + '\\\\filecommand2'):# 获取目录中的所有文件 \n",
    "    if files:\n",
    "        filenames.append([file[:-4] for file in files])#取文件名的第一个到倒数四个字符为文件名\n",
    "fname = 'testexam'\n",
    "for files in filenames:\n",
    "    f = open(thispath + '\\\\filecommand2\\\\' + fname + '.xls','w')\n",
    "    for name in files:\n",
    "        f.write(name[-3:] + '\\t' + name[:-3] + '\\n')\n",
    "    f.close()\n",
    "print('成功生成！')\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-01-22T09:35:53.593103Z",
     "start_time": "2019-01-22T09:35:51.212623Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the files in this E:\\Python\\jupyter will be renamed \n",
      "['python 函数.ipynb', 'python 匿名函数lambda.ipynb', 'PYTHON-CLASSES.ipynb', 'python-dict-字典.ipynb', 'python-if-else等控制语句执行流程.ipynb', 'python-list-tuple数组和元组.ipynb', 'python-math-str-字符串和math.ipynb', 'python-上下文管理器.ipynb', 'python-模块.ipynb', 'python-装饰器.ipynb', 'python-进阶.ipynb', 'python-迭代器iter-生成器-yield.ipynb', 'python-面向对象-继承-异常处理.ipynb', 'testexam0.xls', '文件和文件系统.ipynb']\n",
      "press y to continue.y\n",
      "ipynb_checkpoints\n",
      "filecommand\n",
      "filecommand2\n",
      "ipynb\n",
      "myproject\n",
      "pydata\n",
      "pyfile\n",
      "ipynb\n",
      "E:\\Python\\jupyter\\python 函数.ipynb\n",
      "E:\\Python\\jupyter\\filecommand2\\python 函数.py\n",
      "ipynb\n",
      "E:\\Python\\jupyter\\python 匿名函数lambda.ipynb\n",
      "E:\\Python\\jupyter\\filecommand2\\python 匿名函数lambda.py\n",
      "ipynb\n",
      "E:\\Python\\jupyter\\PYTHON-CLASSES.ipynb\n",
      "E:\\Python\\jupyter\\filecommand2\\PYTHON-CLASSES.py\n",
      "ipynb\n",
      "E:\\Python\\jupyter\\python-dict-字典.ipynb\n",
      "E:\\Python\\jupyter\\filecommand2\\python-dict-字典.py\n",
      "ipynb\n",
      "E:\\Python\\jupyter\\python-if-else等控制语句执行流程.ipynb\n",
      "E:\\Python\\jupyter\\filecommand2\\python-if-else等控制语句执行流程.py\n",
      "ipynb\n",
      "E:\\Python\\jupyter\\python-list-tuple数组和元组.ipynb\n",
      "E:\\Python\\jupyter\\filecommand2\\python-list-tuple数组和元组.py\n",
      "ipynb\n",
      "E:\\Python\\jupyter\\python-math-str-字符串和math.ipynb\n",
      "E:\\Python\\jupyter\\filecommand2\\python-math-str-字符串和math.py\n",
      "ipynb\n",
      "E:\\Python\\jupyter\\python-上下文管理器.ipynb\n",
      "E:\\Python\\jupyter\\filecommand2\\python-上下文管理器.py\n",
      "ipynb\n",
      "E:\\Python\\jupyter\\python-模块.ipynb\n",
      "E:\\Python\\jupyter\\filecommand2\\python-模块.py\n",
      "ipynb\n",
      "E:\\Python\\jupyter\\python-装饰器.ipynb\n",
      "E:\\Python\\jupyter\\filecommand2\\python-装饰器.py\n",
      "ipynb\n",
      "E:\\Python\\jupyter\\python-进阶.ipynb\n",
      "E:\\Python\\jupyter\\filecommand2\\python-进阶.py\n",
      "ipynb\n",
      "E:\\Python\\jupyter\\python-迭代器iter-生成器-yield.ipynb\n",
      "E:\\Python\\jupyter\\filecommand2\\python-迭代器iter-生成器-yield.py\n",
      "ipynb\n",
      "E:\\Python\\jupyter\\python-面向对象-继承-异常处理.ipynb\n",
      "E:\\Python\\jupyter\\filecommand2\\python-面向对象-继承-异常处理.py\n",
      "xls\n",
      "__pycache__\n",
      "ipynb\n",
      "E:\\Python\\jupyter\\文件和文件系统.ipynb\n",
      "E:\\Python\\jupyter\\filecommand2\\文件和文件系统.py\n",
      "rename E:\\Python\\jupyter ipynb to py end.\n"
     ]
    }
   ],
   "source": [
    "# 批量重命名，且复制文件到指定目录中去\n",
    "import os\n",
    "import shutil\n",
    "perfix = 'ipynb'\n",
    "path = os.getcwd()\n",
    "#友好提示\n",
    "print('the files in this %s will be renamed ' % os.getcwd())\n",
    "allfiles = os.listdir(path)\n",
    "print([f for f in allfiles if os.path.isfile(f)])# 输出所有文件的名字不包括文件夹\n",
    "inputs = input('press y to continue.')\n",
    "if inputs.lower() != 'y':\n",
    "    exit()\n",
    "\n",
    "\n",
    "filenames = os.listdir(path)#获取当前目录中的内容\n",
    "for file in filenames:\n",
    "    t = file.split('.')\n",
    "    realname = t[0]#文件名\n",
    "    endfix = t[-1]#文件后缀\n",
    "    print(endfix)\n",
    "    if endfix == perfix and os.path.isfile(file):\n",
    "        oldname= path + \"\\\\\" + file\n",
    "        print(oldname)\n",
    "        newname= path + \"\\\\filecommand2\\\\\" + realname+ \".py\"\n",
    "        print(newname)\n",
    "        shutil.copyfile(oldname,newname)\n",
    "print('rename %s ipynb to py end.' % path)\n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
