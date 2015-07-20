#coding=utf-8
__author__ = 'Administrator'

#filter()函数用于过滤序列
#filter()把传入的函数依次作用于每个元素，
#然后根据返回值是True还是False决定保留还是丢弃该元素
def is_odd(x):
    return x%2==1
print filter(is_odd,[1,2,3,4,5,6,7,8,9])


