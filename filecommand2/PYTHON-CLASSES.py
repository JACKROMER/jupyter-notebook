{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "zhoudrinkmilk\n"
     ]
    }
   ],
   "source": [
    "# 生物类\n",
    "class Creature(object):\n",
    "    def __init__(self,name='',size=0, color='yello'):\n",
    "        self.name = name\n",
    "        self.size = size\n",
    "        self.color = color\n",
    "        \n",
    "    def eat(self,food):\n",
    "        print(self.name + 'eat' + food)\n",
    "\n",
    "# human 人类\n",
    "class Person(Creature):\n",
    "    def __init__(self,name,size,color,age=18):\n",
    "        super(Person,self).__init__()\n",
    "        self.name = name\n",
    "        self.size = size\n",
    "        self.age = age\n",
    "        self.color = color\n",
    "        \n",
    "    def eat(self,food):\n",
    "        print(self.name + 'eat' + food)\n",
    "        \n",
    "    def drink(self,drink):\n",
    "        print(self.name + 'drink' + drink)\n",
    "\n",
    "p = Person(name='zhou',size=15,color='yellow',age=18)\n",
    "p.drink('milk')\n",
    "        "
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
