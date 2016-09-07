# -*- encoding: gbk -*-
from __future__ import division
a = [12,3,21,33,109,15]
def maopao(arr):
    # lens = len(arr)
    # for i in range(lens):
    #     j=i+1
    #     for  j in range(lens):
    #         if arr[i] < arr[j]:
    #             # n = arr[i]
    #             # arr[i] = arr[j]
    #             # arr[j] = n
    #             arr[i],arr[j] = arr[j],arr[i]
    lens = len(arr)
    print(lens)
    for i in range(lens):
        for j in range(i,lens):
            if arr[j]>arr[i]:
                bak = arr[i]
                arr[i] = arr[j]
                arr[j] = bak
    return arr
def quickSort(L, low, high):
    i = low
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j-1
        L[i] = L[j]
        while i < j and L[i] <= key:
            i = i+1
        L[j] = L[i]
    L[i] = key
    quickSort(L, low, i-1)
    quickSort(L, j+1, high)
    return L
# print quickSort(a,0,5)
def chengfabiao():
    for i in range(1,10):
        for j in range(1,i+1):
            print "%d * %d = %d "%(j,i,j*i),
        print('\n')
def chufa():
    fenmu = int(raw_input("fenmu: "))
    fenzi = int(raw_input("fenzi: "))
    print fenmu/fenzi
print maopao(a)