import os,subprocess,time,re
filename = "D:\log.txt"
log_file = "D:\log2.txt"
logcat_file = open(filename, 'w')
logcmd = "adb logcat -v time"
killadb = "adb kill-server"
Poplog = subprocess.Popen(logcmd,stdout=logcat_file,stderr=subprocess.PIPE)
Q = raw_input("Enter q to quit the pro!")
if Q.lower() == 'q':
    Poplog.terminate()
    subprocess.Popen(killadb)
logcat_file.close()

print "kill"
errorId = 0
go_on_id = 0
with open((log_file), 'w') as s:
    with open(filename) as f:
        for line in f:
            if 'FATAL' in line:
                go_on_id = 1
                s.write('#' + '-' * 40 + '\n')
                s.write(line)
                # 通过指定分隔符对字符串进行切片
                errorId = line.split('(')[1].split(')')[0].strip()
            #   reg = re.compile(r'\( (.*)\)')
            #   errorId = re.findall(reg,line)
            elif go_on_id == 1:
                if errorId in line:
                    s.write(line)
                else:
                    go_on_id = 0
