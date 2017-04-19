#-*- coding:utf-8 -*-
import requests 
import sys,re
from bs4 import BeautifulSoup
type = sys.getfilesystemencoding()
url = "http://bbs.cmcm.com/plugin.php?id=mini_soufang:index&page="
urllist = []
prices = []
for i in range(1,4):
	urls = urllist.append(url+str(i))
for i in urllist:
	print i
	soup = BeautifulSoup(requests.get(i).text,'lxml')
	for i in soup.find_all('span',{"class":"number"}):
		prices.append(i.get_text())	
s = len(prices)
print("len = :",s)
ss = 0
for i in prices:
	print i 
	ss+=int(i)
print ("ss = :",ss)
pp = ss/s	
print ("pp :",pp)
#soup = BeautifulSoup(requests.get(url).text,'lxml').decode('utf-8').encode(type)
soup = BeautifulSoup(requests.get(url).text,'lxml')
#print soup.('a',{"href":"plugin.php?id=mini_soufang:index"}).text
#print soup.h1.string
a = re.compile(r"\d+")
for i in soup.find_all('span',{"class":"number"}):
	print (i.get_text())
#    print a.findall(str(i))

#exp = BeautifulSoup('<span class="number">1800</span>','lxml')
#print exp.span.string
