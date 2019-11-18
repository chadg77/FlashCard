# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flashCard_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1052, 621)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.currentCard = QtWidgets.QTextEdit(self.centralwidget)
        self.currentCard.setGeometry(QtCore.QRect(20, 100, 871, 351))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(144)
        font.setBold(True)
        font.setWeight(75)
        self.currentCard.setFont(font)
        self.currentCard.setReadOnly(False)
        self.currentCard.setObjectName("currentCard")
        self.nextCard = QtWidgets.QPushButton(self.centralwidget)
        self.nextCard.setGeometry(QtCore.QRect(320, 480, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.nextCard.setFont(font)
        self.nextCard.setStyleSheet("background-color: rgb(98, 171, 255);")
        self.nextCard.setObjectName("nextCard")
        self.repeatList = QtWidgets.QListWidget(self.centralwidget)
        self.repeatList.setGeometry(QtCore.QRect(910, 100, 131, 351))
        self.repeatList.setObjectName("repeatList")
        self.repeatCard = QtWidgets.QPushButton(self.centralwidget)
        self.repeatCard.setGeometry(QtCore.QRect(60, 480, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.repeatCard.setFont(font)
        self.repeatCard.setStyleSheet("background-color: rgb(253, 135, 157);")
        self.repeatCard.setObjectName("repeatCard")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(930, 70, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.selectList = QtWidgets.QPushButton(self.centralwidget)
        self.selectList.setGeometry(QtCore.QRect(20, 30, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.selectList.setFont(font)
        self.selectList.setAutoFillBackground(False)
        self.selectList.setStyleSheet("background-color: rgb(179, 179, 179)")
        self.selectList.setObjectName("selectList")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1052, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Flashcards"))
        self.nextCard.setText(_translate("MainWindow", "NEXT CARD"))
        self.repeatCard.setText(_translate("MainWindow", "REPEAT CARD"))
        self.label.setText(_translate("MainWindow", "Repeat Cards"))
        self.selectList.setText(_translate("MainWindow", "Select Card List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

