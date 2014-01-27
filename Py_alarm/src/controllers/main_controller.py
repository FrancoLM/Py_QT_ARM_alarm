'''
Created on 23/01/2014

@author: Franco
This script will call the app logic and will connect the model and the view.
'''

class App_controller(object):
    
    def __init__(self, model, view):
        super(App_controller, self).__init__()
        
        self.model = model
        self.view = view
        
        # I have to tell the View to update the graph whenever
        # a new value in the Serial communication (Model)
        # is read.
    
        #call view.set_queue(model.queue)
        
        #connect the model.signal_conn.value_read_signal
        
        
        
        #self.action_exit_app.triggered.connect(self.quit_application)
        
        
        
        #=======================================================================
        # Signal Definition
        #=======================================================================
        
        # Update the Maximum temperature UI value
        
        # When a new temperature value is read, update the view's current temp
        self.model.ser_comm.value_read_signal.connect(self.view.update_current_temp_ui)
        
        # When a new temperature value is read, update the view's graph
        self.model.ser_comm.value_read_signal.connect(self.view.figure.redraw_graph)
        
        # Update the Max temperature UI value
        self.model.max_temp.new_temp_signal.connect(self.view.update_max_temp_ui)
            # Force to update the current value
        self.model.max_temp.set_temperature(self.model.max_temp.get_temperature())
        
        
        # When the alarm is activated
        self.model.alarm.alarm_signal.connect(self.view.change_alarm_window_style)
        # To deactivate alarm:
        self.view.deactivate_alarm_button.clicked.connect(self.model.alarm_turn_off)
        
        
        self.view.new_max_temp_signal.connect(self.model.max_temp.set_temperature)
        
        
        # Close application view -> view should be here???
        self.view.action_exit_app.triggered.connect(self.view.quit_application)
        
        
        
        
        
        
        
        