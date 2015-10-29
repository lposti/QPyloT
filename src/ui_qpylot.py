# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qpylotwindow.ui'
#
# Created: Thu Oct 29 12:20:21 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QPyLOTWindow(object):
    def setupUi(self, QPyLOTWindow):
        QPyLOTWindow.setObjectName("QPyLOTWindow")
        QPyLOTWindow.resize(695, 543)
        self.centralWidget = QtWidgets.QWidget(QPyLOTWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 280, 115, 32))
        self.pushButton.setObjectName("pushButton")
        QPyLOTWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(QPyLOTWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 695, 22))
        self.menuBar.setObjectName("menuBar")
        QPyLOTWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(QPyLOTWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        QPyLOTWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(QPyLOTWindow)
        self.statusBar.setObjectName("statusBar")
        QPyLOTWindow.setStatusBar(self.statusBar)

        self.retranslateUi(QPyLOTWindow)
        QtCore.QMetaObject.connectSlotsByName(QPyLOTWindow)

    def retranslateUi(self, QPyLOTWindow):
        _translate = QtCore.QCoreApplication.translate
        QPyLOTWindow.setWindowTitle(_translate("QPyLOTWindow", "QPyLOTWindow"))
        self.pushButton.setText(_translate("QPyLOTWindow", "PushButton"))

