#coding=utf-8
__author__ = 'Administrator'

#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
print map(lambda x:x*x,[1,2,3,4,5])

f = lambda x:x*x
print f(5)

def build(x,y):
    return lambda x,y:x*x+y*y

