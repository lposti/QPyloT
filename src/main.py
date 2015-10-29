import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_qpylot import Ui_QPyLOTWindow

class MainWindow(QMainWindow, Ui_QPyLOTWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)                                         
		self.setupUi(self)
		
		self.pushButton.clicked.connect(self.chk_fun)
		
	def chk_fun(self):
		print("Good.")

if __name__ == '__main__':
	app = QApplication(sys.argv)
	frame = MainWindow()
	frame.show()
	app.exec_()
	
	
	

	    