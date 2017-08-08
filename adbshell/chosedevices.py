# -*- coding: utf-8 -*-
import os,subprocess,time,re,sys
def get_devices():
	logcmd = "adb devices"
	#Poplog = subprocess.Popen(logcmd,stderr=subprocess.PIPE)
	#Poplog = os.popen(logcmd)
	Poplog = subprocess.Popen(logcmd, shell=True, stdout=subprocess.PIPE).stdout
	devices = Poplog.readlines()
	devices_list = []
	for i in devices:
		if 'devices' not in i and len(i.split()) > 0:
			#print "i: ",i
			#print "len: ",len(i)
			devices_list.append(i.split()[0])
	device_number = len(devices_list)
	if device_number == 0 :
		print "NO decices !!"
		sys.exit()
	elif device_number == 1:
		devices = devices_list[0]
	else:
		for i in range(device_number):
			print i," ",devices_list[i]
		dec = raw_input("device: ")
		devices = devices_list[int(dec)]
	return devices
def install_app(device):		
	app = raw_input("package path: ")
	install_cmd = "adb -s %s install %s" % (device,app)
	Poplog = subprocess.Popen(install_cmd, shell=True, stdout=subprocess.PIPE).stdout
	Poplog.readlines()
if __name__ == "__main__" :
	device = get_devices()
	install_app(device)

