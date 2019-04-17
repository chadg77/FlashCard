# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flashCard_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1052, 621)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cardList = QtWidgets.QListWidget(self.centralwidget)
        self.cardList.setGeometry(QtCore.QRect(40, 40, 141, 481))
        self.cardList.setObjectName("cardList")
        self.currentCard = QtWidgets.QTextEdit(self.centralwidget)
        self.currentCard.setGeometry(QtCore.QRect(210, 70, 641, 251))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(144)
        font.setBold(True)
        font.setWeight(75)
        self.currentCard.setFont(font)
        self.currentCard.setReadOnly(False)
        self.currentCard.setObjectName("currentCard")
        self.nextCard = QtWidgets.QPushButton(self.centralwidget)
        self.nextCard.setGeometry(QtCore.QRect(560, 350, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.nextCard.setFont(font)
        self.nextCard.setObjectName("nextCard")
        self.repeatList = QtWidgets.QListWidget(self.centralwidget)
        self.repeatList.setGeometry(QtCore.QRect(880, 40, 131, 491))
        self.repeatList.setObjectName("repeatList")
        self.repeatCard = QtWidgets.QPushButton(self.centralwidget)
        self.repeatCard.setGeometry(QtCore.QRect(310, 350, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.repeatCard.setFont(font)
        self.repeatCard.setObjectName("repeatCard")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(900, 20, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 20, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nextCard.setText(_translate("MainWindow", "NEXT CARD"))
        self.repeatCard.setText(_translate("MainWindow", "REPEAT CARD"))
        self.label.setText(_translate("MainWindow", "Repeat Cards"))
        self.label_2.setText(_translate("MainWindow", "Card List"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
