# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/plot1d.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Plot1D_Window(object):
    def setupUi(self, Plot1D_Window):
        Plot1D_Window.setObjectName("Plot1D_Window")
        Plot1D_Window.resize(750, 629)
        self.centralWidget = QtWidgets.QWidget(Plot1D_Window)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Main_gridLayout = QtWidgets.QGridLayout()
        self.Main_gridLayout.setContentsMargins(11, 11, 11, 11)
        self.Main_gridLayout.setSpacing(6)
        self.Main_gridLayout.setObjectName("Main_gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setObjectName("listWidget")
        self.Main_gridLayout.addWidget(self.listWidget, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Main_gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.horizontalLayout.addLayout(self.Main_gridLayout)
        Plot1D_Window.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(Plot1D_Window)
        self.mainToolBar.setOrientation(QtCore.Qt.Horizontal)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.mainToolBar.setObjectName("mainToolBar")
        Plot1D_Window.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(Plot1D_Window)
        self.statusBar.setObjectName("statusBar")
        Plot1D_Window.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(Plot1D_Window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 750, 22))
        self.menuBar.setObjectName("menuBar")
        Plot1D_Window.setMenuBar(self.menuBar)

        self.retranslateUi(Plot1D_Window)
        QtCore.QMetaObject.connectSlotsByName(Plot1D_Window)

    def retranslateUi(self, Plot1D_Window):
        _translate = QtCore.QCoreApplication.translate
        Plot1D_Window.setWindowTitle(_translate("Plot1D_Window", "QPyLOT - Plot 1D"))

