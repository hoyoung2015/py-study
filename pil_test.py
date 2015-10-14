#coding=utf-8
__author__ = 'Administrator'
a = "abc"
b = "cba"

print list(a)
print list(b)

def func(s,t):
    print (lambda x:(x.sort(),x)[1])(list(s))
    print list(s).sort()
    s = "".join((lambda x:(x.sort(),x)[1])(list(s)))
    t = "".join((lambda y:(y.sort(),y)[1])(list(t)))
    if s == t:
        return True
    else:
        return False

print(func(a,b))
