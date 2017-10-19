# -*- coding: utf-8 -*-
import sys,time
reload(sys)
sys.setdefaultencoding("utf-8")
from PyQt4 import QtGui, QtCore
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
			#return strs
        else:
            super(Edit,self).dropEvent(event)
class MyWindow(QtGui.QWidget):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setGeometry(100,100,300,400)
        self.setWindowTitle("Filenames")
        self.apkpath = Edit(self)
        self.apkpath.setGeometry(QtCore.QRect(90, 90, 61, 51))
        self.apkpath.setText("Change Me!")
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.apkpath)
        self.setLayout(layout)
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
