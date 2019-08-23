{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## python-进阶"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "### 函数和命名空间"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2018-12-03T09:35:20.919105Z",
     "start_time": "2018-12-03T09:35:20.915107Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "bar fun \n",
      "current module\n",
      "foo fun\n",
      "Foo module\n",
      "foo fun\n",
      "Foo module\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "#在module的path中临时添加指定的python文件目录，防止引入文件报错\n",
    "sys.path.append('E:\\Python\\jupyter\\pyfile')\n",
    "from python_foofun import foofun\n",
    "\n",
    "name = 'current module'\n",
    "def bar():\n",
    "    print('bar fun ')\n",
    "    print(name)\n",
    "    \n",
    "def call_foofun(fun):\n",
    "    fun()\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    bar()\n",
    "    foofun()\n",
    "    call_foofun(foofun)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 闭包及应用"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2018-12-03T09:40:08.032343Z",
     "start_time": "2018-12-03T09:40:08.028330Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x is  3\n"
     ]
    }
   ],
   "source": [
    "x = 15\n",
    "def foo():\n",
    "    x =3\n",
    "    def bar():\n",
    "        print('x is ',x)\n",
    "    bar()\n",
    "    \n",
    "if __name__ == '__main__':\n",
    "    foo()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2018-12-03T09:40:26.459892Z",
     "start_time": "2018-12-03T09:40:26.456895Z"
    }
   },
   "source": [
    "## 闭包和延迟求值"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2018-12-03T09:49:09.466403Z",
     "start_time": "2018-12-03T09:49:09.461401Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "返回求和函数并不求和\n",
      "调用求和\n",
      "17\n"
     ]
    }
   ],
   "source": [
    "def delay_fun(x,y):\n",
    "    def caculator():\n",
    "        return x + y\n",
    "    return caculator\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    print('返回求和函数并不求和')\n",
    "    msum = delay_fun(9,8)\n",
    "    print('调用求和')\n",
    "    re = msum()\n",
    "    print(re)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 闭包和泛型函数"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2018-12-03T09:51:43.618963Z",
     "start_time": "2018-12-03T09:51:43.613977Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "13\n",
      "70\n"
     ]
    }
   ],
   "source": [
    "def line(a,b):\n",
    "    def aline(x):\n",
    "        return a * x + b\n",
    "    return aline\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    line23 = line(2,3)\n",
    "    line230 = line(20,30)\n",
    "    print(line23(5))\n",
    "    print(line230(2))"
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
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
