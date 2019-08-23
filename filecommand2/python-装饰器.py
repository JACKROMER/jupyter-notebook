{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## python装饰器"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-01-21T09:35:31.979019Z",
     "start_time": "2019-01-21T09:35:31.975009Z"
    }
   },
   "outputs": [],
   "source": [
    "# 定义装饰器 \n",
    "def demo_decorater(fun):\n",
    "    def new_fun(*args,**kwargs):\n",
    "        print('start do something.')\n",
    "        fun(*args,**kwargs)\n",
    "        print('end do something.')\n",
    "    return new_fun\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-01-21T09:35:24.814870Z",
     "start_time": "2019-01-21T09:35:24.809860Z"
    }
   },
   "outputs": [],
   "source": [
    "# 定义装饰器 (带参数)\n",
    "def demo_decoraterPara(action):\n",
    "    def demo_decorater(fun):\n",
    "        def new_fun(*args,**kwargs):\n",
    "            print('start do something.',action)\n",
    "            fun(*args,**kwargs)\n",
    "            print('end do something.',action)\n",
    "        return new_fun\n",
    "    return demo_decorater"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2018-12-03T03:42:43.418745Z",
     "start_time": "2018-12-03T03:42:43.413749Z"
    },
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "start do something. hello you ok ?\n",
      "4 5\n",
      "end do something. hello you ok ?\n",
      "start do something.\n",
      "jajajja\n",
      "end do something.\n"
     ]
    }
   ],
   "source": [
    "# 调用装饰器\n",
    "@demo_decoraterPara('hello you ok ?')\n",
    "def test(x,y):\n",
    "    print(x,y)\n",
    "\n",
    "@demo_decorater\n",
    "def test2(name):\n",
    "    print(name)\n",
    "    \n",
    "if __name__ == '__main__':\n",
    "    test(4,5)\n",
    "    test2('jajajja')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2019-01-21T09:35:37.831981Z",
     "start_time": "2019-01-21T09:35:37.825985Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "0\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "# 装饰类\n",
    "def abc(myclass):\n",
    "    class innerclass:\n",
    "        def __init__(self,z=2):\n",
    "            self.z = z\n",
    "            self.wrapper = myclass()\n",
    "        def position(self):\n",
    "            self.wrapper.position()\n",
    "            print(self.z)\n",
    "    return innerclass\n",
    "\n",
    "@abc\n",
    "class coordination:\n",
    "    def __init__(self,x=0,y=0):\n",
    "        self.x = x\n",
    "        self.y = y\n",
    "    def position(self):\n",
    "        print(self.x)\n",
    "        print(self.y)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    coor = coordination()\n",
    "    coor.position()\n"
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
