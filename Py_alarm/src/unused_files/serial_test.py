'''
Created on 19 Apr 2014

@author: Franco
'''
import serial
from Queue import Queue
for i in range(0, 10):
    try:
        ser = serial.Serial(i)  # open first serial port
        print "Conectado a", ser.name  # check which port was really used
        cola = Queue(10)
        while True:
            line = ser.readline()  # read a '\n' terminated line
            valor = int(line)
            print "valor es:", valor
            try:
                cola.put_nowait(valor)
            except Exception, e:
                cola.get_nowait()
                cola.put_nowait(valor)
                print "el valor en la cola es:", list(cola.queue)
                #print line
        ser.close()  # close port
    except Exception, e:
        pass