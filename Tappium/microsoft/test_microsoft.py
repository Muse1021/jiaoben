#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from OpenActivity import *
for i in range(30):
    strs = openappstore()
    if i == 0 or i == 3 or i == 10 or i == 25:
        if str(strs) == '温馨提示':
            print str(i)+" day: "+strs
            pass
        else:
            print "error:"+str(i)+" day: "+strs
    else:
        if str(strs) == '小主，确定退出吗？':
            print str(i)+" day: "+strs
            pass
        else:
            print "error:"+str(i)+" day: "+strs
    addtime()



driver.quit()