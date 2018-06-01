# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(367, 634)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.below_btn = QtWidgets.QPushButton(self.centralwidget)
        self.below_btn.setGeometry(QtCore.QRect(10, 560, 351, 31))
        self.below_btn.setObjectName("below_btn")
        self.textbody = QtWidgets.QTextBrowser(self.centralwidget)
        self.textbody.setEnabled(True)
        self.textbody.setGeometry(QtCore.QRect(10, 90, 351, 461))
        self.textbody.setObjectName("textbody")
        self.nickname_input = QtWidgets.QLineEdit(self.centralwidget)
        self.nickname_input.setGeometry(QtCore.QRect(60, 20, 111, 21))
        self.nickname_input.setObjectName("nickname_input")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(10, 50, 351, 31))
        self.add.setObjectName("add")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 19, 51, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 20, 41, 20))
        self.label_2.setObjectName("label_2")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(230, 20, 121, 21))
        self.password_input.setObjectName("password_input")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 367, 22))
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
        self.below_btn.setText(_translate("MainWindow", "PushButton"))
        self.add.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "NickName"))
        self.label_2.setText(_translate("MainWindow", "Password"))


    def showbox(self, name, sort):
        x = 30
        y = 90
        wid = 73
        len = 16
        y = y + len * sort
        _translate = QtCore.QCoreApplication.translate
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(x, y, wid, len))
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName(name)
        self.checkBox.setText(_translate("MainWindow", name))

