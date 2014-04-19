'''
Created on 23/01/2014

@author: Franco
This script will call the app logic and will connect the model and the view.
'''

class App_controller(object):
    '''
    This class represents the application Controller part
    of the MVC pattern. This class defines the signal connections.
    '''
    
    def __init__(self, model, view):
        super(App_controller, self).__init__()
        
        self.model = model
        self.view = view
        
        #Pass the model's queue to the view, so it can print its contents
        view.set_queue(temperature_queue = model.temp_queue)
        
        #=======================================================================
        # Signal Definition
        #=======================================================================
        
        # When a new temperature value is read, update the view's current temp
        self.model.update_current_temp_signal.connect(self.view.update_current_temp_ui)
        
        # When a new temperature value is read, update the view's graph
        self.model.ser_comm.value_read_signal.connect(self.view.figure.redraw_graph)
        
        # Update the Max temperature UI value
        self.model.max_temp.new_temp_signal.connect(self.view.update_max_temp_ui)
            # Force to update the current value
        self.model.max_temp.set_temperature(self.model.max_temp.get_temperature())
        
        
        # Update UI when the alarm is activated
        self.model.alarm.alarm_signal.connect(self.view.change_alarm_window_style)
        # Deactivate alarm:
        self.view.deactivate_alarm_button.clicked.connect(self.model.alarm_turn_off)
        
        # Update the maximum temperature entered by the user
        self.view.new_max_temp_signal.connect(self.model.max_temp.set_temperature)
        
        #Close Serial port when application is closed
        self.view.close_app_signal.connect(self.model.ser_comm.close_port)
        
        # need a signal for reading the initial maximum temp from the serial connection with the HW 
        # and setting it.
        
        
        
        
        
        