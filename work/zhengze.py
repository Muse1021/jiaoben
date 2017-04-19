#coding=utf-8
import re
cr = re.compile(r".*?123") 
s = "abcd123d123ad1v123" 
print cr.findall(s)
#匹配开头结尾，中间有规则
#cr1 = re.compile(r"\A123.*ab\Z")
cr1 = re.compile(r"123[^\d|p|s]*?ab")
s1 = "a123qc489abvpd123d“p”f12ab123sabd123f1123abc"
print cr1.findall(s1)
#识别下列字符串：“bat,” “bit,” “but,” “hat,” “hit,” 或 “hut”
s2 = "you are bat, but i have a hat"
cr2 = re.compile(r"[b|h].t")
print cr2.findall(s2)
#匹配用一个空格分隔的任意一对单词，比如，名和姓
s3 = "Sam Smith"
#cr3 = re.compile(r".*\s.*")
cr3 = re.compile(r"\S+\s\S+")
print cr3.findall(s3)
#匹配任意数目的表示街道名字的单词
s4 = "3120 De la Cruz Boulevard."
cr4 = re.compile(r"(\d+\s)+(\w+\s)+")
print cr4.findall(s4)