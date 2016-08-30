__author__ = 'Muse'
import urllib
import re

def getpageurl(i):
    pageurls=[""]*i
    for j in range(i):
        pageurl="http://bizhi.knowsky.com/bizhi.asp?id="+str(j+1)
        pageurls[j]=pageurl
    return pageurls

def getHtml(url):
    lists = len(url)
    htmls=[""]*lists
    for i in range(lists):
        page = urllib.urlopen(url[i])
        htmls[i] = page.read()
    return htmls

def getImg(html):
    reg = r'src="(.+?\.jpg)" width'
    imgre = re.compile(reg)
    sum2=len(html)
    imglists=[]
    for i in range(sum2):
        inhtml=html[i]
        imglist = re.findall(imgre,inhtml)
        imglists=imglists+imglist
    return imglists
def dldimg(str):
    x=261
    for imgurl in str:
        if x!=1000:
            urllib.urlretrieve(imgurl,"pic\p"+'%s.jpg' % x)
            x+=1
        else:
            break

pageurl = getpageurl(50)
pageinurl = getHtml(pageurl)
strs=getImg(pageinurl)
dldimg(strs)