#-*- coding:utf-8 -*-
import re,subprocess
devices = "83726adb"
pkg_name = "com.cleanmaster.mguard_cn"
cmd = "adb -s " +  devices +" shell  dumpsys  meminfo %s" % (pkg_name)
print(cmd)
output = subprocess.check_output(cmd).split()

s_men = ".".join([x.decode() for x in output])
# 转换为string
print(s_men)
men2 = int(re.findall("TOTAL.(\d+)*", s_men, re.S)[0])
print (re.findall("TOTAL.(\d+)*", s_men, re.S))
print(men2 )