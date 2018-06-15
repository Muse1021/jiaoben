__author__ = 'cm'
# -*- coding:utf-8 -*-
def mountion(a):
    for i in range(1,a):
        str1 = " "*(a-i)
        str2= ""
        for j in range(i):
            str2 = str2+"*"+" "
        print str1+str2
def mountion2(a):
    for i in range(1,a):
        str1 = " "*(a-i)
        str2= ""
        for j in range(i):
            str2 = str2+"*"+" "
        print str1+str2


mountion(5)