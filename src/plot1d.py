### ----------------------------------------------------------------------------
### plot1d.py: Plot1DWindow class definition derived from Ui_Plot1D_Window class.
###            It controls the actions on the 1D plot window
### ----------------------------------------------------------------------------

import os
import numpy as np
from PyQt5.QtWidgets import *
from ui_plot1d import Ui_Plot1D_Window


class Param ():
    def __init__(self, filename):
        fname = filename
    


class Plot1DWindow(QMainWindow, Ui_Plot1D_Window):
    def __init__(self, parent=None):
        super(Plot1DWindow, self).__init__(parent)
        self.setupUi(self)
    
        self.files = []
        
        # Connect all the slots to the correspondent functions
        self.File_pushButton.clicked.connect(self.openDialog)
        self.File_lineEdit.editingFinished.connect(self.FileChanged)
        self.X_file_comboBox.currentIndexChanged[int].connect(self.X_fileChanged)
        self.Y_file_comboBox.currentIndexChanged[int].connect(self.Y_fileChanged)

    def openDialog(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file')
        if filename:
            self.files.append(filename[0])
            self.File_lineEdit.setText(self.files[-1])
            self.FileChanged()

            


    def FileChanged(self):
        filename = self.File_lineEdit.text()
        filename = os.path.expanduser(filename)

        if filename: 
            print (filename)
            self.X_file_comboBox.addItem(filename.split("/")[-1])
            self.Y_file_comboBox.addItem(filename.split("/")[-1])
            
            
    def X_fileChanged(self, item): self.updateColumnComboBox(self.X_col_comboBox,item)     
    def Y_fileChanged(self, item): self.updateColumnComboBox(self.Y_col_comboBox,item)
        
        
    
    def updateColumnComboBox(self, combobox, item):
        try:
            data = np.genfromtxt(self.files[item], names=True, autostrip=True)
            colnames = data.dtype.names
            combobox.clear()
            for cn in colnames:
                combobox.addItem(cn)
        except:
            print ("NUN CE CAPISCO")
       
        
        
        
        
        
        
        
        
