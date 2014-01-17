'''
Created on Jan 17, 2014

@author: fmartinez1
'''
class TempNotSetError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    
    

class Temperature(object):
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


class Max_Temp(Temperature):
    
    def __init__(self):
        super(Max_Temp, self).__init__()
        
        

class Current_Temp(Temperature):
    
    def __init__(self):
        super(Current_Temp, self).__init__()


if __name__ == "__main__":
    temp = Temperature()
    temp.set_temperature(57)
    temp.get_temperature()
            
        