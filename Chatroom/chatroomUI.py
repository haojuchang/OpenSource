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
        MainWindow.resize(700, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #----------- current persons label--------------------------------------------------------------------------
        self.cur_person = QtWidgets.QLabel(self.centralwidget)
        self.cur_person.setGeometry(QtCore.QRect(10, 10, 60, 20))
        self.cur_person.setObjectName("cur_person")
        #----------- nickname label----------------------------------------------------------------------------------
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 60, 40))
        self.label.setObjectName("label")
        #------------nickname edit
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 40, 180, 50))
        self.lineEdit_2.setObjectName("lineEdit_2")
        #------------nickname password edit
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(260, 40, 180, 50))
        self.password.setObjectName("password")
        #---------login button
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 40, 180, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        #----------- change password label------------------------------------------------------------------------
        self.cp = QtWidgets.QLabel(self.centralwidget)
        self.cp.setGeometry(QtCore.QRect(10, 100, 80, 40))
        self.cp.setObjectName("cp")
        #------------change password edit
        self.ch_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.ch_pass.setGeometry(QtCore.QRect(100, 100, 340, 50))
        self.ch_pass.setObjectName("ch_pass")
        #---------update password button
        self.up_pass = QtWidgets.QPushButton(self.centralwidget)
        self.up_pass.setGeometry(QtCore.QRect(450, 100, 180, 50))
        self.up_pass.setObjectName("up_pass")
        #---------text browser---------------------------------------------------------------------------------------
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 170, 620, 300))
        self.textBrowser.setObjectName("textBrowser")
        #----------message box----------------------------------------------------------------------------------------
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 480, 620, 40))
        #---------send button-----------------------------------------------------------------------------------
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 530, 620, 50))
        self.pushButton.setObjectName("pushButton")
        #----------------------------------------------------------------------------------------------
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 371, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chat Application"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "Login"))
        self.up_pass.setText(_translate("MainWindow", "update password"))
        self.label.setText(_translate("MainWindow", "NickName"))
        self.cp.setText(_translate("MainWindow", "change password"))
        self.cur_person.setText(_translate("MainWindow", "cur_person"))


