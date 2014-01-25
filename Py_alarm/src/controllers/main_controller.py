'''
Created on 23/01/2014

@author: Franco
This script will call the app logic and will connect the model and the view.
'''

class App_controller():
    
    def __init__(self, model, view):
        super(App_controller, self).__init__()
        
        # I have to tell the View to update the graph whenever
        # a new value in the Serial communication (Model)
        # is read.
    
        #call view.set_queue(model.queue)
        
        #connect the model.signal_conn.value_read_signal
        
        