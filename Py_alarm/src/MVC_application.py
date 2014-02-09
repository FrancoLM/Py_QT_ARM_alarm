'''
Created on 23/01/2014

@author: Franco

This is the main script, which instantiates the MVC components and connects them.
'''

from models.alarm import Alarm
from models.app_model import App_model
#import time

import sys
from PySide.QtGui import QApplication
from views.main_window_handler import MainWindow
from controllers.main_controller import App_controller
    
if __name__ == "__main__":
    
    #QApplication object: neccesary to run PySide applications
    q_app = QApplication(sys.argv)
    
    
    #===========================================================================
    # Instantiate the Model
    #===========================================================================
    # I need to read this max temp from the HW 
    app_model = App_model(queue_size = 20, initial_max_temp = 33)
    
    
    #===========================================================================
    # Instantiate the View (UI)
    #===========================================================================
    main_window_view = MainWindow()
    
    
    #===========================================================================
    # Instantiate the Controller
    #===========================================================================
    app_controller = App_controller(app_model, main_window_view)
    
    
    #===========================================================================
    # Show the View
    #===========================================================================
    main_window_view.show()
    
    #set sys.exit (required by QApplication)
    sys.exit(q_app.exec_())
    
    
