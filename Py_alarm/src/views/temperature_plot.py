'''
Created on 21/01/2014

@author: Franco
This script contains the plot class used to show the temperature variatons
accross time.
'''

from PySide.QtGui import QHBoxLayout

#matplotlib imports
import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class Temperature_graph():

    def __init__(self):
        '''
        This method adds the matplotlib pyplot to the UI.
        It fits the plot inside a layout, which is then set to a QFrame.
        The graph redrawing should be handled by a thread other than the main one.
        '''
        
        #self.queue = temp_queue
        #t = threading.Thread(target = self.queue.read_port)
        #t.daemon = True
        #t.start()
        
        # a figure instance to plot on
        self.figure = plt.figure()
        
        # this is the Canvas Widget that displays the `figure`
        self.canvas = FigureCanvas(self.figure)
        
        #Add a timer to redraw the graph
        #The timer is not optimal, and this should run on a separate thread.
        #The graph should be updated on demand... each time a new value is read from the serial port...
        #self.plot_timer = self.canvas.new_timer(interval=100)
        #self.plot_timer.add_callback(self.redraw_graph)
        
        
        #Create the layout for the frame
        self.layout = QHBoxLayout()
        
        #Add the Figure to the layout
        self.layout.addWidget(self.canvas)
        
        self.layout.setStretchFactor(self.canvas, 1)
        
        
        #self.redraw_graph()
        #self.plot_timer.start()
    
    def set_graph_queue(self, temperature_queue):
        self.queue = temperature_queue
    
    def get_layout(self):
        return self.layout
    
    def redraw_graph(self):
        '''
        This method redraws the graph. It's called everytime the plot_timer
        reaches zero.
        '''
        '''
        mu, sigma = 100, 15
        x = mu + sigma * np.random.randn(1000)
        #print "I enter here... x =", x
        
        # the histogram of the data
        #x should be my queue...
        n, bins, patches = plt.hist(x, 50, normed=1, facecolor='b', alpha=0.75)
        
        
        plt.xlabel('Smarts')
        plt.ylabel('Probability')
        #plt.title('Histogram of IQ')
        #plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
        plt.axis([40, 160, 0, 0.03])
        plt.grid(True)
        
        #I erase the old data graph, because I'm redrawing it with new values.
        plt.hold(False)
        
        #Re-draw the graph (with the new values)
        self.canvas.draw()
        #plt.show()
        '''
        # random data
        data = self.queue.get_cola()
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