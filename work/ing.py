# -*- coding: utf-8 -*-
import threading,time
def doing():
	for i in range(15):
		time.sleep(1)
		print "doing"
t = threading.Thread(target=doing)
#t.setDaemon(True)
t.start()
for i in range(3):
		time.sleep(1)
		print "main"
