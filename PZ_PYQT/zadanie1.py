# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zadanie1.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.btn = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(619, 551)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.speed_text = QtWidgets.QLabel(self.centralwidget)
        self.speed_text.setGeometry(QtCore.QRect(190, 140, 111, 41))
        self.speed_text.setObjectName("speed_text")
        self.ugol_text = QtWidgets.QLabel(self.centralwidget)
        self.ugol_text.setGeometry(QtCore.QRect(190, 180, 91, 71))
        self.ugol_text.setObjectName("ugol_text")
        self.speed = QtWidgets.QLineEdit(self.centralwidget)
        self.speed.setGeometry(QtCore.QRect(290, 150, 113, 22))
        self.speed.setObjectName("speed")
        self.ugol = QtWidgets.QLineEdit(self.centralwidget)
        self.ugol.setGeometry(QtCore.QRect(290, 210, 113, 22))
        self.ugol.setObjectName("ugol")
        self.pb = QtWidgets.QPushButton(self.centralwidget)
        self.pb.setGeometry(QtCore.QRect(190, 270, 211, 81))
        self.pb.setObjectName("pb")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 619, 26))
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
        self.speed_text.setText(_translate("MainWindow", "Скорость м/c:"))
        self.ugol_text.setText(_translate("MainWindow", "Угол броска "))
        self.pb.setText(_translate("MainWindow", "Построить траекторию"))
