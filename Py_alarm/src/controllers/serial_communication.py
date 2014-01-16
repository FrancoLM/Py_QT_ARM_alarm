'''
Created on Jan 16, 2014

@author: fmartinez1
'''
import serial

class Serial_Communication(object):
    '''
    classdocs
    '''
    
    ser = None
    port_number = 99
    
    def __init__(self, port_number):
        '''
        Constructor
        '''
        super(Serial_Communication, self).__init__()
        self.port_number = port_number
        self.establish_serial_connection()
        
    
    
    def establish_serial_connection(self):
        '''
        This method establishes the connection between the PC and the alarm hardware.
        Both are connected via a Serial Port. 
        The method takes the port number and checks if it can connect.
        Note that port_number 0 == COM1
        '''
        
        print "Trying to connect to Serial Port number", self.port_number + 1
        try:
            self.ser = serial.Serial(self.port_number, 115200, timeout=1)
            #self.ser = serial.Serial(self.port_number)  # open first serial port
            print "Connected to", self.ser.name   # check which port was really used

            #cola = Queue(10)
        except Exception, e:
            #I should emit a signal so the app displays an info message.
            print "Device not connected to port COM" + str(self.port_number) +  ".", e
                
               
    def read_port(self):
        '''
        This method read a '\n' terminated line
        '''
        try:
            line = self.ser.readline()   # read a '\n' terminated line
            print line
        except Exception, e:
            #Maybe I could not read because there is no data? Check documentation!
            
            print "Could not read from port.", e
            '''valor = float(line) / 100

            try:
                self.cola.put_nowait(valor)

            except Exception, e:
                self.cola.get_nowait()
                self.cola.put_nowait(valor)

            print "el valor en la cola es:", list(self.cola.queue)'''

            #print line
    def close_port(self):
        self.ser.close()             # close port


if __name__ == '__main__':
    comm = Serial_Communication(port_number = 7)
    comm.read_port()
