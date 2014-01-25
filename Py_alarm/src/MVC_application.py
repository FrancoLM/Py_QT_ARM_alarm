'''
Created on 23/01/2014

@author: Franco

This is the main script, which creates the MVC components and initiates and connects them.
'''

from models.alarm import Alarm
from models.temperature import Max_temp, Current_temp
from models.serial_communication import Serial_communication
from models.temperature_queue import Temp_queue
from models.app_model import App_model
import time

import sys
from PySide.QtGui import QMainWindow, QApplication
from views.main_window_handler import MainWindow
    
if __name__ == "__main__":

    #===========================================================================
    # Instantiate the Model
    #===========================================================================
    app_model = App_model(queue_size = 20, initial_max_temp = 22)
    
    #===========================================================================
    # Start the View (UI) objects
    #===========================================================================
    q_app = QApplication(sys.argv)

    #I shouldn't pass the queue to the View this way....
    main = MainWindow(temp_queue = app_model.temp_queue)
    
    
    
    #===========================================================================
    # Start the Controller
    #===========================================================================
    
    
    
    
    #===========================================================================
    # Show the View
    #===========================================================================
    main.show()
    
    #set sys.exit (required by QApplication)
    sys.exit(q_app.exec_())
    
    
    while True:
        time.sleep(10)