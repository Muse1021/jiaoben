# -*- coding: utf-8 -*-
from PyQt4 import QtCore,QtGui
import time
#继承 QThread 类
class BigWorkThread(QtCore.QThread):
    """docstring for BigWorkThread"""
    #声明一个信号，同时返回一个list，同理什么都能返回啦
    finishSignal = QtCore.pyqtSignal(list)
    finishSignal1 = QtCore.pyqtSignal(str)
    finishSignal2 = QtCore.pyqtSignal(str)
    #构造函数里增加形参
    def __init__(self, t,parent=None):
        super(BigWorkThread, self).__init__(parent)
        #储存参数
        self.t = t

    #重写 run() 函数，在里面干大事。
    def run(self):
        #大事
        time.sleep(self.t)
        #大事干完了，发送一个信号告诉主线程窗口
        self.finishSignal.emit(['hello,','world','!'])
        self.base()
        time.sleep(3)
        print"2222222222222222222"
        self.finishSignal1.emit("uu")
    def base(self):
        time.sleep(3)
        print "inbase"
        self.finishSignal2.emit("base")

