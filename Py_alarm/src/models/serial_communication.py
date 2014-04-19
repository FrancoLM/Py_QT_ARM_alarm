'''
Created on Jan 16, 2014

@author: fmartinez1
'''
import serial
import random
import time
import threading
from PySide.QtCore import Signal, QObject

#===============================================================================
#===============================================================================
class Serial_communication(QObject):
    '''
    If Serial_communication is Not a QObject, then the Signals and Slots
    do not work...
    '''
    
    #Neccesary??? I think not...
    ser = None
    port_number = 99
    value_read = None
    
    value_read_signal = Signal(str)
    
    def __init__(self):
        '''
        Constructor
        '''
        super(Serial_communication, self).__init__()
        self._establish_serial_connection()
        #self.app_logic = app_logic
        
    
    #===========================================================================
    def _establish_serial_connection(self):
        '''
        This method establishes the connection between the PC and the alarm hardware.
        Both are connected via a Serial Port. 
        The method takes the port number and checks if it can connect.
        Note that port_number 0 == COM1
        '''
        for i in range(0, 10):
            self.port_number = i
            print "Trying to connect to Serial Port number", self.port_number
            try:
                self.ser = serial.Serial(self.port_number, 9600, timeout=10)
                #self.ser = serial.Serial(self.port_number)  # open first serial port
                print "Connected to", self.ser.name   # check which port was really used
                break
            except Exception:
                #I should emit a signal so the app displays an info message.
                pass
                
    
    #===========================================================================
    def read_from_port(self):
        '''
        This method reads a '\n' terminated line.
        After reading it, it notifies the app logic object, so it saves this
        value as the new current temperature value, and queues it in the temperature
        queue, so it can be displayed in the UI graph.
        It emits the signal value_read_signal. The controller handles that signal.
        '''
        
        while True:
            try:    
                #print "About to read..."        
                self.value_read = self.ser.readline()   # read a '\n' terminated line
                #print "Read value:", str(self.value_read)
                
                time.sleep(0.5)
                
                self.value_read_signal.emit(self.value_read)
                #return self.value_read
            except Exception, e:
                #Maybe I could not read because there is no data? Check documentation!
                
                print "Could not read from port.", e
                return None
        '''
        while True:
            
            self.value_read = random.randint(5, 35)
            self.value_read_signal.emit(str(self.value_read))
            
            #self.app_logic.update_current_temp(self.value_read)
            #print "I'm reading...", self.value_read, "and signal emmited"
            #The time it sleeps should be informed by the HW...
            time.sleep(0.5)
        '''
    
    #===========================================================================
    def get_value_read(self):
        return self.value_read
            
    #===========================================================================
    def close_port(self):
        '''
        This method closes the Serial connection, if it was opened. If it wasn't, 
        it does nothing.
        '''
        print "Closing port..."
        try:
            self.ser.close()   # close port
            print "Port", self.ser.name, "closed successfully"
        except Exception, e:
            pass


if __name__ == '__main__':
    comm = Serial_communication(port_number = 17)
    #comm.establish_serial_connection()
    
    #print "value read:", comm.read_from_port()
    
    t = threading.Thread(target = comm.read_from_port)
    t.daemon = True
    print "about to start..."
    t.start()
    print "started..."
    print "value read:", comm.get_value_read()
    
    while True:
        pass
    comm.close_port()
