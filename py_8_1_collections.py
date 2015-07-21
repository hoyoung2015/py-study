#coding=utf-8
__author__ = 'Administrator'

from collections import namedtuple

#namedtuple
#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，
# 并可以用属性而不是索引来引用tuple的某个元素。

Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)

print p,p.x,isinstance(p,Point),isinstance(p,tuple)

#deque
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
print q
q.appendleft('y')
print q

#OrderedDict Key会按照插入的顺序排列，不是Key本身排序
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print d
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print od



