# -*- coding: utf-8 -*-

#===============================================================================
# Va a entrar en desuso cuando modularice todo
#===============================================================================
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import random
import numpy as np





from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar



import matplotlib.pyplot as plt
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
import threading

import serial
from Queue import Queue

import time


#===============================================================================
# 
#===============================================================================
class Python_serial(object):
    
    
    def __init__(self):
        super(Python_serial, self).__init__()
        self.cola = Queue(20)
        
    
    def read_port(self):
        for i in range(0, 10):
            print "Im trying to connect..."
            try:
                ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
                #ser = serial.Serial(i)  # open first serial port
                print "Conectado a", ser.name   # check which port was really used
    
                #cola = Queue(10)
    
                while True:
                    line = ser.readline()   # read a '\n' terminated line
                    valor = float(line) / 100
    
                    try:
                        self.cola.put_nowait(valor)
    
                    except Exception, e:
                        self.cola.get_nowait()
                        self.cola.put_nowait(valor)
    
                    print "el valor en la cola es:", list(self.cola.queue)
    
                    #print line
                ser.close()             # close port
            except Exception, e:
                #Si no pude leer el puerto, escribo randoms (esto para probar sin estar conectado)
                #Borrar esto cuando se conecte!!!!
                #cola = Queue(10)
                print "entro aca... esta mal"
                while True:
                    valor = random.randint(0, 25)
      
                    try:
                        self.cola.put_nowait(valor)
      
                    except Exception, e:
                        self.cola.get_nowait()
                        self.cola.put_nowait(valor)
                     #print "el valor en la cola es:", list(self.cola.queue)
                    time.sleep(0.1)
               #Borrar cuando estemos conectados!! Por las dudas (aunque es poco probable que entremos aca)
    
    def get_cola(self):
        return list(self.cola.queue)
                
#===============================================================================
# 
#===============================================================================
class myLCDNumber(QtGui.QLCDNumber):
    def __init__(self, parent=None):
        super(myLCDNumber, self).__init__(parent)


    value = 40
    value1 = 1
    @pyqtSlot()
    def count(self):
        self.display(self.value)

    @pyqtSlot()
    def tempbaj(self):
        self.display(self.value1)


    @pyqtSlot()
    def tempact(self):
        self.display(random.randint(0,50))



#===============================================================================
# 
#===============================================================================
class Window(QtGui.QDialog):
    
    def __init__(self, uart_conn, parent=None):
        super(Window, self).__init__(parent)
        
        self.uart_conn = uart_conn
        
        #print "recibi", self.uart_conn
        # a figure instance to plot on
        self.figure = plt.figure()
#         mu, sigma = 100, 15
#         x = mu + sigma * np.random.randn(10000)
#         self.figure = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
        

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        
        self.plot_timer = self.canvas.new_timer(interval=100)
        self.plot_timer.add_callback(self.plot, self.uart_conn)
        self.plot_timer.start()
        

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        #self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.button = QtGui.QPushButton('Plot')
        
        
        #Un boton que pause el grafico
        self.button.clicked.connect(lambda: self.plot(self.uart_conn))

        # set the layout
        self.ventana=QtGui.QWidget()
        #horizontal=QtGui.QVBoxLayout()

        self.titulo=QtGui.QLabel('Temp  Maxima')
        self.tmax=QtGui.QLabel('Temp  Maxima')
        self.tact=QtGui.QLabel('Temp  Actual')
        self.tmin=QtGui.QLabel('Temp  Minima')
        self.titulo.move(50,10)
        display1 = myLCDNumber(5)
        display2 = myLCDNumber(5)
        display3 = myLCDNumber(5)
        timer = QtCore.QTimer()
        display1.connect(timer,SIGNAL("timeout()"),display1,SLOT("count()"))
        timer.start(1000)
        display2.connect(timer,SIGNAL("timeout()"),display2,SLOT("tempact()"))
        timer.start(1000)
        display3.connect(timer,SIGNAL("timeout()"),display3,SLOT("tempbaj()"))
        timer.start(1000)
        
        #self.button.clicked.connect(lambda: self.plot(self.uart_conn))
        #self.button.connect(timer, SIGNAL("timeout()"), self.button, self.button.clicked)
        #display3.connect(timer,SIGNAL("timeout()"),display3,SLOT("tempbaj()"))

        self.display_widget	= QtGui.QWidget()
        
#         self.vlayout    = QtGui.QVBoxLayout()

        self.vBoxlayout	= QtGui.QHBoxLayout()

        self.vBoxlayout.addWidget(display1)
        self.vBoxlayout.addWidget(display2)
        self.vBoxlayout.addWidget(display3)


        layout = QtGui.QVBoxLayout()
        #layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        #layout.addWidget(self.button)
        
        self.display_widget.setLayout(self.vBoxlayout)
        #self.display_widget.resize(480, 320)
        
        layout.addWidget(self.display_widget)
#         layout.addWidget(display2)
#         layout.addWidget(display3)
        
        self.setLayout(layout)
        #self.setLayout(tab3)
        
        
    def plot(self, uart_conn):
        ''' plot some random stuff '''
        
        # random data
        data = uart_conn.get_cola()
        #data = [10,17,30,22,6,3,34,24,15]
        #random.random() for i in range(10)
        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.hold(False)
        
        
        
        
        # plot data
        ax.plot(data, '*-')
        
        #Set rango de valores del eje y
        ax.set_ylim([0,42])
        ax.set_title("Variacion de Temperatura")
        
        # refresh canvas
        self.canvas.draw()
        
    def example_graph(self):
        mu, sigma = 100, 15
        x = mu + sigma * np.random.randn(10000)
        
        # the histogram of the data
        n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
        
        
        plt.xlabel('Smarts')
        plt.ylabel('Probability')
        plt.title('Histogram of IQ')
        plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
        plt.axis([40, 160, 0, 0.03])
        plt.grid(True)
        #plt.show()


#===============================================================================
#===============================================================================
# # 
#===============================================================================
#===============================================================================
if __name__ == '__main__':
    
    #Thread que lee el puerto
    uart_conn = Python_serial()
    t = threading.Thread(target = uart_conn.read_port)
    t.daemon = True
    t.start()
    
    
    #Interfaz de usuario
    app = QtGui.QApplication(sys.argv)

    main = Window(uart_conn)
    
    main.show()

    sys.exit(app.exec_())
