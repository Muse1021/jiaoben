# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
#从 ui.py 文件里 import ui类
from main_ui import Ui_Dialog
import sys,subprocess
import time

#新建自己的窗口类，继承 QDialog 和 ui类
class MyDialog(QtGui.QDialog,Ui_Dialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        #调用内部的 setupUi() ，本身对象作为参数
        self.setupUi(self)
        #连接 QPushButton 的点击信号到槽 BigWork()
        self.pushButton.clicked.connect(self.BigWork)

    def BigWork(self):
        #import 自己的进程类
        from threads import BigWorkThread
        #新建对象
        self.bwThread = BigWorkThread()
        #开始执行run()函数里的内容
        self.bwThread.start()

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    #新建类对象
    Dialog = MyDialog()
    #显示类对象
    Dialog.show()
    sys.exit(app.exec_())