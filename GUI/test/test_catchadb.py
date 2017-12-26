# -*- coding: utf-8 -*-
import subprocess
def test1():
	command = "adb shell"
	strs = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stderr.read()
	print strs
def test2():
	install_cmd = "adb install -r C:/Users/Administrator/Desktop/CleanMaster-v51751077-sj-100003-uL.apk"
	print "start"
	Poplog = subprocess.Popen(str(install_cmd), shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout
	sum = 1
	for i  in Poplog.readlines():
		print str(sum),":",i
		sum+=1
def test3():
	install_cmd = "adb install -r C:\Users\Administrator\Desktop\CleanMaster-v60111011-sj-100003-uL.apk "
	Poplog = subprocess.Popen(str(install_cmd), shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout
	sum = 1
	if "Success" in Poplog.readlines()[-1]:
		print "chenggong"
	else:
		print "fail"
test2()