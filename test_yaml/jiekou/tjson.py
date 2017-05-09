# -*- coding:utf-8 -*-
import types  
import urllib2  
import json  
  
  
duan ="--------------------------"  #在控制台断行区别的  
  
#利用urllib2获取网络数据  
def registerUrl():  
    try:  
        url ="https://ws.ksmobile.net/api/GetCloudMsgEx?phonelanguage=zh_CN&cmlanguage=zh_CN&apkversion=5.15.9.1010&dataversion=2017.1.5.737&sdkversion=4.4.4&device=A31&networkstate=wifi&channelid=100003&realchannelid=100003&pkg=com.cleanmaster.mguard_cn&resolution=854*480&mem_size=898&minsdk=14&trdmarket=1&vtype=1&currenttime=1484301764582"  
        data = urllib2.urlopen(url).read()  
        return data  
    except Exception,e:  
        print e  
          
#写入文件  
def jsonFile(fileData):  
    file = open("d:\json.txt","w")  
    file.write(fileData)  
    file.close()  
  
#解析从网络上获取的JSON数据      
def praserJsonFile(jsonData):  
    value = json.loads(jsonData)  
    rootlist = value.keys()  
    print rootlist  
    print duan  
    for rootkey in rootlist:  
        print rootkey  
    print duan  
    subvalue = value[rootkey]  
    print subvalue  
    print duan  
    for subkey in subvalue:  
        print subkey,subvalue[subkey]  
      
if __name__ == "__main__":  
    # xinput = raw_input()  
    # x = 130  
    # xvalue = cmp(x,xinput)  
    # print xvalue  
    # print x/100.0  
      
    data = registerUrl()  
    # jsonFile(data)  
      
    praserJsonFile(data)  