# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot1d_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Plot1D_Window(object):
    def setupUi(self, Plot1D_Window):
        Plot1D_Window.setObjectName("Plot1D_Window")
        Plot1D_Window.resize(519, 395)
        self.centralWidget = QtWidgets.QWidget(Plot1D_Window)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.File_lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.File_lineEdit.setObjectName("File_lineEdit")
        self.gridLayout.addWidget(self.File_lineEdit, 0, 2, 1, 1)
        self.File_label = QtWidgets.QLabel(self.centralWidget)
        self.File_label.setObjectName("File_label")
        self.gridLayout.addWidget(self.File_label, 0, 1, 1, 1)
        self.File_pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.File_pushButton.setObjectName("File_pushButton")
        self.gridLayout.addWidget(self.File_pushButton, 0, 3, 1, 1)
        Plot1D_Window.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(Plot1D_Window)
        self.mainToolBar.setOrientation(QtCore.Qt.Vertical)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.mainToolBar.setObjectName("mainToolBar")
        Plot1D_Window.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(Plot1D_Window)
        self.statusBar.setObjectName("statusBar")
        Plot1D_Window.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(Plot1D_Window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 519, 27))
        self.menuBar.setObjectName("menuBar")
        Plot1D_Window.setMenuBar(self.menuBar)
        self.actionAaa = QtWidgets.QAction(Plot1D_Window)
        self.actionAaa.setObjectName("actionAaa")

        self.retranslateUi(Plot1D_Window)
        QtCore.QMetaObject.connectSlotsByName(Plot1D_Window)

    def retranslateUi(self, Plot1D_Window):
        _translate = QtCore.QCoreApplication.translate
        Plot1D_Window.setWindowTitle(_translate("Plot1D_Window", "QPyLOT - Plot 1D"))
        self.File_label.setText(_translate("Plot1D_Window", "Source"))
        self.File_pushButton.setText(_translate("Plot1D_Window", "Open"))
        self.actionAaa.setText(_translate("Plot1D_Window", "aaa"))

