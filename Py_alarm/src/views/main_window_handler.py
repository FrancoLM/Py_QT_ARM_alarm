# -*- coding: utf-8 -*-

'''
Created on Jan 20, 2014

@author: fmartinez1
'''
import sys
from PySide.QtGui import QMainWindow, QApplication
from main_window_gui import Ui_MainWindow
from PySide.QtCore import Signal

from temperature_plot import Temperature_graph
from views.max_temp_dialog_handler import Max_temp_dialog


class MainWindow(QMainWindow, Ui_MainWindow):
    
    
    new_max_temp_signal = Signal(int)
    close_app_signal = Signal()
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        
        #Creates the UI made with Qt Designer
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height()) # Can't be resized
        
        #Set the alarm button's initial state to invisible 
        self.deactivate_alarm_button.setVisible(False)
        
        #=======================================================================
        #  Add the plot to the main window
        #=======================================================================
        self.figure = Temperature_graph()
        #Set the canvas to the Main Window frame to that of the figure
        self.frame.setLayout(self.figure.get_layout())
        
        #=======================================================================
        # Signal connections
        #=======================================================================
        # When I click on the deactivate alarm button,
        self.actionDesactivar_alarma.triggered.connect(self.turn_off_alarm_action)
        
        # Open new max temperature dialog
        self.set_max_temp_button.clicked.connect(self.show_max_temp_dialog)
        self.action_set_new_max_temp.triggered.connect(self.show_max_temp_dialog)
        
        
        
        self.action_exit_app.triggered.connect(self.quit_application)
        #=======================================================================
        #=======================================================================
    
    #===========================================================================
    #===========================================================================
    # # 
    #===========================================================================
    #===========================================================================
    
    def show_max_temp_dialog(self):
        max_temp_dialog = Max_temp_dialog()
        max_temp_dialog.exec_()
        
        try: # Accept
            self.new_max_temp_signal.emit(int(max_temp_dialog.lineEdit.text()))
        except: # Cancel
            self.new_max_temp_signal.emit(int(self.max_temp_value.text()))
        #self.max_temp_value.setText(max_temp_dialog.lineEdit.text())
        #max_temp_dialog.new_max_temp_signal.connect(self.max_temp_value.setText)
    
    
    def update_max_temp_ui(self, new_value):
        self.max_temp_value.setText(str(new_value))
        #print "max temp UI updated"
    
    def update_current_temp_ui(self, new_value):
        self.current_temp_value.setText(new_value)
    
    def turn_off_alarm_action(self):
        self.change_alarm_window_style(False)
    
    
    def set_queue(self, temperature_queue):
        '''
        This method is called by the Controller.
        It connects the Model queue to the View so the View
        can plot it in a graph.
        '''
        self.figure.set_graph_queue(temperature_queue)
    
    def change_alarm_window_style(self, alarm_on):
        '''
        This method updates the main window's Stylesheet
        when the alarm is activated.
        '''
        if alarm_on:
            # Alarm is activated
            self.actionDesactivar_alarma.setEnabled(True)
            self.main_frame.setStyleSheet("QFrame#main_frame{\n"
                "    background-color: rgb(255, 140, 142);\n"
                "}\n"
                "\n"
                "QFrame{\n"
                "    background-color: rgb(250, 250, 250);\n"
                "}\n"
                "")
            self.deactivate_alarm_button.setVisible(True)
        
        else:
            # Alarm is deactivated
            self.actionDesactivar_alarma.setEnabled(False)
            self.main_frame.setStyleSheet("QFrame#main_frame{\n"
                "    background-color: rgb(226, 226, 226);\n"
                "}\n"
                "\n"
                "QFrame{\n"
                "    background-color: rgb(250, 250, 250);\n"
                "}\n"
                "")
            self.deactivate_alarm_button.setVisible(False)
    
       
    def quit_application(self):
        '''
        This method closes the application.
        '''
        self.close()
        #sys.exit(0)
        
    #Overloaded method
    def closeEvent(self, event):
        '''
        This is an overload call to the closeEvent method, because besides
        closing the app, we need to close the Serial port.
        The emmited signal calls the serial_communication.close_port() method.
        '''
        print "Closing application..."
        
        #Emit close application signal
        self.close_app_signal.emit()
        
        event.accept() # let the window close


if __name__ == '__main__':
    # Used to test the UI
    app = QApplication(sys.argv)

    main = MainWindow()
    main.set_queue(temperature_queue = None)
    
    main.show()
    

    sys.exit(app.exec_())