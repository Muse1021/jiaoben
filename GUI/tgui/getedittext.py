#!/usr/bin/python  
# -*- coding: utf-8 -*-  
#单行编辑器中键入的文字会立即打印在屏幕上  
  
from PyQt4 import QtGui  
from PyQt4 import QtCore   
  
class Example(QtGui.QWidget):  
    def __init__(self, parent=None):  
        QtGui.QWidget.__init__(self, parent)  
  
        self.initUI()  
  
  
    def initUI(self):  
  
        self.edit = QtGui.QLineEdit(self)#创建 QLineEdit 。  
  
        self.edit.move(60, 100)#文本框的位置  
  
        self.connect(self.edit, QtCore.SIGNAL('textChanged(QString)'),self.onChanged)  
        #如果单行编辑器中的文本发生变化，调用 onChanged() 方法。  
  
          
        self.setWindowTitle('QLineEdit')  
        self.setGeometry(250, 200, 350, 250)  
  
  
    def onChanged(self):#这个函数能够实时打印文本框的内容  
        b=self.edit.text()  
        print (u'文本框此刻输入的内容是：%s'%b)  
          
def main():  
    app = QtGui.QApplication([])  
    exm = Example()  
    exm.show()  
    app.exec_()  
  
  
if __name__ == '__main__':  
    main()  

