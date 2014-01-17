'''
Created on Jan 17, 2014

@author: fmartinez1

[Rethink this class/method.........]

'''
#[Do I need the imports?]
from alarm import Alarm
from temperature import Current_Temp, Max_Temp

class App_Logic(object):
    
    def __init__(self, alarm, max_temp, current_temp):
        super(App_Logic, self).__init__()
        self.alarm = alarm
        self.max_temp = max_temp
        self.current_temp = current_temp
        
    def compare_temperatures(self):        
        if self.current_temp.get_temperature() >= self.max_temp.get_temperature():
            self.alarm_turn_on()
            
        
    #turn on and off should be private?
    def alarm_turn_off(self):
        #Signal to stop alarm
        self.alarm.set_alarm_status(False)
        
    def alarm_turn_on(self):
        #Signal to sound alarm
        self.alarm.set_alarm_status(True)
        
        
if __name__ == "__main__":
    
    alarm = Alarm()
    max_temp = Max_Temp()
    current_temp = Current_Temp()
    
    max_temp.set_temperature(25)
    current_temp.set_temperature(10)
    
    app = App_Logic(alarm, max_temp, current_temp)
    app.compare_temperatures()
    
    print alarm._alarm_status
    
    current_temp.set_temperature(44)
    app.compare_temperatures()
    
    print alarm._alarm_status
    