# -*-coding: utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore

class Exemple(QtGui.QWidget):
	def __init__(self):
		super(Exemple,self).__init__()
		self.initUI()
	def initUI(self):
		self.resize(500,500)
		self.center()
		self.setWindowTitle("seticon")
		self.setWindowIcon(QtGui.QIcon("1.jpg"))
		QtGui.QToolTip.setFont(QtGui.QFont('SansSerif',10))
		self.setToolTip('This is A <b>QWidget</b> widget')
		btn = QtGui.QPushButton('button',self)
		btn.setToolTip('This is a <b>QWidget</b> widget')
		btn.resize(btn.sizeHint())
		btn.move(50,50)
		btn_quit = QtGui.QPushButton('quit',self)
		btn_quit.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btn_quit.resize(btn_quit.sizeHint())
		btn_quit.move(100,100)
		self.show()
	def closeEvent(self,event):
		reply = QtGui.QMessageBox.question(self,'Massage',"ARE YOU SURE?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,QtGui.QMessageBox.No)
		if reply ==QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()
	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	ic = Exemple()
	sys.exit(app.exec_())