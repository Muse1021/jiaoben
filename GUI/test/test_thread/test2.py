# -*- coding: utf-8 -*-
import threading,time,sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
#自己写的线程，继承父类threading.Thread  
class Thread(threading.Thread):  
    def __init__(self, signal_pictures):  
        threading.Thread.__init__(self)  
        #定义更换图片信号  
        self.signal_pictures = signal_pictures  
    def run(self):  
        while True:  
            #每隔两秒，信号发射一次  
            self.signal_pictures.emit()  
            time.sleep(2)  
  
class Mainpage (QDialog, Mainpage.Ui_Mainpage):  
    # 声明信号  
    signal_pictures=QtCore.pyqtSignal()  
    flag=0  
    def __init__(self, parent=None):  
        super(Mainpage, self).__init__(parent)  
        self.setupUi(self)  
  
        #信号关联更换图片函数  
        self.signal_pictures.connect(self.signal_pictures_function)  
  
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    mainpage = Mainpage()  
    mainpage.show()  
    #抛出线程  
    Thread(mainpage.signal_pictures).start()  
    app.exec_()  