'''
Created on Jan 17, 2014

@author: fmartinez1
'''
from PySide.QtCore import QObject, Signal

class TempNotSetError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    
    

class Temperature(QObject):
    '''
    This is the class from where Max_temp and Current_temp will inherit
    '''
    
    _temperature = None
    
    
    def __init__(self):
        '''
        Constructor
        '''
        super(Temperature, self).__init__()
        
    def set_temperature(self, temp_value):
        '''
        Temperature Setter method
        '''
        self._temperature = temp_value
        
    def get_temperature(self):
        '''
        Temperature Getter method. If temperature was not initialized, an exception is thrown.
        '''
        if self._temperature:
            return self._temperature
        else:
            raise TempNotSetError("Temperature was not initialized")


class Max_temp(Temperature):
    
    new_temp_signal = Signal(int)
    
    def __init__(self):
        super(Max_temp, self).__init__()
        
    def set_temperature(self, temp_value):
        '''
        Temperature Setter method
        '''
        self._temperature = temp_value
        self.new_temp_signal.emit(temp_value)
        #print "max temp signal"

class Current_temp(Temperature):
    
    def __init__(self):
        super(Current_temp, self).__init__()


if __name__ == "__main__":
    temp = Temperature()
    temp.set_temperature(57)
    temp.get_temperature()
            
        