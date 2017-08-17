# -*- coding:utf-8 -*-
from __future__ import division
import sys,os
from PyQt4 import QtCore, QtGui, uic
import subprocess
qtCreatorFile = "tax_calc.ui" # Enter file here.
qtdialogFile = "dialo.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
Ui_Dialog, QtDialogClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.clear_data.clicked.connect(self.Clear)
    def Clear(self):
        res = self.RunCmd("adb shell pm clear com.qihoo.appstore")
        os.popen("adb shell am start -W -n com.qihoo.appstore/com.qihoo.appstore.home.MainActivity | findstr ThisTime")
        dlg=uic.loadUi("Dialog.ui")
        if res != '' :
            dlg.res_text.setText(res)
        else:
            dlg.res_text.setText("error!!")
        dlg.exec_()
    def RunCmd(self,curCmd):
            pipe = subprocess.Popen(curCmd,shell = True,stdout =subprocess.PIPE).stdout
            printStr = pipe.read()
            return printStr

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

