{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "scrolled": true,
    "tags": [
     "MATH"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.4142135623730951"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#1 hahahah\n",
    "import math\n",
    "x = 2\n",
    "y = math.cos(x)\n",
    "z = math.sqrt(2)\n",
    "f = math.pow(2,19)\n",
    "f = math.pow(2,9)\n",
    "z\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {
    "tags": [
     "str"
    ]
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "aaa;bbb;ccc\n",
      "41.258\n",
      "2 + 3 = 6\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'hello 我'"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import math\n",
    "print('aaa','bbb','ccc',sep=';',end='\\n')\n",
    "\n",
    "a = 5.458\n",
    "# math 相关\n",
    "math.sin(a)\n",
    "math.cos(a)\n",
    "math.pow(2,3)\n",
    "x = math.pi\n",
    "y = math.log10(x)\n",
    "y\n",
    "m = math.ceil(x)\n",
    "m = -41.258\n",
    "print(math.fabs(m))\n",
    "x = math.fabs(m)\n",
    "\n",
    "big = 199 ** 99\n",
    "big\n",
    "\n",
    "# 0.9- (0.1 + 0.1 + 0.1  + 0.1  + 0.1  + 0.1  + 0.1  + 0.1  + 0.1)< 10 ** -9\n",
    "\n",
    "#字符串 \n",
    "# str = '''hello'''\n",
    "# str2 = \"\"\"hello2\"\"\"\n",
    "# str3 = 'abcd\\nsss'\n",
    "# str2\n",
    "# print(str2 + str3)\n",
    "\n",
    "# 字符串处理函数\n",
    "s = \"hello this is my name jackromer || HOW ARE || Y || OU\"\n",
    "# s = s.capitalize()\n",
    "# count = s.count('y')\n",
    "# index = s.find('yx')\n",
    "# flag = s.isalnum()\n",
    "# flag = s.isdigit()\n",
    "# # s = s.swapcase()\n",
    "# s = s.title()\n",
    "# slenth = len(s)\n",
    "\n",
    "# array = s.split('||',2)\n",
    "# print(array)\n",
    "\n",
    "# 整数\n",
    "0o24\n",
    "0x3f\n",
    "0b10100101\n",
    "\n",
    "a = 100\n",
    "a%b\n",
    "\n",
    "# 浮点数\n",
    "# .098\n",
    "# 19.\n",
    "# -2e3\n",
    "\n",
    "# int('78',base=10)\n",
    "\n",
    "# ss = '25'\n",
    "# ma = int(ss)\n",
    "# ma = ss.startswith('5')\n",
    "# ma\n",
    "\n",
    "r'abc\\asss'\n",
    "print('%d + %d = %d' %(2,3,6))\n",
    "wd = 'hello 我'\n",
    "utf8_wd = wd.encode('gb2312')\n",
    "decode_utf8_wd = utf8_wd.decode('gb2312')\n",
    "decode_utf8_wd\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    },
    "tags": [
     "list操作"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 3, 4]"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "li = []\n",
    "li\n",
    "for i in range(5):\n",
    "    li.append(i)\n",
    "li"
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
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
