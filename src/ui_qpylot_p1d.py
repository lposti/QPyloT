# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qpylot_p1d_window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QPyLOT_p1d_Window(object):
    def setupUi(self, QPyLOT_p1d_Window):
        QPyLOT_p1d_Window.setObjectName("QPyLOT_p1d_Window")
        QPyLOT_p1d_Window.resize(519, 395)
        self.centralWidget = QtWidgets.QWidget(QPyLOT_p1d_Window)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        QPyLOT_p1d_Window.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(QPyLOT_p1d_Window)
        self.mainToolBar.setObjectName("mainToolBar")
        QPyLOT_p1d_Window.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(QPyLOT_p1d_Window)
        self.statusBar.setObjectName("statusBar")
        QPyLOT_p1d_Window.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(QPyLOT_p1d_Window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 519, 22))
        self.menuBar.setObjectName("menuBar")
        QPyLOT_p1d_Window.setMenuBar(self.menuBar)

        self.retranslateUi(QPyLOT_p1d_Window)
        QtCore.QMetaObject.connectSlotsByName(QPyLOT_p1d_Window)

    def retranslateUi(self, QPyLOT_p1d_Window):
        _translate = QtCore.QCoreApplication.translate
        QPyLOT_p1d_Window.setWindowTitle(_translate("QPyLOT_p1d_Window", "QPyLOT"))

