# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window3(object):
    def setupUi(self, window3):
        window3.setObjectName("window3")
        window3.resize(806, 520)
        window3.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(window3)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(6, -18, 111, 521))
        self.label.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 50, 101, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 100, 101, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_113 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_113.setGeometry(QtCore.QRect(50, 420, 51, 51))
        self.pushButton_113.setStyleSheet("background-image: url(:/newPrefix/pic/login.png);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_113.setText("")
        self.pushButton_113.setObjectName("pushButton_113")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 100, 381, 271))
        self.label_2.setStyleSheet("background-image: url(:/newPrefix/pic/3.png);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/pic/3.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 310, 111, 21))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        window3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 21))
        self.menubar.setObjectName("menubar")
        window3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window3)
        self.statusbar.setObjectName("statusbar")
        window3.setStatusBar(self.statusbar)

        self.retranslateUi(window3)
        QtCore.QMetaObject.connectSlotsByName(window3)

    def retranslateUi(self, window3):
        _translate = QtCore.QCoreApplication.translate
        window3.setWindowTitle(_translate("window3", "MainWindow"))
        self.pushButton.setText(_translate("window3", "Home"))
        self.pushButton_2.setText(_translate("window3", "Scrapping"))
        self.label_3.setText(_translate("window3", "0301 6395907"))
import image


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window3 = QtWidgets.QMainWindow()
    ui = Ui_window3()
    ui.setupUi(window3)
    window3.show()
    sys.exit(app.exec_())
