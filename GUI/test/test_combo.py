# -*- coding: utf-8 -*-
import sys  
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
class Ex(QDialog):  
    def __init__(self,parent=None):  
        super(Ex, self).__init__(parent)  
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)  
        self.setStyleSheet(  
                           "QComboBox{border:1px groove rgb(170,214,252);}"  
                           "QComboBox{border-radius:2px;}"  
                           "QComboBox{color:rgb(100,20,200);}"  
                           "QComboBox{font:times;}"  
                           "QComboBox{font-size:15px;}"  
                           "QComboBox{font:bold;}"  
                           "QComboBox:hover{border-color:rgb(50,150,250)}"  
                           "QComboBox QAbstractItemView:item{height:50px;}"  
                           "QComboBox:drop-down{subcontrol-origin:padding;}"  
                           "QComboBox:drop-down{subcontrol-position:top right;}"  
                           "QComboBox:drop-down{width:30px;}"  
                           "QComboBox:drop-down{border-left-width:1px;}"  
                           "QComboBox:drop-down{border-left-color:rgb(170,214,252);}"  
                           "QComboBox:drop-down{border-left-style:solid;}"  
                           "QComboBox:drop-down{border-top-right-radius:3px;}"   
                           "QComboBox:drop-down{border-bottom-right-radius:3px;}"  
                           "QComboBox:down-arrow{image:url(images/lower.gif);}"  
                            )  
        self.InitUI()  
        self.setFixedSize(400,450)  
        self.linePath()
		#这句放在设置窗口大小的代码之后，方可调用self.width（）等函数，不然无效。  
        #self.setAttribute(Qt.WA_TranslucentBackground,True)#透明窗口  
    def InitUI(self):  
        self.tipLabel = QLabel(u"ComboBox",self)  
        self.tipLabel.setFont(QFont("times",13,QFont.Bold))  
        self.tipLabel.setStyleSheet("color:white;")  
        self.closeButton = QPushButton(self)  
        self.closeButton.setFixedSize(30,30)  
        self.closeButton.setIcon(QIcon("images/0.png"))  
        self.closeButton.setIconSize(QSize(30,30))  
        self.closeButton.setStyleSheet("QPushButton{border:5px;}"  
                           "QPushButton:hover{background:red;}"  
                           "QPushButton:pressed{background:black;}")  
        self.connect(self.closeButton, SIGNAL("clicked()"),self.slotClose)  
        self.label = QLabel('safafew', self)  
        self.label.setFixedWidth(200)  
        self.label.setFont(QFont("times",12,QFont.Bold))  
        self.combo = QComboBox(self)  
        self.connect(self.combo, SIGNAL("clicked"),self.comboClicked)  
        self.combo.setFixedSize(200,30)  
        self.combo.setFont(QFont("times",12,QFont.Bold))  
        self.listWidget = QListWidget(self)  
        self.combo.setModel(self.listWidget.model())  
        self.combo.setView(self.listWidget)  
        self.combo.setEditable(True)  
        #self.combo.lineEdit().setFocusPolicy(Qt.NoFocus)#可以是combox不能被编辑  
        #self.combo.setFocusPolicy(Qt.NoFocus)#可以是combox不能被编辑  
        self.account_item = []  
        for i in range(3):  
            self.account_item_index = AccountItem()  
            self.account_item_index.setAccountNumber(QString("safe_") + QString.number(i, 10) + QString("@sina.com"))  
            self.connect(self.account_item_index, SIGNAL("showAccount"), self.showAccount)  
            self.connect(self.account_item_index, SIGNAL("removeAccount"), self.removeAccount)  
            self.account_item.append(self.account_item_index)  
        for i in range(3):      
            list_item = QListWidgetItem(self.listWidget)  
            self.listWidget.setItemWidget(list_item, self.account_item[i])  
        self.combo.setEditText("safafew")#设置当前值  
        self.combo.move(100,100)  
        self.label.move(100,270)  
    def comboClicked(self):  
        print "clicked"  
    def showAccount(self,account):  
        print account  
        self.combo.setEditText(account)  
        self.combo.hidePopup() #隐藏combox所有的选项  
        self.label.setText(account)  
    def removeAccount(self,account):  
        print account  
        self.combo.hidePopup()  
        button=QMessageBox.warning(self,"Warning",  
                                   u"是否删除?",  
                                   QMessageBox.Discard|QMessageBox.Cancel)  
        if button==QMessageBox.Discard:  
            for i in range(len(self.account_item)):  
                item = self.listWidget.item(i)  
                account_item_del = self.account_item[i]  
                account_number = account_item_del.getAccountNumber()  
                if(account == account_number):  
                    self.listWidget.takeItem(i)  
                    self.listWidget.removeItemWidget(item)  
                    self.account_item.remove(self.account_item[i])  
                    break  
        elif button==QMessageBox.Cancel:  
            self.label.setText("Warning button/Cancel")  
              
    def linePath(self):  
        aPoint = QPoint(0,0)  
        bPoint = QPoint(self.width()-1,0)  
        cPoint = QPoint(self.width()-1,self.height()-1)  
        dPoint = QPoint(0,self.height()-1)  
        self.linePath = QPainterPath()  
        self.linePath.moveTo(aPoint)  
        self.linePath.lineTo(bPoint)  
        self.linePath.moveTo(bPoint)  
        self.linePath.lineTo(cPoint)  
        self.linePath.moveTo(cPoint)  
        self.linePath.lineTo(dPoint)  
        self.linePath.moveTo(dPoint)  
        self.linePath.lineTo(aPoint)  
        self.linePath.closeSubpath()  
    def slotClose(self):  
        self.close()  
    def mouseMoveEvent(self,event):  
        if self.mousePressed:  
            self.move(self.pos() + event.pos() - self.currentPos)  
     
    def mousePressEvent(self,event):  
        if event.buttons() == Qt.LeftButton:  
            self.currentPos = event.pos()  
            self.mousePressed = True  
     
    def mouseReleaseEvent(self,event):  
        if event.buttons() == Qt.LeftButton:  
            self.mousePressed = False      
              
    def paintEvent(self,event):  
        self.closeButton.move(self.width()-32,2)  
        self.tipLabel.move(5,5)  
          
        p = QPainter(self)  
        pix = QPixmap("images/background.png")  
        p.drawPixmap(self.rect(), pix)  
        p.drawPath(self.linePath)  
          
        painter = QPainter(self)  
        linearGradient = QLinearGradient(0,0,0,35)  
        linearGradient.setColorAt(0, QColor(60,100,200))  
        linearGradient.setColorAt(0.1, QColor(6,88,200))  
        linearGradient.setColorAt(1, QColor(10,100,100))  
        painter.setBrush(QBrush(linearGradient))  
        self.menuRect = QRect(0, 0, self.width(), 35)  
        painter.fillRect(self.menuRect, QBrush(linearGradient))        
      
  
  
  
          
