'''
Created on Jan 16, 2014

@author: fmartinez1
'''
import serial


#===============================================================================
#===============================================================================
class Serial_Communication(object):
    '''
    classdocs
    '''
    
    #Neccesary??? I think not...
    ser = None
    port_number = 99
    
    def __init__(self, port_number):
        '''
        Constructor
        '''
        super(Serial_Communication, self).__init__()
        self.port_number = port_number
        self._establish_serial_connection()
        
    
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
        This method read a '\n' terminated line
        '''
        try:            
            line = self.ser.readline()   # read a '\n' terminated line
            return line
        except Exception, e:
            #Maybe I could not read because there is no data? Check documentation!
            
            print "Could not read from port.", e
            return None
            
            
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
    comm = Serial_Communication(port_number = 17)
    #comm.establish_serial_connection()
    print "value read:", comm.read_from_port()
    #print "value read:", comm.read_from_port()
    
    comm.close_port()
