


import sys,subprocess
from PyQt5.QtWidgets import *

from ui_start import Ui_Start_Window
from plot1d import Plot1DWindow

from ui_qpylot import Ui_QPyLOTWindow


def open_file(filename):
    if sys.platform.startswith('darwin'):
        subprocess.call(('open', filename))
    elif os.name == 'nt':
        os.startfile(filepath)
    elif os.name == 'posix':
        subprocess.call(('xdg-open', filename))


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
        
    






class Plot2DWindow(QMainWindow, Ui_QPyLOTWindow):
    def __init__(self, parent=None):
        super(Plot2DWindow, self).__init__(parent)
        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = StartWindow()
    frame.show()
    app.exec_()
	
	
	

	    
