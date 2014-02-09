'''
Created on 26/01/2014

@author: Franco
'''

import sys
from PySide.QtGui import QDialog, QApplication
from views.max_temp_dialog import Ui_new_max_temp_dialog

class Max_temp_dialog(QDialog, Ui_new_max_temp_dialog):
    '''
    This class represents a dialog which prompts the user to enter
    the new maximum temperature value.
    '''
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
            print "New max temperaure value entered:", new_value
        except:
            pass
            #print "bad"
        
        
        
    
if __name__ == '__main__':
    #Interfaz de usuario
    app = QApplication(sys.argv)

    main = Max_temp_dialog()
    
    main.show()
    

    sys.exit(app.exec_())