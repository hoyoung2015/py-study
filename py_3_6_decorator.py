#coding=utf-8
__author__ = 'Administrator'

def now():
    print '2015-7-20'
f = now
f()

def log(func):
    def wrapper(*args,**kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
@log
def now():
    print '2015-7-20'
now()
f = now
f()

#now = log(now)
# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，
# 只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在
# log()函数中返回的wrapper()函数

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print '2015-7-20'

now()

print now.__name__

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
@log
def now():
    print '2015-7-20'

print now.__name__