class AccountItem(QWidget):  
    def __init__(self,parent=None):  
            super(AccountItem,self).__init__(parent)  
            self.setStyleSheet(  
                               "QPushButton{border:4px;}"  
                               "QPushButton:hover{background:red;}"  
                               "QPushButton:pressed{background:blue;}")  
            self.mouse_press = False  
            self.hovered = False  
            self.account_number = QLabel()  
            self.account_number.setFont(QFont("times",14,QFont.Bold))  
            self.iconLabel = QLabel()  
            self.iconLabel.setFixedSize(40,40)  
            pixmap0 = QPixmap("images/icon.png").scaled(40,40)  
            self.iconLabel.setPixmap(pixmap0)  
            self.delede_button = QPushButton()  
            pixmap = QPixmap("images/icon.png").scaled(20,20)  
            self.delede_button.setIcon(QIcon(pixmap))  
            self.delede_button.setIconSize(pixmap.size())  
            #self.delede_button.setStyleSheet("background:transparent;");  
            self.connect(self.delede_button, SIGNAL("clicked()"), self.removeAccount)  
            main_layout = QHBoxLayout()  
            main_layout.addWidget(self.iconLabel)  
            main_layout.addWidget(self.account_number)  
            main_layout.addStretch()  
            main_layout.addWidget(self.delede_button)  
            main_layout.setContentsMargins(5, 5, 5, 5)  
            main_layout.setSpacing(5)  
            self.setLayout(main_layout)  
    def setAccountNumber(self,account_text):  
        self.account_number.setText(account_text)  
    def getAccountNumber(self):  
        account_number_text = self.account_number.text()  
        return account_number_text  
    def removeAccount(self):  
        account_number_text = self.account_number.text()  
        self.emit(SIGNAL("removeAccount"),account_number_text)  
          
    def mousePressEvent(self,event):  
        if(event.button() == Qt.LeftButton):  
            self.mouse_press = True  
    def mouseReleaseEvent(self,event):  
        if(self.mouse_press):  
            account_number_text = self.account_number.text()  
            self.emit(SIGNAL("showAccount"),account_number_text)  
            self.mouse_press = False  
    def enterEvent(self,event):  
        self.hovered = True  
        self.repaint()  
    def leaveEvent(self,event):  
        self.hovered = False  
        self.repaint()   
    def paintEvent(self,event):  
        painter0 = QPainter(self)  
        brush0 = QBrush(QColor(255,255,200))  
        painter0.setBrush(brush0)  
        painter0.fillRect(QRect(0,0,self.width(),self.height()), brush0)  
          
        painter1=QPainter(self)  
        painter1.setPen(QPen(QColor(Qt.lightGray),1))  
        outline = QPainterPath()  
        outline.addRoundedRect(0, 0, self.width(), self.height(), 0, 0)  
        painter1.setOpacity(1)  
        painter1.drawPath(outline)  
          
        if self.hovered == True:  
            painter = QPainter(self)  
            brush = QBrush(QColor(Qt.lightGray))  
            painter.setBrush(brush)  
            painter.fillRect(QRect(0,0,self.width(),self.height()), brush)  
          
  
app = QApplication(sys.argv)  
ex = Ex()  
ex.show()  
app.exec_()  