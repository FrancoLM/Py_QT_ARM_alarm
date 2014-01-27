'''
Created on Jan 17, 2014

@author: fmartinez1
'''
from PySide.QtCore import Signal, QObject

class Alarm(QObject):
    '''
    This class represents an alarm that activates when the current temperature
    is greater or equal than the maximum temperature value.
    [Por ahora, el HW no hace sonar ninguna alarma...]
    '''
    alarm_signal = Signal(bool)

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
        self.alarm_signal.emit(status)
        #print "I get alarm =", status
        '''
        if status:
            self._alarm_status = status
            #self._activate_alarm()
            self.alarm_signal.emit(status)
            #print "Alarm activated!!!"
        else:
            if self._is_alarm():
                #self._deactivate_alarm()
                self.alarm_signal.emit(status)
        '''
                
    
    #unused
    def _activate_alarm(self):
        '''
        This method emits a signal to activate the alarm
        '''
        pass
    
    #unused
    def _deactivate_alarm(self):
        '''
        This method emits a signal to deactivate the alarm.
        '''
        pass
    
    def _is_alarm(self):
        return self._alarm_status
    
    
    
