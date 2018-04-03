# -*-coding: utf-8 -*-
import requests,sys,io     # 导入requests模块
from bs4 import BeautifulSoup as bs # 从bs4 模块中导入BeautifulSoup模块并命名为bs

def test1():
	request_url = 'https://testerhome.com/topics/4621'  # 请求的url是 上一章的url地址
	response = bs(requests.get(request_url).text , 'lxml') # 返回一个bs对象 ，格式为lxml
	# print response.decode("utf-8")
	print u"这篇文章的名字是 ：" , response.find('span',{"class":"title"}).text # 获取文章标题˜
	print u"该文章属于 ：" , response.find('a',{"class":"node"}).text#获取发表在哪一个技术类型下
	print u"该文章的分类为 ： ", response.h2.string
	# print("-------"*10+"这里是获取所有的楼层评论"+"-------"*10)
	# for i in response.find_all('div',{"class":"reply"}):
	#     print(i.p.text)
	# print("-------"*10+"这里是获取所有的楼层评论"+"-------"*10)
def Tencent():
	url = "http://news.qq.com/"
	response = bs(requests.get(url).text,'lxml')
	for i in response.find_all('a',{"class":"linkto"}):
		print (i.text)
		print i['href']
Tencent()
#test1()
