# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scrapping.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import csv
import time
from PyQt5 import QtCore, QtGui, QtWidgets
class MyWindow(QtWidgets.QWidget):
    def __init__(self, fileName, parent=None):
        super(MyWindow, self).__init__(parent)
        self.fileName = fileName

        self.model = QtGui.QStandardItemModel(self)

        self.tableView = QtWidgets.QTableView(self)
        self.tableView.setModel(self.model)

        self.pushButtonLoad = QtWidgets.QPushButton(self)
        self.pushButtonLoad.setText("Load Csv File!")
        self.pushButtonLoad.clicked.connect(self.on_pushButtonLoad_clicked)


        self.layoutVertical = QtWidgets.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.tableView)
        self.layoutVertical.addWidget(self.pushButtonLoad)

    def loadCsv(self, fileName):
        with open(fileName, "r") as fileInput:
            for row in csv.reader(fileInput):    
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)

    @QtCore.pyqtSlot()
    def on_pushButtonWrite_clicked(self):
        self.writeCsv(self.fileName)

    @QtCore.pyqtSlot()
    def on_pushButtonLoad_clicked(self):
        self.loadCsv(self.fileName)
class Ui_window2(object):
    def setupUi(self, window2):
        window2.setObjectName("window2")
        window2.resize(794, 574)
        window2.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(window2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 131, 551))
        self.label.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 111, 51))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 120, 111, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 470, 51, 51))
        self.pushButton_3.setStyleSheet("background-image: url(:/newPrefix/C:/Users/DEll/OneDrive/Pictures/Screenshots/login.png);\n"
"background-image: url(:/newPrefix/pic/login.png);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(150, 10, 141, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(160, 90, 181, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(600, 20, 171, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(520, 20, 75, 21))
        self.pushButton_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(520, 90, 75, 23))
        self.pushButton_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(600, 90, 75, 23))
        self.pushButton_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 125, 181, 21))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.load = QtWidgets.QPushButton(self.centralwidget)
        self.load.setGeometry(QtCore.QRect(160, 250, 611, 23))
        self.load.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.load.setObjectName("load")
        window2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 21))
        self.menubar.setObjectName("menubar")
        window2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window2)
        self.statusbar.setObjectName("statusbar")
        window2.setStatusBar(self.statusbar)

        self.retranslateUi(window2)
        QtCore.QMetaObject.connectSlotsByName(window2)
        
       
        
      

    def retranslateUi(self, window2):
        _translate = QtCore.QCoreApplication.translate
        window2.setWindowTitle(_translate("window2", "MainWindow"))
        self.pushButton.setText(_translate("window2", "Home"))
        self.pushButton_2.setText(_translate("window2", "About"))
        self.comboBox.setItemText(0, _translate("window2", "Count Sort "))
        self.comboBox.setItemText(1, _translate("window2", "Insertion Sort"))
        self.comboBox.setItemText(2, _translate("window2", "Selection Sort"))
        self.comboBox.setItemText(3, _translate("window2", "Merge Sort"))
        self.comboBox.setItemText(4, _translate("window2", "Quick Sort"))
        self.comboBox.setItemText(5, _translate("window2", "Bucket Sort"))
        self.comboBox.setItemText(6, _translate("window2", "Radix Sort"))
        self.comboBox.setItemText(7, _translate("window2", "Bubble Sort"))
        self.comboBox.setItemText(8, _translate("window2", "Hybrid Sort"))
        self.pushButton_11.setText(_translate("window2", "Search :"))
        self.pushButton_12.setText(_translate("window2", "Start"))
        self.pushButton_13.setText(_translate("window2", "Pause"))
        self.label_2.setText(_translate("window2", "Time "))
        self.load.setText(_translate("window2", "Load Data From csv"))
import image


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window2 = QtWidgets.QMainWindow()
    ui = Ui_window2()
    ui.setupUi(window2)
    window2.show()
    
    app.setApplicationName('MyWindow')
    main = MyWindow("C://Users/DEll/Documents/DSA tasks/DSA project/CS261F21PID11/scrapping/course.csv")
    main.show()
    
    sys.exit(app.exec_())
