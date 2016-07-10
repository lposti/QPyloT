### ----------------------------------------------------------------------------
### plot1d.py: Plot1DWindow class definition derived from Ui_Plot1D_Window class.
###            It controls the actions on the 1D plot window
### ----------------------------------------------------------------------------

import os
import numpy as np
from PyQt5.QtWidgets import *
from ui_plot1d import Ui_Plot1D_Window
from ui_plot1d_tabw import Ui_Plot1D_tabwidget

from PyQt5 import QtWidgets

class Filein_Widget(QtWidgets.QWidget):
    # This class is just a container for a (lineedit + button Open + button Add) array
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self)        
        # GUI elements and settings
        self.parent = parent
        self.Layout = QtWidgets.QGridLayout(self)
        
        self.File_label = QtWidgets.QLabel("  File (ASCII or FITS table)  ")
        self.Layout.addWidget(self.File_label,0,0)
        self.row = 0
        self.File_lineEdit = []
        self.File_pushButton = []
        
        self.buttonGroup = [] 
        
        
        self.File_toolButton = []
        self.filename = []

        self.addFile()
       
        
    def addFile(self):
        r = len(self.File_lineEdit)
        print(r)
        self.File_lineEdit.append(QtWidgets.QLineEdit(self))
        self.Layout.addWidget(self.File_lineEdit[r],r,1)
        self.File_pushButton.append(QtWidgets.QPushButton(self))
        self.File_pushButton[r].setText("Open")
        self.Layout.addWidget(self.File_pushButton[r],r,2)
        self.File_toolButton.append(QtWidgets.QToolButton(self))
        self.File_toolButton[r].setText("+")
        
        #### MENU OK, MA BISOGNA CONNETERLO
        a = QtWidgets.QMenu(self)
        a.addAction("CAZZo")
        a.addAction("Figa")
        self.File_toolButton[r].setMenu(a)
        self.File_toolButton[r].setPopupMode(QtWidgets.QToolButton.InstantPopup)
        a.triggered.connect()
        
        
        self.Layout.addWidget(self.File_toolButton[r],r,3)
        
        
        
        self.File_pushButton[r].clicked.connect(self.openDialog)
        #self.File_toolButton[r].clicked.connect(self.addFile)
        
        if r>0:
            self.File_toolButton[r-1].setText("-")
            self.File_toolButton[r-1].clicked.disconnect()
            self.File_toolButton[r-1].clicked.connect(self.removeFile)
            
    
    def removeFile(self):
        for idx, ad in enumerate(self.File_toolButton):
            if ad==self.sender():
                self.File_lineEdit[idx].setVisible(False)
                self.File_pushButton[idx].setVisible(False)
                self.File_toolButton[idx].setVisible(False)

    
    def openDialog(self):
        # Select file 
        filename = QFileDialog.getOpenFileName(self, 'Open file')[0]
        if filename:
            for idx, ad in enumerate(self.File_pushButton):
                if ad==self.sender():
                    self.File_lineEdit[idx].setText(filename)
                    if self.parent is not None: 
                        self.parent.grancazzo() # Send a signal to parent object self.FileChanged()

class Filein_Frame(QtWidgets.QFrame):
    def __init__(self,parent=None):
        QtWidgets.QFrame.__init__(self)
        self.parent = parent
        self.Layout = QtWidgets.QGridLayout(self)

                
        self.row = -1
        self.filein_w = []
        self.addFile()
        
    def addFile(self):
        print ("gran pezzo di fica")
        self.row +=1
        self.filein_w.append(Filein_Widget(self.parent))
        self.Layout.addWidget(self.filein_w[self.row],self.row,1)
        self.filein_w[self.row].File_toolButton.clicked.connect(self.addFile)
                
        
        if self.row>0: 
            #self.filein_w[self.row-1].File_toolButton.setText("-")
            #self.filein_w[self.row-1].File_toolButton.clicked.disconnect()
            #self.filein_w[self.row-1].File_toolButton.clicked.connect(self.removeFile)
            self.filein_w[self.row-1].File_toolButton.setHidden(True)
        
        
    def removeFile(self):
        print (self.sender().name)
        

class Param ():
    def __init__(self, filename):
        fname = filename

class Plot_Tab (QWidget,Ui_Plot1D_tabwidget):
    def __init__(self, parent=None):
        super(Plot_Tab, self).__init__(parent)
        self.setupUi(self)


class Plot1DWindow(QMainWindow, Ui_Plot1D_Window):
    def __init__(self, parent=None):
        super(Plot1DWindow, self).__init__(parent)
        self.setupUi(self)
    
        self.files = []

        self.file_inp = Filein_Widget(self)
        self.Main_gridLayout.addWidget(self.file_inp,0,0,1,0)
        self.plot_tab = Plot_Tab(self)
        self.Main_gridLayout.addWidget(self.plot_tab,1,2)

        
        # Connect all the slots to the correspondent functions
        #self.File_lineEdit.editingFinished.connect(self.FileChanged)
        #self.X_file_comboBox.currentIndexChanged[int].connect(self.X_fileChanged)
        #self.Y_file_comboBox.currentIndexChanged[int].connect(self.Y_fileChanged)

    def grancazzo(self):
        print ("sta grande minchia")
            
#    def FileChanged(self):
 #       filename = self.File_lineEdit.text()
  #      filename = os.path.expanduser(filename)

        #if filename: 
        #    print (filename)
        #    self.X_file_comboBox.addItem(filename.split("/")[-1])
        #    self.Y_file_comboBox.addItem(filename.split("/")[-1])
            
            
   # def X_fileChanged(self, item): self.updateColumnComboBox(self.X_col_comboBox,item)     
   # def Y_fileChanged(self, item): self.updateColumnComboBox(self.Y_col_comboBox,item)
        
        
    
    def updateColumnComboBox(self, combobox, item):
        try:
            data = np.genfromtxt(self.files[item], names=True, autostrip=True)
            colnames = data.dtype.names
            combobox.clear()
            for cn in colnames:
                combobox.addItem(cn)
        except:
            print ("NUN CE CAPISCO")
       
        
        
        
        
        
        
        
        
