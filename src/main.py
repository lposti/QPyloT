import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from ui_qpylot import Ui_QPyLOTWindow
from ui_qpylot_p1d import Ui_QPyLOT_p1d_Window


class MainWindow(QMainWindow, Ui_QPyLOTWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)                                         
        self.setupUi(self)
        self.window2 = None



        self.pushButton_3.clicked.connect(self.handleButton)
        
    def handleButton(self):
        if self.window2 is None:
            self.window2 = Form2(self)
        self.window2.show()

    def chk_fun(self):
	    print("Good.")

class Form2(QMainWindow, Ui_QPyLOT_p1d_Window):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	frame = MainWindow()
	frame.show()
	app.exec_()  
	
	
	

	    