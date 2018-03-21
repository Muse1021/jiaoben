# -*-coding: utf-8 -*-
import subprocess
import requests     # 导入requests模块
from bs4 import BeautifulSoup as bs # 从bs4 模块中导入BeautifulSoup模块并命名为bs
def test2():
    request_url = 'http://app.mi.com/details?id=com.cleanmaster.mguard_cn'
    res = requests.get(request_url)
    res1 = requests.get("http://app.mi.com/details?id=com.tencent.qqmusic")
    print(res1.url)
    response = bs(res.text,'lxml')
    print response.h3.string
def getapp():
    getlist = "adb shell pm list packages"
    Poplog = subprocess.Popen(getlist,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    A = Poplog.stdout.readlines()
    x = len(A)
    applist= [""]*x
    for s in range(x):
        applist[s] = A[s].split(":")[1].split("\r\r\n")[0]
    return applist
def getname(lists):
    for s in lists:
        url = "http://app.mi.com/details?id="+s
        res = requests.get(url)
        if res.url != "http://app.mi.com/":
            response = bs(res.text,'lxml')
            print response.h3.string

lists=['com.tencent.qqmusic']
listss = getapp()
print listss
getname(listss)


