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
from models.temperature import Max_temp


class MainWindow(QMainWindow, Ui_MainWindow):
    
    
    new_max_temp_signal = Signal(int)
    
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
        # When I click on the deactivate alarm button,
        self.actionDesactivar_alarma.triggered.connect(self.turn_off_alarm_action)
        
        # Open new max temperature dialog
        self.set_max_temp_button.clicked.connect(self.show_max_temp_dialog)
        self.action_set_new_max_temp.triggered.connect(self.show_max_temp_dialog)
        
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
        
        self.new_max_temp_signal.emit(int(max_temp_dialog.lineEdit.text()))
        #self.max_temp_value.setText(max_temp_dialog.lineEdit.text())
        #max_temp_dialog.new_max_temp_signal.connect(self.max_temp_value.setText)
    
    
    def update_max_temp_ui(self, new_value):
        self.max_temp_value.setText(str(new_value))
        print "max temp UI updated"
    
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
    
    def change_alarm_window_style(self, status):
        '''
        This method updates the main window's Stylesheet
        when the alarm is activated.
        rgb(255, 140, 142);
        '''
        if status:
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