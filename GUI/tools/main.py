# -*-coding: utf-8 -*-
import sys
from chosedevices import get_devices
from PyQt4 import QtGui,QtCore
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
class Edit(QtGui.QLineEdit):
    def __init__(self, parent):
        super(Edit, self).__init__(parent)
        self.setAcceptDrops(True)
        #self.setDragDropMode(QAbstractItemView.InternalMove)
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(Edit, self).dragEnterEvent(event)
    def dragMoveEvent(self, event):
        super(Edit, self).dragMoveEvent(event)
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            #遍历输出拖动进来的所有文件路径
            for url in event.mimeData().urls():
                strs =  str(url.toLocalFile()).decode('UTF-8').encode('GBK')
                self.setText(strs)
            event.acceptProposedAction()
        else:
            super(Edit,self).dropEvent(event)
class Exemple(QtGui.QWidget):
    def __init__(self):
        super(Exemple,self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(500,500)
        self.center()
        self.setWindowTitle("Tool")
        self.setWindowIcon(QtGui.QIcon("icon.jpg"))
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif',10))
        self.setToolTip('This is A <b>QWidget</b> widget')
        btn = QtGui.QPushButton('button',self)
        btn.clicked.connect(self.btn_event)
        btn.setToolTip('This is a <b>QWidget</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(400,100)
        btn_quit = QtGui.QPushButton('quit',self)
        btn_quit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(300,100)
        btn_re = QtGui.QPushButton('re',self)
        btn_re.clicked.connect(self.devices_list)
        btn_re.resize(btn_quit.sizeHint())
        btn_re.move(200,100)
        string_list = ['no device']
        self.combo = QtGui.QComboBox(self)
        self.combo.addItems(string_list)
        self.combo.resize(100, 30)
        self.apkpath = Edit(self)
        self.apkpath.setGeometry(QtCore.QRect(90, 120, 610, 51))
        self.apkpath.setText("")
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.apkpath)
        self.setLayout(layout)
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
    def btn_event(self):
        install = "adb install -r "+self.apkpath.text()
        print install
    def devices_list(self):
        str = get_devices()
        print str
        self.combo.addItems(str)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ic = Exemple()
    sys.exit(app.exec_())