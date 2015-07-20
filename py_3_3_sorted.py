#coding=utf-8
__author__ = 'Administrator'

list = [4,5,2,6,7,3,5]
print sorted(list)

#逆序排序
def reversed_cmp(x,y):
    if x>y:
        return -1
    if x<y:
        return 1
    return 0
print sorted(list,reversed_cmp)

#字符串忽略大小写排序
def cmp_ignore_case(s1,s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1<u2:
        return -1
    if u1>u2:
        return 1
    return 0
print sorted(['Hoyoung','abc','Word'],cmp_ignore_case)