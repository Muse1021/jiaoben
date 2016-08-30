#coding=utf-8
import requests     # 导入requests模块
from bs4 import BeautifulSoup as bs # 从bs4 模块中导入BeautifulSoup模块并命名为bs

request_url = 'https://testerhome.com/topics/4621'  # 请求的url是 上一章的url地址
response = bs(requests.get(request_url).text , 'lxml') # 返回一个bs对象 ，格式为lxml
print response
print"这篇文章的名字是 ：" , response.h1.string  # 获取文章标题˜
print"该文章属于 ：" , response.find('a',{"class":"node"}).text#获取发表在哪一个技术类型下
print"该文章的分类为 ： ", response.h2.string
# print("-------"*10+"这里是获取所有的楼层评论"+"-------"*10)
# for i in response.find_all('div',{"class":"reply"}):
#     print(i.p.text)
# print("-------"*10+"这里是获取所有的楼层评论"+"-------"*10)