# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
#从 ui.py 文件里 import ui类
from example_ui import Ui_Dialog
import sys
from func import *
import time

class MyDialog(QtGui.QDialog,Ui_Dialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        #调用内部的 setupUi() ，本身对象作为参数
        self.setupUi(self)
        #连接 QPushButton 的点击信号到槽 BigWork()
        self.pushButton.clicked.connect(self.BigWork)

    def BigWork(self):
        #把按钮禁用掉
        self.pushButton.setDisabled(True)
        #import 自己的进程类
        from threads import BigWorkThread
        #新建对象，传入参数
        self.bwThread = BigWorkThread(int(1))
        #连接子进程的信号和槽函数
        self.bwThread.finishSignal.connect(self.BigWorkEnd)
        self.bwThread.finishSignal1.connect(self.BigWorkEnd1)
        self.bwThread.finishSignal2.connect(self.BigWorkEnd1)
        #开始执行 run() 函数里的内容
        self.bwThread.start()

    #增加形参准备接受返回值 ls
    def BigWorkEnd(self,ls):
        print 'get!'
        #使用传回的返回值
        for word in ls:
            print word,
        #恢复按钮
        self.pushButton.setDisabled(False)
        QtGui.QMessageBox.about(self,u"提示",u"已恢复！！")
    def BigWorkEnd1(self,ls):
        QtGui.QMessageBox.about(self,"aa",ls)

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    #新建类对象
    Dialog = MyDialog()
    #显示类对象
    Dialog.show()
    sys.exit(app.exec_())