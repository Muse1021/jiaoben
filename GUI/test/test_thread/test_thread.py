# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys,threading,subprocess

class MainStyle(QWidget):
    def __init__(self):
        super(MainStyle,self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(500,500)
        self.setWindowTitle(u'工具')
        self.btn_setting = QPushButton(self)
        self.btn_setting.clicked.connect(self.installs)
        #main布局
        self.show()
    def installs(self):
        print "thread"
        self.Threadin = threadInstall()
        self.Threadin.start()
class threadInstall(QtCore.QThread):
    def __init__(self,parent = None):
        super(threadInstall,self).__init__(parent)
    def run(self):
        print "in install"
        ins = "adb install -r C:/Users/Administrator/Desktop/CleanMaster-v60411014-sj-100003-uL.apk"
        Poplog =subprocess.Popen(ins,shell= True, stdout = subprocess.PIPE).stdout
        Poplog.readlines()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainStyle()
    app.exec_()