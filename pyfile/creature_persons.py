#!/usr/bin/env python
# coding: utf-8

# In[5]:


# 生物类
class Creature(object):
    def __init__(self,name='',size=0, color='yello'):
        self.name = name
        self.size = size
        self.color = color
        
    def eat(self,food):
        print(self.name + ' eat ' + food)

# human 人类
class Person(Creature):
    def __init__(self,name,size,color,age=18):
        super(Person,self).__init__()
        self.name = name
        self.size = size
        self.age = age
        self.color = color
        
    def eat(self,food):
        print(self.name + ' eat ' + food)
        
    def drink(self,drink):
        print(self.name + ' drink ' + drink)
        
    def ageDouble(self):
        self.age = self.age ** 2
        print(self.name ,' age is ' ,self.age)