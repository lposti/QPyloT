# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/start_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Start_Window(object):
    def setupUi(self, Start_Window):
        Start_Window.setObjectName("Start_Window")
        Start_Window.resize(583, 225)
        self.centralWidget = QtWidgets.QWidget(Start_Window)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_plot1d = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_plot1d.setObjectName("pushButton_plot1d")
        self.gridLayout.addWidget(self.pushButton_plot1d, 0, 0, 1, 1)
        self.pushButton_plot2d = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_plot2d.setObjectName("pushButton_plot2d")
        self.gridLayout.addWidget(self.pushButton_plot2d, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        Start_Window.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Start_Window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 583, 27))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        Start_Window.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(Start_Window)
        self.mainToolBar.setMovable(True)
        self.mainToolBar.setIconSize(QtCore.QSize(28, 28))
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        Start_Window.addToolBar(QtCore.Qt.LeftToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(Start_Window)
        self.statusBar.setObjectName("statusBar")
        Start_Window.setStatusBar(self.statusBar)
        self.actionQuit = QtWidgets.QAction(Start_Window)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Start_Window)
        self.actionQuit.triggered.connect(Start_Window.close)
        self.pushButton_3.clicked.connect(self.pushButton_plot1d.showMenu)
        QtCore.QMetaObject.connectSlotsByName(Start_Window)

    def retranslateUi(self, Start_Window):
        _translate = QtCore.QCoreApplication.translate
        Start_Window.setWindowTitle(_translate("Start_Window", "QPyLOT"))
        self.pushButton_plot1d.setText(_translate("Start_Window", "Plot 1D"))
        self.pushButton_plot2d.setText(_translate("Start_Window", "PushButton"))
        self.pushButton_3.setText(_translate("Start_Window", "PushButton"))
        self.menuFile.setTitle(_translate("Start_Window", "File"))
        self.actionQuit.setText(_translate("Start_Window", "Quit"))

