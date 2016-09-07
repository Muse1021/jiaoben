#coding=utf-8
import re
strs="muse01 love is muse"
strs1= "<img src=\"http://s9.knowsky.com/bizhi/jpg/2010121210.jpg\" width"
exc =re.compile(r"e(\d\d) l")
# exc1 = re.compile(r'src="([\w\W]*)" width')
# coms = r'src="(.+?\.jpg)" width'
def add():
    addstr="ldkff@360.com"
    rex = re.compile(r'[\w]{4,6}@(360|163).com')
    result =re.match(rex,addstr)
    print result.groups()
def fenzu():
    fenzustr = "<book>python</book>"
    fenzustr1 = "<book>"
    fenzustr2 = "<book></book>"
    rex = re.compile(r'<([\w]+>)')
    rex2 = re.compile(r'<([\w]+>)</\1')
    rex3 = re.compile(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)')
    result=re.match(rex3,fenzustr)
    result1 = re.match(rex,fenzustr1)
    result2 = re.match(rex2,fenzustr2)
    print result1.group(),result1.groups()
    print(result2.group(),result2.groups())
    print(result.group(),result.groups())
fenzu()
coms = r'src="(.+)" width'
exc1 = re.compile(coms)
result = re.findall(exc,strs)
result1 = re.findall(exc1,strs1)
print result1
# print exc.match(strs).groups()
ma = re.match(r'[1-9]?\d\d$','09')
# print ma.group()