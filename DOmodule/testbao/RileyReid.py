#coding=utf-8
import urllib
import re
import sys 
reload(sys) 
sys.setdefaultencoding('utf8')

def getpageurl(i):
    pageurls=[""]*i
    for j in range(i):
        if j==0:
            pageurl="http://44pdpd.com/xiazaiqu/btoumei/"
            pageurls[j]=pageurl
        else:    
            pageurl="http://44pdpd.com/xiazaiqu/btoumei/index_"+str(j)+".html"
            pageurls[j]=pageurl
    return pageurls

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
def findRileyReid(strs):
    #只找出title
    '''    
    reg = r'title="(.+?\.html)" target'
    imgre = re.compile(reg) 
    urllists=[]'''
    sum=len(strs)
    for i in range(sum):
        pagestr=getHtml(strs[i])
#        lists = re.findall(imgre,pageurl)
#        if pagestr.find("Riley") != -1:
        if pagestr.find("malkova") != -1:
            print "打开："+str(i)
        else:
            print "现在是："+str(i)
            pass     
        
p=getpageurl(241)

 
findRileyReid(p)
