{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 函数"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello word.\n",
      "0\n",
      "2\n",
      "4\n",
      "6\n",
      "8\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[0, 2, 4, 6, 8]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def  hello():\n",
    "    print('hello word.')\n",
    "    lists = [iv for iv in range(10) if iv % 2 == 0]\n",
    "    for value in lists:\n",
    "        print(value)\n",
    "    return lists\n",
    "\n",
    "listresult = hello()\n",
    "listresult"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "please input a num>>>78\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "45"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def sumNums(n = 10):\n",
    "    result = 0;\n",
    "    for i in range(n):\n",
    "        result += i\n",
    "    return result\n",
    "n = int(input('please input a num>>>'));\n",
    "sumNums()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "哈哈 yes\n",
      "hahaha your name.\n"
     ]
    }
   ],
   "source": [
    "def hello(hi='nihao',name='yes'):\n",
    "    print(hi,name)\n",
    "hello('哈哈')\n",
    "hello('hahaha','your name.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n",
      "0\n",
      "(2, 3)\n"
     ]
    }
   ],
   "source": [
    "def changePara(*para,a,b=0):\n",
    "    print(a)\n",
    "    print(b)\n",
    "    print(para)\n",
    "changePara(2,3,a=9)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'c': 9, 'u': 10}\n",
      "333\n",
      "0\n"
     ]
    }
   ],
   "source": [
    "# dict para\n",
    "def changePara(a,b=0,**para):\n",
    "    print(para)\n",
    "    print(a)\n",
    "    print(b)\n",
    "changePara(333,c=9,u=10)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "729\n",
      "16384\n"
     ]
    }
   ],
   "source": [
    "def sums(a,b):\n",
    "    print(a**b)\n",
    "sums(*(3,6))\n",
    "sums(**{'a':4,'b':7})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['hahaha']\n",
      "['hahaha', 'hahaha']\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "def myfun(lst=[]):\n",
    "    global m;\n",
    "    m = 0;\n",
    "    m += 1\n",
    "    lst.append('hahaha')\n",
    "    print(lst)\n",
    "myfun()\n",
    "myfun()\n",
    "print(m)"
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
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
