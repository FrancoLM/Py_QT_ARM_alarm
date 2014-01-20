'''
Created on Jan 16, 2014

@author: fmartinez1
'''

# Allow access to command-line arguments
import sys
 
# Import the core and GUI elements of Qt
#Change PyQt4 for PySide...
from PySide.QtCore import *
from PySide.QtGui import *
 
# Every Qt application must have one and only one QApplication object;
# it receives the command line arguments passed to the script, as they
# can be used to customize the application's appearance and behavior
qt_app = QApplication(sys.argv)
 
# Create a label widget with our text
label = QLabel('Hello, world!')
 
# Show it as a standalone widget
label.show()
 
# Run the application's event loop
qt_app.exec_()

'''
import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
'''