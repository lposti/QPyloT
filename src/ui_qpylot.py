# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qpylotwindow.ui'
#
# Created: Thu Oct 29 13:00:51 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QPyLOTWindow(object):
    def setupUi(self, QPyLOTWindow):
        QPyLOTWindow.setObjectName("QPyLOTWindow")
        QPyLOTWindow.resize(743, 524)
        self.centralWidget = QtWidgets.QWidget(QPyLOTWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.MaintabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.MaintabWidget.setObjectName("MaintabWidget")
        self.Plot1Dtab = QtWidgets.QWidget()
        self.Plot1Dtab.setObjectName("Plot1Dtab")
        self.MaintabWidget.addTab(self.Plot1Dtab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.MaintabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.MaintabWidget, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        QPyLOTWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(QPyLOTWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 743, 22))
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
        self.MaintabWidget.setTabText(self.MaintabWidget.indexOf(self.Plot1Dtab), _translate("QPyLOTWindow", "Tab 1"))
        self.MaintabWidget.setTabText(self.MaintabWidget.indexOf(self.tab_2), _translate("QPyLOTWindow", "Tab 2"))
        self.pushButton.setText(_translate("QPyLOTWindow", "PushButton"))

