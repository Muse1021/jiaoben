__author__ = 'Muse'
import os
import re
timelist =[]
for i in range(4):
    os.system("adb shell pm clear com.qihoo.appstore")
    b= os.popen("adb shell am start -W -n com.qihoo.appstore/com.qihoo.appstore.home.MainActivity | findstr ThisTime")
    a = re.findall(r"\d+",b.read())
    timelist.append(int(a[0]))
print(timelist)
max = 0
min = timelist[0]
sums = 0
for times in timelist:
    if times >= max:
        max = times
    if times < min:
        min = times
    sums += times
print "max: ",max
print "min: ",min
print "sum: ",sums
avg = (sums -(max+min))/2
print avg

# SEARCH_PAT = re.compile(r'TotalTime\s*:\s*(\d+)')
# pat_search = SEARCH_PAT.search(a)
# if pat_search != None:
#     print pat_search.group(1)
# SEARCH_PAT = re.compile(r'iops\s*=\s*(\d+)')
# src_line = 'io=8192.0MB, bw=24407KB/s, iops=6101 , runt=343698msec'
# pat_search = SEARCH_PAT.search(src_line)
# if pat_search != None:
#     print pat_search.group(1)
# print "find: "
# print a.find('TotalTime: ')
# p1 = re.compile(r'(?:"Total")\d{3}')
# print "  ".join(re.findall(p1,a))
# print re.findall(p1,a)
# s = 'ID: 042 SEX: M DOB:1 1967-08-17 Status: Active 1968'
# p = re.compile(r'(?:19|20)\d{2}')
# print "  ".join(re.findall(p,s))
# print re.findall(p,s)
# coms = r'home(.+)MainActivity'
# exc1 = re.compile(coms)
# result1 = re.findall(exc1,a)
# print "result: "
# print result1