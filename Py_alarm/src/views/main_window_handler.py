# -*- coding: utf-8 -*-

'''
Created on Jan 20, 2014

@author: fmartinez1
'''
import sys
from PySide.QtGui import QMainWindow, QApplication, QHBoxLayout, QWidget
from main_window_gui import Ui_MainWindow

#matplotlib imports
import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

import numpy as np


#-------------------
import time


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        
        
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        
        
        self.add_plot()
        
        
        #=======================================================================
        # Signal connections
        #=======================================================================
        self.action_exit_app.triggered.connect(self.quit_application)
        
    
        #=======================================================================
        #=======================================================================
    
    def add_plot(self):
        '''
        This method adds the matplotlib pyplot to the UI.
        It fits the plot inside a layout, which is then set to a QFrame.
        '''
        
        # a figure instance to plot on
        self.figure = plt.figure()
        
        # this is the Canvas Widget that displays the `figure`
        self.canvas = FigureCanvas(self.figure)
        
        #Add a timer to redraw the graph
        self.plot_timer = self.canvas.new_timer(interval=100)
        self.plot_timer.add_callback(self.redraw_graph)
        
        
        #Create the layout for the frame
        self.layout = QHBoxLayout()
        
        #Add the Figure to the layout
        self.layout.addWidget(self.canvas)
        
        self.layout.setStretchFactor(self.canvas, 1)
        
        #Set the canvas to the Main Window frame
        self.frame.setLayout(self.layout)
        
        #self.redraw_graph()
        
        ###########
        self.plot_timer.start()
        
    def redraw_graph(self):
        '''
        This method redraws the graph. It's called everytime the plot_timer
        reaches zero.
        '''
        print "I enter here..."
        mu, sigma = 100, 15
        x = mu + sigma * np.random.randn(1000)
        
        # the histogram of the data
        n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
        
        
        plt.xlabel('Smarts')
        plt.ylabel('Probability')
        #plt.title('Histogram of IQ')
        #plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
        plt.axis([40, 160, 0, 0.03])
        plt.grid(True)
        plt.draw()
        #plt.show()
    
    
    def quit_application(self):
        '''
        This method closes the application.
        sys.exit is not the best way to close it... improve this.
        '''
        sys.exit(0)

if __name__ == '__main__':
    #Interfaz de usuario
    app = QApplication(sys.argv)

    main = MainWindow()
    
    main.show()
    

    sys.exit(app.exec_())