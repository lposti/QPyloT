###----------------------------------------------------------------------------
### mpl_canvas.py: create matplotlib canvases as a Qt5 window
###                Used for plotting windows.
###                It is edited from http://matplotlib.org/examples/user_interfaces/embedding_in_qt5.html
###----------------------------------------------------------------------------

import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
import sys
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pylab as plt

class Base1DPlotWindow():
    """Abstract Base class for 1D Plot Windows"""
    def __init__(self):
        """Initialize all needed data to make plot"""

        # get lists of x & y arrays
        self.x, self.y           = self._get_xy()

        # How many points collections to plot?
        self.nplots = 0
        if (isinstance(self.x, list) and isinstance(self.y, list)):
            # check if x & y are lists
            if (isinstance(self.x[0], list) and isinstance(self.y[0], list)):
                if (len(self.x) == len(self.y) and len(self.x)>1):
                    # check that x & y have same size
                    # check if we have more than one data collection
                    self.nplots = len(self.x)

                else:
                    raise ValueError("some problem: len(x)=%d len(y)=%d" % (len(self.x), len(self.y)))
            else:
                self.nplots = 1
        else:
            raise NotImplementedError("x & y must be lists")

        for i in range(self.nplots):
            assert(len(self.x[i]) == len(self.y[i]))  # check that all data collection have x & y with same size

        # get lists of markers and colors
        self.markers, self.colors = self._get_markers_and_colors()
        assert(len(self.markers) == self.nplots)  # sanity check on sizes
        assert(len(self.colors)  == self.nplots)

        # get labels for each data collection
        self.datalabels = self._get_datalabels()
        assert(len(self.datalabels) == self.nplots)  # sanity check on sizes

        self.xlabel, self.ylabel = self._get_xylabels()

    def plot(self, fig=None, ax=None, fontsize=14, lw=2, ms=6, legend=True, noshow=False):
        """
        Plotting routine.
        Depends on self._get_xy()
                   self._get_markers_and_colors()
                   self._get_datalabels()
                   self._get_xylabels()
        """

        # get current figure and axis
        if (fig is None and ax is None):
            fig, ax = plt.gcf(), plt.gca()

        self.fig, self.ax = fig, ax

        # plot data collections
        for i in range(self.nplots):
            self.ax.plot(self.x[i], self.y[i], marker=self.markers[i], color=self.colors[i], label=self.datalabels[i],
                         linewidth=lw, markersize=ms)

        # set plot labels
        self.ax.set_xlabel(self.xlabel, fontsize=fontsize)
        self.ax.set_ylabel(self.ylabel, fontsize=fontsize)

        if legend:
            self.ax.legend(loc='best', frameon=False, fontsize=fontsize)

        if ~noshow:
            plt.show()

    def _get_xy(self):
        """
        Return a tuple of two lists.
        x & y: lists of arrays (or lists)
        """
        pass

    def _get_markers_and_colors(self):
        """
        Return a tuple of two lists.
        markers & colors: lists of strings
        """
        pass

    def _get_datalabels(self):
        """Return a list of strings: labels for each data collection"""
        pass

    def _get_xylabels(self):
        """Return a tuple of two strings: xlabel, ylabel"""
        pass


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)

        self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""

    def compute_initial_figure(self):
        # t = arange(0.0, 3.0, 0.01)
        # s = sin(2*pi*t)
        # self.axes.plot(t, s)

        p = Plot1DWindow()
        p.plot(fig=self.fig, ax=self.axes, noshow=True)


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QtWidgets.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QtWidgets.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        self.main_widget = QtWidgets.QWidget(self)

        l = QtWidgets.QVBoxLayout(self.main_widget)
        sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        l.addWidget(sc)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("First 1D plot!", 2000)

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QtWidgets.QMessageBox.about(self, "About", """about""")


from numpy import arange
class Plot1DWindow(Base1DPlotWindow):

    def _get_xy(self):
        return [arange(10)], [arange(10)/2.]

    def _get_markers_and_colors(self):
        return ['o'], ['b']

    def _get_datalabels(self):
        return ["line"]

    def _get_xylabels(self):
        return "XXX", "YYY"


qApp = QtWidgets.QApplication(sys.argv)

aw = ApplicationWindow()
aw.setWindowTitle("%s" % sys.argv[0])
aw.show()
sys.exit(qApp.exec_())
