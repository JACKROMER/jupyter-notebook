{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 迭代器"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2018-11-30T01:57:25.913748Z",
     "start_time": "2018-11-30T01:57:25.908751Z"
    },
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "4\n",
      "6\n",
      "8\n"
     ]
    }
   ],
   "source": [
    "class Counter(object):\n",
    "    def __init__(self,x = 0):\n",
    "        self.x =x\n",
    "counter = Counter()\n",
    "def useIter():\n",
    "    counter.x += 2\n",
    "    return counter.x\n",
    "for i in iter(useIter,10):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2018-11-30T02:31:06.134713Z",
     "start_time": "2018-11-30T02:31:06.125719Z"
    },
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "5\n",
      "0\n",
      "2\n",
      "9\n",
      "0\n",
      "2\n",
      "9\n",
      "('A', 'B')\n",
      "('A', 'C')\n",
      "('A', 'D')\n",
      "('B', 'A')\n",
      "('B', 'C')\n",
      "('B', 'D')\n",
      "('C', 'A')\n",
      "('C', 'B')\n",
      "('C', 'D')\n",
      "('D', 'A')\n",
      "('D', 'B')\n",
      "('D', 'C')\n",
      "('X', 'Y')\n",
      "('X', 'Z')\n",
      "('Y', 'Z')\n"
     ]
    }
   ],
   "source": [
    "import itertools as it\n",
    "for i in it.count(1,4):\n",
    "    print(i)\n",
    "    if(i > 4):\n",
    "        break\n",
    "list2 = [i for i in range(10)]\n",
    "lists = list(it.repeat(5,4))\n",
    "# 根据[1,[],True,3] 迭代1 2 3 4 数组，True/false代表是否需要迭代该值\n",
    "list(it.compress([1,2,3,4],[0,False,False,0]))\n",
    "# 条件为假时开始迭代 即X<6出现时迭代\n",
    "list(it.dropwhile(lambda x:x>6,[8,9,1,2,8,9]))\n",
    "# 条件为真时开始迭代 即X>1出现时开始迭代，到x<=1出现时候结束\n",
    "list(it.takewhile(lambda x:x>1,[8,9,3,1,0,2,8,9]))\n",
    "# 重复迭代\n",
    "for x in it.tee([0,2,9],2):\n",
    "    for isx in x:\n",
    "        print(isx)\n",
    "# 迭代序列排列组合\n",
    "for per in it.permutations('ABCD',2):\n",
    "#     for ol in per:\n",
    "    print(per)\n",
    "    \n",
    "for per in it.combinations('XYZ',2):\n",
    "#     for ol in per:\n",
    "    print(per)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 生成器yield"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2018-11-30T02:57:14.848109Z",
     "start_time": "2018-11-30T02:57:14.842113Z"
    },
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "start yield\n",
      "one\n",
      "yield end\n",
      "start yield\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 生成器也是一个函数\n",
    "def  myYield(n):\n",
    "    while n > 0 :\n",
    "        print('start yield')\n",
    "        yield n\n",
    "        print('yield end')\n",
    "        n -= 1\n",
    "# if __name__ == '__main__':\n",
    "#     for i in myYield(2):\n",
    "#         print(i)\n",
    "myy = myYield(10)\n",
    "myy.__next__()\n",
    "print('one')\n",
    "myy.__next__()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2018-11-30T03:03:55.339962Z",
     "start_time": "2018-11-30T03:03:55.335952Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 3, 4, 5]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = (i for i in range(6))\n",
    "a\n",
    "type(a)\n",
    "list(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2018-11-30T03:05:56.961351Z",
     "start_time": "2018-11-30T03:05:56.955356Z"
    },
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "start yield\n",
      "yield end\n",
      "start yield\n",
      "yield end\n",
      "start yield\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 生成器也是一个函数\n",
    "def  myYield(n):\n",
    "    while n > 0 :\n",
    "        print('start yield')\n",
    "        rcv = yield n\n",
    "        print('yield end')\n",
    "        n -= 1\n",
    "        if rcv is not None:\n",
    "            n = rcv\n",
    "# if __name__ == '__main__':\n",
    "#     for i in myYield(2):\n",
    "#         print(i)\n",
    "myy = myYield(2)\n",
    "myy.__next__()\n",
    "myy.send(5)\n",
    "myy.__next__()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 生成器和协程"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2018-11-30T03:25:40.860842Z",
     "start_time": "2018-11-30T03:25:40.854845Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "waiting process...\n",
      "send a process  0\n",
      "recieve a process ,and do it >  0\n",
      "send a process  1\n",
      "recieve a process ,and do it >  1\n",
      "send a process  2\n",
      "recieve a process ,and do it >  2\n"
     ]
    }
   ],
   "source": [
    "# 生产者 消费者\n",
    "def consumer():\n",
    "    print('waiting process...')\n",
    "    while True:\n",
    "        data = (yield)\n",
    "        data2 = (yield)\n",
    "        print('recieve a process ,and do it > ', data)\n",
    "    \n",
    "def producer():\n",
    "    c = consumer()\n",
    "    c.__next__()\n",
    "    for i in range(3):\n",
    "        print('send a process ',i)\n",
    "        c.send(i)\n",
    "# 先初始化生产者再初始化消费者\n",
    "if __name__ == '__main__':\n",
    "    producer()\n",
    "        "
   ]
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
   "toc_window_display": true
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
