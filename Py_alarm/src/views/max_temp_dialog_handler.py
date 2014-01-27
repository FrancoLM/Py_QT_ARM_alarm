'''
Created on 26/01/2014

@author: Franco
'''

import sys
from PySide.QtGui import QDialog, QApplication
from PySide.QtCore import Signal
from main_window_gui import Ui_MainWindow
from views.max_temp_dialog import Ui_new_max_temp_dialog

class Max_temp_dialog(QDialog, Ui_new_max_temp_dialog):
    
    
    
    def __init__(self, parent = None):
        super(Max_temp_dialog, self).__init__(parent)
        
        
        self.setupUi(self)
        self.lineEdit.setFocus()
        self.lineEdit.setMaxLength(2)
    
    
    def accept(self):
        '''
        This method is called when user presses the Accept button.
        It should only be enabed if text entered is valid...
        It emits a signal to update the model's max temp value.
        '''
        #print "I enter", self.lineEdit.text()
        
        try:
            new_value = int(self.lineEdit.text())
            
            self.close()
            print "ok"
        except:
            pass
            #print "bad"
        
        
        
    
if __name__ == '__main__':
    #Interfaz de usuario
    app = QApplication(sys.argv)

    main = Max_temp_dialog()
    
    main.show()
    

    sys.exit(app.exec_())