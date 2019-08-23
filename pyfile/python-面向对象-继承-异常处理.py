#!/usr/bin/env python
# coding: utf-8

# ## python 面向对象

# In[17]:


def getabs(x,y):
    return(abs(x),abs(y))

class MyClass:
    #定义类名
    "myclass help"
    #构造函数     
    def __init__(self,x,y=0):
        self.x = x
        self.y = y
    def info(self):
        print('this is my class.')
    def mysum(self,x,y):
        x,y = getabs(x,y)
        return x + y
nclass = MyClass(2,-9)
nclass.info()
nclass.mysum(2,-99)


# ### 静态方法和类成员方法

# In[17]:


class DemoClass2:
    @staticmethod
    def static_methon():
        print('you can call me every where.')
        
    @classmethod
    def classs_methond(cls):
        print('you can call me when democlass is not null.',cls)

dcs = DemoClass2()
dcs.classs_methond()


# ### 继承和多继承

# In[62]:


class Animal(object):
    def __init__(self,name='baseanimal',age=1):
        self.name = name
        self.age = age
        
    def aniinfo(self):
        print('当前位置',self.name,self.age)
        
    def eat(self):
        print(self.name,self.age," 's animal should eat something.")
        self.info()
        
class Ant(object):
    def __init__(self,x=0,y=0,color='black'):
        self.x = x
        self.y = y
        self.color = color
        
    def info(self):
        print('当前位置',self.x,self.y)
        
    def crawl(self,x,y):
        print('ant is crawling.')
        self.x = x
        self.y = y
        self.info()
        
    def bit(self):
        print('ant bit people.')
        
class FlyAnt(Animal,Ant,):
    def __init__(self,name,age,x,y,color):
        super(FlyAnt,self).__init__()
        self.name = name
        self.age = age
        self.x = x
        self.y = y
        self.color = color
#     def eat(self):
#         print('flyant eat',self.color)
    #重写bit方法     
    def bit(self):
        print('flyant bit animals, not people')
    #新增功能
    def fly(self,x,y):
        print('this ant can fly.')
        self.x = x
        self.y = y
        self.info()
# TEST
flyant = FlyAnt(name='爬行动物',age=99,x=9,y=100,color='blue')
# flyant.crawl(3,5)
flyant.fly(99,10)
flyant.eat()


# ### 异常处理

# In[70]:


def testTry():
    a = '789'
    try:
        print(3 / 0)
    except AttributeError:
        print('attributeError.')
    except TabError:
        print('tableError')
    else:
        print('other')
    finally:
        print('end')
testTry()


# In[75]:


def testRaise():
    for i in range(5):
        try :
            #条件为假 则大于3则不抛出异常
            assert i > 3
        except AssertionError:
            print('assert a error')
#             raise NameError
        print(i)
    print('end')
testRaise()


# In[77]:


class myError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return self.value
raise myError('this is my error.')


# In[ ]:


import pdb
pdb.run("""
for i in range():
    print(i)
""")

