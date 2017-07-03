#coding=utf-8
import threading,time
class mythread (threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id = id
    def run(self):
        for i in range(20):
            print("dengdai")
            time.sleep(2)

def sta(n):
# 子线程随主线程结束
    t.setDaemon(True)
    t.start()

    for i in range(n):
        time.sleep(1)
        print i
t = mythread(99)
sta(5)

