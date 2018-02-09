# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import time,subprocess

#继承 QThread 类
class BigWorkThread(QtCore.QThread):
    """docstring for BigWorkThread"""
    def __init__(self, parent=None):
        super(BigWorkThread, self).__init__(parent)

    #重写 run() 函数，在里面干大事。
    def run(self):
        #大事

        for i in range(10):
            time.sleep(1)
            print i
        ins = "adb install -r C:/Users/Administrator/Desktop/CleanMaster-v60411014-sj-100003-uL.apk"
        Poplog =subprocess.Popen(ins,shell= True, stdout = subprocess.PIPE).stdout
        Poplog.readlines()