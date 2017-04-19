import os
import sys
packageName=""
command = "adb shell ps | grep %s | awk '{print $2}'"%(packageName)
p = os.popen(command)
##for some applications,there are multiple processes,so we should get all the process id
pid = p.readline().strip()
filters = pid
while(pid != ""):
    pid = p.readline().strip()
    if (pid != ''):
        filters = filters +  "|" + pid
        #print 'command = %s;filters=%s'%(command, filters)
if (filters != '') :
    cmd = 'adb logcat | grep --color=always -E "%s" '%(filters)
    os.system(cmd)