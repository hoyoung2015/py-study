#coding=utf-8
__author__ = 'Administrator'
def lazy_sum(*args):
    def sum():
        ax = 0
        for a in args:
            ax = ax + a
        return ax
    return sum

print lazy_sum(1,2,3,4,5) #返回function
print lazy_sum(1,2,3,4,5)() #返回function并执行

#当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
f1 = lazy_sum(1,2,3,4,5)
f2 = lazy_sum(1,2,3,4,5)
print f1==f2

def lazy_sumnx(*args):
    def sumnx(n):
        ax = 0
        for a in args:
            ax = ax + a
        return ax*n
    return sumnx
print lazy_sumnx(1,2,3,4,5)(2) #返回function并执行


#返回函数不要引用任何循环变量，或者后续会发生变化的变量
#如果一定要引用循环变量怎么办？方法是再创建一个函数，
#用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变

