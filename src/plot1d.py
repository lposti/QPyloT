### ----------------------------------------------------------------------------
### plot1d.py: Plot1DWindow class definition derived from Ui_Plot1D_Window class.
###            It controls the actions on the 1D plot window
### ----------------------------------------------------------------------------

from PyQt5.QtWidgets import *
from ui_plot1d import Ui_Plot1D_Window



class Plot1DWindow(QMainWindow, Ui_Plot1D_Window):
    def __init__(self, parent=None):
        super(Plot1DWindow, self).__init__(parent)
        self.setupUi(self)

        # Connect all the slots to the correspondent functions
        self.File_pushButton.clicked.connect(self.openDialog)
        self.File_lineEdit.editingFinished.connect(self.FileChanged)

    def openDialog(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file')
        if filename:
            self.File_lineEdit.setText(filename[0])
            self.FileChanged()

    def FileChanged(self):
        filename = self.File_lineEdit.text()
        if filename:
            print (filename)

