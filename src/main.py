from PyQt5.QtWidgets import *



import sys
from ui_start import Ui_Start_Window
from ui_plot1d import Ui_Plot1D_Window


from ui_qpylot import Ui_QPyLOTWindow

class StartWindow(QMainWindow, Ui_Start_Window):
    def __init__(self, parent=None):
        super(StartWindow, self).__init__(parent)
        self.setupUi(self)
        self.plot1d_w = None
        self.plot2d_w = None


        self.pushButton_plot1d.clicked.connect(self.openPlot1D_Window)
        self.pushButton_plot2d.clicked.connect(self.openPlot2D_Window)

        
    def openPlot1D_Window(self):
        if self.plot1d_w is None:
            self.plot1d_w = Plot1DWindow(self)
        self.plot1d_w.show()

    def openPlot2D_Window(self):
        if self.plot2d_w is None:
            self.plot2d_w = Plot2DWindow(self)
        self.plot2d_w.show()


    def chk_fun(self):
	    print("Good.")



class Plot1DWindow(QMainWindow, Ui_Plot1D_Window):
    def __init__(self, parent=None):
        super(Plot1DWindow, self).__init__(parent)
        self.setupUi(self)

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




class Plot2DWindow(QMainWindow, Ui_QPyLOTWindow):
    def __init__(self, parent=None):
        super(Plot2DWindow, self).__init__(parent)
        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = StartWindow()
    frame.show()
    app.exec_()
	
	
	

	    
