# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qpylotwindow.ui'
#
# Created: Thu Nov 12 18:18:27 2015
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_QPyLOTWindow(object):
    def setupUi(self, QPyLOTWindow):
        QPyLOTWindow.setObjectName(_fromUtf8("QPyLOTWindow"))
        QPyLOTWindow.resize(738, 558)
        self.centralWidget = QtGui.QWidget(QPyLOTWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.MaintabWidget = QtGui.QTabWidget(self.centralWidget)
        self.MaintabWidget.setObjectName(_fromUtf8("MaintabWidget"))
        self.Plot2Dtab = QtGui.QWidget()
        self.Plot2Dtab.setObjectName(_fromUtf8("Plot2Dtab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.Plot2Dtab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_2 = QtGui.QPushButton(self.Plot2Dtab)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_2.addWidget(self.pushButton_2, 4, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.Plot2Dtab)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 3, 0, 1, 1)
        self.Plot2DlistWidget = QtGui.QListWidget(self.Plot2Dtab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Plot2DlistWidget.sizePolicy().hasHeightForWidth())
        self.Plot2DlistWidget.setSizePolicy(sizePolicy)
        self.Plot2DlistWidget.setObjectName(_fromUtf8("Plot2DlistWidget"))
        item = QtGui.QListWidgetItem()
        self.Plot2DlistWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.Plot2DlistWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.Plot2DlistWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.Plot2DlistWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.Plot2DlistWidget.addItem(item)
        self.gridLayout_2.addWidget(self.Plot2DlistWidget, 0, 0, 1, 1)
        self.Plot2DstackedWidget = QtGui.QStackedWidget(self.Plot2Dtab)
        self.Plot2DstackedWidget.setObjectName(_fromUtf8("Plot2DstackedWidget"))
        self.Plot2DDatapage = QtGui.QWidget()
        self.Plot2DDatapage.setObjectName(_fromUtf8("Plot2DDatapage"))
        self.gridLayout_3 = QtGui.QGridLayout(self.Plot2DDatapage)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.Filelabel = QtGui.QLabel(self.Plot2DDatapage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Filelabel.sizePolicy().hasHeightForWidth())
        self.Filelabel.setSizePolicy(sizePolicy)
        self.Filelabel.setObjectName(_fromUtf8("Filelabel"))
        self.gridLayout_3.addWidget(self.Filelabel, 1, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 5, 1, 1, 1)
        self.Y1lineEdit = QtGui.QLineEdit(self.Plot2DDatapage)
        self.Y1lineEdit.setObjectName(_fromUtf8("Y1lineEdit"))
        self.gridLayout_3.addWidget(self.Y1lineEdit, 3, 1, 1, 1)
        self.Y1comboBox = QtGui.QComboBox(self.Plot2DDatapage)
        self.Y1comboBox.setEnabled(False)
        self.Y1comboBox.setObjectName(_fromUtf8("Y1comboBox"))
        self.gridLayout_3.addWidget(self.Y1comboBox, 3, 3, 1, 1)
        self.Y1pushButton = QtGui.QPushButton(self.Plot2DDatapage)
        self.Y1pushButton.setObjectName(_fromUtf8("Y1pushButton"))
        self.gridLayout_3.addWidget(self.Y1pushButton, 3, 2, 1, 1)
        self.Columnlabel = QtGui.QLabel(self.Plot2DDatapage)
        self.Columnlabel.setObjectName(_fromUtf8("Columnlabel"))
        self.gridLayout_3.addWidget(self.Columnlabel, 1, 3, 1, 1)
        self.X1pushButton = QtGui.QPushButton(self.Plot2DDatapage)
        self.X1pushButton.setObjectName(_fromUtf8("X1pushButton"))
        self.gridLayout_3.addWidget(self.X1pushButton, 2, 2, 1, 1)
        self.Y1label = QtGui.QLabel(self.Plot2DDatapage)
        self.Y1label.setObjectName(_fromUtf8("Y1label"))
        self.gridLayout_3.addWidget(self.Y1label, 3, 0, 1, 1)
        self.X1comboBox = QtGui.QComboBox(self.Plot2DDatapage)
        self.X1comboBox.setEnabled(False)
        self.X1comboBox.setObjectName(_fromUtf8("X1comboBox"))
        self.gridLayout_3.addWidget(self.X1comboBox, 2, 3, 1, 1)
        self.X1label = QtGui.QLabel(self.Plot2DDatapage)
        self.X1label.setObjectName(_fromUtf8("X1label"))
        self.gridLayout_3.addWidget(self.X1label, 2, 0, 1, 1)
        self.X1FilelineEdit = QtGui.QLineEdit(self.Plot2DDatapage)
        self.X1FilelineEdit.setObjectName(_fromUtf8("X1FilelineEdit"))
        self.gridLayout_3.addWidget(self.X1FilelineEdit, 2, 1, 1, 1)
        self.line = QtGui.QFrame(self.Plot2DDatapage)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_3.addWidget(self.line, 4, 0, 1, 4)
        self.Plot2DstackedWidget.addWidget(self.Plot2DDatapage)
        self.Plot2DAxespage = QtGui.QWidget()
        self.Plot2DAxespage.setObjectName(_fromUtf8("Plot2DAxespage"))
        self.gridLayout_4 = QtGui.QGridLayout(self.Plot2DAxespage)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.line_2 = QtGui.QFrame(self.Plot2DAxespage)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_4.addWidget(self.line_2, 0, 2, 1, 2)
        self.YLabellabel = QtGui.QLabel(self.Plot2DAxespage)
        self.YLabellabel.setObjectName(_fromUtf8("YLabellabel"))
        self.gridLayout_4.addWidget(self.YLabellabel, 2, 0, 1, 1)
        self.Fontlabel = QtGui.QLabel(self.Plot2DAxespage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Fontlabel.sizePolicy().hasHeightForWidth())
        self.Fontlabel.setSizePolicy(sizePolicy)
        self.Fontlabel.setObjectName(_fromUtf8("Fontlabel"))
        self.gridLayout_4.addWidget(self.Fontlabel, 3, 0, 1, 1)
        self.Labelslabel = QtGui.QLabel(self.Plot2DAxespage)
        self.Labelslabel.setObjectName(_fromUtf8("Labelslabel"))
        self.gridLayout_4.addWidget(self.Labelslabel, 0, 0, 1, 1)
        self.XLabellabel = QtGui.QLabel(self.Plot2DAxespage)
        self.XLabellabel.setObjectName(_fromUtf8("XLabellabel"))
        self.gridLayout_4.addWidget(self.XLabellabel, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 4, 2, 1, 1)
        self.XLabellineEdit = QtGui.QLineEdit(self.Plot2DAxespage)
        self.XLabellineEdit.setObjectName(_fromUtf8("XLabellineEdit"))
        self.gridLayout_4.addWidget(self.XLabellineEdit, 1, 2, 1, 2)
        self.YLabellineEdit = QtGui.QLineEdit(self.Plot2DAxespage)
        self.YLabellineEdit.setObjectName(_fromUtf8("YLabellineEdit"))
        self.gridLayout_4.addWidget(self.YLabellineEdit, 2, 2, 1, 2)
        self.LabelFonttoolButton = QtGui.QToolButton(self.Plot2DAxespage)
        self.LabelFonttoolButton.setObjectName(_fromUtf8("LabelFonttoolButton"))
        self.gridLayout_4.addWidget(self.LabelFonttoolButton, 3, 2, 1, 1)
        self.Plot2DstackedWidget.addWidget(self.Plot2DAxespage)
        self.gridLayout_2.addWidget(self.Plot2DstackedWidget, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 2, 0, 1, 1)
        self.MaintabWidget.addTab(self.Plot2Dtab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.MaintabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.MaintabWidget, 0, 0, 1, 1)
        QPyLOTWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(QPyLOTWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 738, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        QPyLOTWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(QPyLOTWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        QPyLOTWindow.setStatusBar(self.statusBar)
        self.mainToolBar = QtGui.QToolBar(QPyLOTWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        QPyLOTWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.retranslateUi(QPyLOTWindow)
        self.Plot2DstackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(QPyLOTWindow)

    def retranslateUi(self, QPyLOTWindow):
        QPyLOTWindow.setWindowTitle(_translate("QPyLOTWindow", "QPyLOT", None))
        self.pushButton_2.setText(_translate("QPyLOTWindow", "PushButton", None))
        self.pushButton.setText(_translate("QPyLOTWindow", "PushButton", None))
        __sortingEnabled = self.Plot2DlistWidget.isSortingEnabled()
        self.Plot2DlistWidget.setSortingEnabled(False)
        item = self.Plot2DlistWidget.item(0)
        item.setText(_translate("QPyLOTWindow", "Data", None))
        item = self.Plot2DlistWidget.item(1)
        item.setText(_translate("QPyLOTWindow", "Axes", None))
        item = self.Plot2DlistWidget.item(2)
        item.setText(_translate("QPyLOTWindow", "Markers", None))
        item = self.Plot2DlistWidget.item(3)
        item.setText(_translate("QPyLOTWindow", "Legend", None))
        item = self.Plot2DlistWidget.item(4)
        item.setText(_translate("QPyLOTWindow", "Text", None))
        self.Plot2DlistWidget.setSortingEnabled(__sortingEnabled)
        self.Filelabel.setText(_translate("QPyLOTWindow", "File (ASCII or FITS table)", None))
        self.Y1pushButton.setText(_translate("QPyLOTWindow", "Open", None))
        self.Columnlabel.setText(_translate("QPyLOTWindow", "Column", None))
        self.X1pushButton.setText(_translate("QPyLOTWindow", "Open", None))
        self.Y1label.setText(_translate("QPyLOTWindow", "Y", None))
        self.X1label.setText(_translate("QPyLOTWindow", "X  ", None))
        self.YLabellabel.setText(_translate("QPyLOTWindow", "Y label:", None))
        self.Fontlabel.setText(_translate("QPyLOTWindow", "Font:", None))
        self.Labelslabel.setText(_translate("QPyLOTWindow", "LABELS", None))
        self.XLabellabel.setText(_translate("QPyLOTWindow", "X label:", None))
        self.LabelFonttoolButton.setText(_translate("QPyLOTWindow", "Helvetica, 12 pt", None))
        self.MaintabWidget.setTabText(self.MaintabWidget.indexOf(self.Plot2Dtab), _translate("QPyLOTWindow", "2D Plot", None))
        self.MaintabWidget.setTabText(self.MaintabWidget.indexOf(self.tab_2), _translate("QPyLOTWindow", "Tab 2", None))

