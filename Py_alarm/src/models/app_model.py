'''
Created on Jan 17, 2014

@author: fmartinez1

[Rethink this class/method.........]

'''
#[Do I need the imports?]
from alarm import Alarm
from temperature import Current_temp, Max_temp
from temperature_queue import Temp_queue
from models.serial_communication import Serial_communication
import threading
#from PySide.QtCore import QObject


class App_model(object):
    '''
    This class is the Model component of the MVC pattern.
    '''
    
    def __init__(self, queue_size, initial_max_temp):
        super(App_model, self).__init__()
        #=======================================================================
        # Initialize the temperature parameters (max temp, current temp, alarm,
        # temperature queue) and connects everything.
        #=======================================================================
        #app = App_Logic(alarm, max_temp, current_temp, temp_queue)
        
        self.alarm = Alarm()
        self.max_temp = Max_temp()
        self.current_temp = Current_temp()
        self.temp_queue = Temp_queue(queue_size = 20)
        
        self.max_temp.set_temperature(int(initial_max_temp))
        
        #=======================================================================
        # Serial Port listener
        # Initialize the HW listener... it runs in a different thread.
        #=======================================================================
        self.ser_comm = Serial_communication(port_number = 5,app_logic = self)
        
        t = threading.Thread(target = self.ser_comm.read_from_port)
        t.daemon = True
        t.start()
        print "Serial Listener started!"
        
        
        
    def compare_temperatures(self):
        '''
        This method compares the current temperature and the max temperature defined.
        If the current is greater than the max temperature, an alarm will sound.
        '''
        if self.current_temp.get_temperature() >= self.max_temp.get_temperature():
            self.alarm_turn_on()
        #elif self.alarm.is_alarm():
            
            
    
    #===========================================================================
    def alarm_turn_off(self):
        #Signal to stop alarm
        self.alarm.set_alarm_status(False)
    
    #===========================================================================
    def alarm_turn_on(self):
        #Signal to sound alarm
        self.alarm.set_alarm_status(True)
    
    
    def update_current_temp(self, new_value):
        self.current_temp.set_temperature(new_value)
        self.temp_queue.put_in_queue(new_value)
        self.compare_temperatures()
    
import time    
if __name__ == "__main__":
    
    app = App_model(queue_size = 20, initial_max_temp = 45)
    
    app.max_temp.set_temperature(25)
    app.current_temp.set_temperature(10)
    
    app.compare_temperatures()
    
    print app.alarm._alarm_status
    
    app.current_temp.set_temperature(44)
    app.compare_temperatures()
    
    print app.alarm._alarm_status
    
    while True:
        time.sleep(10)
    