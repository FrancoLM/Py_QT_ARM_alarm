'''
Created on Jan 21, 2014

@author: fmartinez1
'''
import time
from Queue import Queue
import random

def create_queue():
    
    cola = Queue(20)
    
    while True:
        valor = random.randint(0, 9)
        
        try:
            cola.put_nowait(valor)
        
        except Exception, e:
            cola.get_nowait()
            cola.put_nowait(valor)
        print "el valor en la cola es:", list(cola.queue)
        time.sleep(0.4)


def get_cola():
    return list(cola.queue)


if __name__ == "__main__":
    create_queue()