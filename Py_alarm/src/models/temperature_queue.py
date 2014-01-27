'''
Created on 22/01/2014

@author: Franco
'''
import Queue


import time

class Temp_queue(object):
    
    def __init__(self, queue_size):
        super(Temp_queue, self).__init__()
        self.cola = Queue.Queue(queue_size)
        
        # I'm cheating here... this is so the graph is properly
        # plotted (model and view should not know each other.........
        #for index in range(queue_size):
            #print "queueing..."
            #self.cola.put_nowait(0.001)
        
    def put_in_queue(self, temperature_value):
        #print "Im saving", temperature_value, "in the queue..."
        try:
            self.cola.put_nowait(temperature_value) #add the element in the queue
        
        except Exception, e:
            self.cola.get_nowait()  #takes an element out of the queue
            self.cola.put_nowait(temperature_value)
    
    
    def get_cola(self):
        return list(self.cola.queue)
    

    #===========================================================================
    # #To delete... only used for testing
    #===========================================================================
    def test_method(self):
        while True:
            valor = random.randint(0, 25)
            try:
                self.cola.put_nowait(valor)
        
            except Exception, e:
                self.cola.get_nowait()
                self.cola.put_nowait(valor)
            print "el valor en la cola es:", list(self.cola.queue)
            time.sleep(0.1)
    #===========================================================================
    # 
    #===========================================================================

# threading for testing purposes
import random
import threading

if __name__ == '__main__':
    
    #Thread que lee el puerto
    test_queue = Temp_queue()
    t = threading.Thread(target = test_queue.test_method)
    t.daemon = True
    t.start()
    
    while True:
        pass