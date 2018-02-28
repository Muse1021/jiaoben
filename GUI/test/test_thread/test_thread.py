# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys,threading,subprocess,time

class MainStyle(QWidget):
    def __init__(self):
        super(MainStyle,self).__init__()
        self.f = func()
        self.initUI()
    def initUI(self):
        self.resize(500,500)
        self.setWindowTitle(u'工具')
        self.btn_setting = QPushButton("A",self)
        self.btn_setting.clicked.connect(self.installs)
        self.btn_setting.move(200,100)
        self.btn_B = QPushButton("b",self)
        self.btn_B.clicked.connect(self.installB)
        self.btn_B.move(100,100)
        #main布局
        self.show()
    def installs1(self):
        print "thread"
        self.Threadin = threadInstall()
        self.Threadin.start()
    def installs(self):
        self.d = threadInstall(self.f.A)
        self.d.start()
    def installB(self):
        self.d = threadInstall(self.f.B)
        self.d.start()
class func():
    def __init__(self):
        pass
    def A(self):
        time.sleep(6)
        print "AAA"
    def B(self):
        time.sleep(6)
        print "BBB"

class threadInstall(QtCore.QThread):
    def __init__(self,f):
        super(threadInstall,self).__init__()
        self.f = f
    def run1(self):
        print "in install"
        ins = "adb install -r C:/Users/Administrator/Desktop/CleanMaster-v60411014-sj-100003-uL.apk"
        Poplog =subprocess.Popen(ins,shell= True, stdout = subprocess.PIPE).stdout
        Poplog.readlines()
    def run(self):
        self.f()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainStyle()
    app.exec_()