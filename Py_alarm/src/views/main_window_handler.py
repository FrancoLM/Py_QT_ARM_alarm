# -*- coding: utf-8 -*-

'''
Created on Jan 20, 2014

@author: fmartinez1
'''
import sys
from PySide.QtGui import QMainWindow, QApplication
from main_window_gui import Ui_MainWindow

from temperature_plot import Temperature_graph


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        
        #Creates the UI made with Qt Designer
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height()) # Can't be resized
        
        #=======================================================================
        #  Add the plot to the main window
        #=======================================================================
        self.figure = Temperature_graph()
        #Set the canvas to the Main Window frame to that of the figure
        self.frame.setLayout(self.figure.get_layout())
        
        #=======================================================================
        # Signal connections
        #=======================================================================
        self.action_exit_app.triggered.connect(self.quit_application)
        
    
        #=======================================================================
        #=======================================================================
    
    #===========================================================================
    #===========================================================================
    # # 
    #===========================================================================
    #===========================================================================
    
    def set_queue(self, temperature_queue):
        '''
        This method is called by the Controller.
        It connects the Model queue to the View so the View
        can plot it in a graph.
        '''
        self.figure.set_graph_queue(temperature_queue)
    
    
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
    main.set_queue(temperature_queue = None)
    
    main.show()
    

    sys.exit(app.exec_())