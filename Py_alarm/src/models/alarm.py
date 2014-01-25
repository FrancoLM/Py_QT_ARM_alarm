'''
Created on Jan 17, 2014

@author: fmartinez1
'''

class Alarm(object):
    '''
    This class represents an alarm that activates when the current temperature
    is greater or equal than the maximum temperature value.
    [Por ahora, el HW no hace sonar ninguna alarma...]
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(Alarm, self).__init__()
        self._alarm_status = False
        
    
    def set_alarm_status(self, status):
        '''
        This method activates or deactivates the alarm.
        '''
        if status:
            self._alarm_status = status
            self._activate_alarm()
            print "Alarm activated!!!"
        else:
            if self._is_alarm():
                self._deactivate_alarm()
    
    
    def _activate_alarm(self):
        '''
        This method emits a signal to activate the alarm
        '''
        pass
    
    def _deactivate_alarm(self):
        '''
        This method emits a signal to deactivate the alarm.
        '''
        pass
    
    def _is_alarm(self):
        return self._alarm_status
    
    
    
