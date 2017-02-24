import subprocess,time
filename = "D:\log.txt"
log_file = "D:\log2.txt"
logcat_file = open(filename, 'w')

logcmd = "adb logcat -v time"
Poplog = subprocess.Popen(logcmd,stdout=logcat_file,stderr=subprocess.PIPE)
time.sleep(10)
Poplog.terminate()
logcat_file.close()
errorId = 0
go_on_id = 0
with open((log_file), 'w') as s:
	with open(filename) as f:
		for line in f:
			if 'FATAL' in line:
				go_on_id = 1
				s.write('#' + '-' * 40 + '\n')
				s.write(line)
				errorId = line.split('(')[1].split(')')[0].strip()
			elif go_on_id == 1:
				if errorId in line:
					s.write(line)
				else:
					go_on_id = 0