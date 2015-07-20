#coding=utf-8
__author__ = 'Administrator'
#map
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回
def f(x):
    return x*x
print map(f,[2,3,5])

print map(str,[1,2,3])
print map(int,['1','2','3'])

#reduce
#reduce把一个函数作用在一个序列[x1, x2, x3...]上，
#这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
def add(x,y):
    return str(x)+str(y)
print reduce(add,[1,2,3,4,5])

#将字符串转为整数
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(fn,map(char2num,s))
print str2int('13579')





