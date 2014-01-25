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
    
    value_read_signal = Signal()
    
    def __init__(self, port_number, app_logic):
        '''
        Constructor
        '''
        super(Serial_communication, self).__init__()
        self.port_number = port_number
        self._establish_serial_connection()
        self.app_logic = app_logic
        
    
    #===========================================================================
    def _establish_serial_connection(self):
        '''
        This method establishes the connection between the PC and the alarm hardware.
        Both are connected via a Serial Port. 
        The method takes the port number and checks if it can connect.
        Note that port_number 0 == COM1
        '''
        #self.port_number = port_number
        print "Trying to connect to Serial Port number", self.port_number + 1
        try:
            self.ser = serial.Serial(self.port_number, 115200, timeout=10)
            #self.ser = serial.Serial(self.port_number)  # open first serial port
            print "Connected to", self.ser.name   # check which port was really used

            #cola = Queue(10)
        except Exception, e:
            #I should emit a signal so the app displays an info message.
            print "Error.", e
                
    
    #===========================================================================
    def read_from_port(self):
        '''
        This method reads a '\n' terminated line.
        After reading it, it notifies the app logic object, so it saves this
        value as the new current temperature value, and queues it in the temperature queue, 
        so it can be displayed in the UI graph.
        It emits the signal value_read_signal. The controller handles that signal.
        '''
        '''
        #Uncomment this when the HW - PC communication works
        try:            
            line = self.ser.readline()   # read a '\n' terminated line
            return line
        except Exception, e:
            #Maybe I could not read because there is no data? Check documentation!
            
            print "Could not read from port.", e
            return None
        '''
        while True:
            
            self.value_read = random.randint(5, 35)
            self.value_read_signal.emit()
            print "I'm reading...", self.value_read, "and signal emmited"
            try:
                self.app_logic.update_current_temp(self.value_read)
            except Exception, e:
                print "App is none"
            time.sleep(1)
    
    
    #===========================================================================
    def get_value_read(self):
        return self.value_read
            
    #===========================================================================
    def close_port(self):
        '''
        This method closes the Serial connection, if it was opened. If it wasn't, 
        it does nothing.
        '''
        try:
            
            self.ser.close()   # close port
            print "Port", self.ser.name, "closed successfully"
        except Exception, e:
            pass


if __name__ == '__main__':
    comm = Serial_communication(port_number = 17, app_logic = None)
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
