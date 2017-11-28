# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)




class MainStyle(QWidget):
	def __init__(self):
		super(MainStyle,self).__init__()
		self.initUI()
	def initUI(self):
		self.resize(500,500)
		self.setWindowTitle(u'工具')
		self.btn_setting = QPushButton()
		self.btn_setting.setStyleSheet("""QPushButton{background-image:url(./img/icon_cog.png);width:16px;height:16px;padding-top:0px;border:0px;margin-right:15px;}
                                        QPushButton:hover{background-image:url(./img/icon_cogs.png);}""")
        #main布局
		self.topBarLayout = QtGui.QHBoxLayout()
		self.topBarLayout.addStretch()
		self.topBarLayout.addWidget(self.btn_setting,0,Qt.AlignRight | Qt.AlignHCenter)
		self.show()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainStyle()
    app.exec_()