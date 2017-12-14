# -*- coding: utf-8 -*-

"""
This program shows a confirmation 
message box when we click on the close
button of the application window. 
"""

import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):               

        self.resize(500,500)
        self.setWindowTitle('Message box')
        self.btn = QtGui.QPushButton("test",self)
        self.btn.move(400,100)
        self.btn.clicked.connect(self.compare)
        self.Teidt = QtGui.QLineEdit(self)

        self.show()


    def MEvent(self):

        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            print "1"
        else:
            print "2"
    def compare(self):
        if int(self.Teidt.text()) > 1:
            self.MEvent()
        else:
            print "no"

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()