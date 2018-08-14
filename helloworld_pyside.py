# Import PySide2 classes
import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *

# Create a Qt application
app = QApplication(sys.argv)

# Create a Window
mywindow = QWidget()
mywindow.resize(320, 240)
mywindow.setWindowTitle('Hello World!')

# Create a label and display it all together
mylabel = QLabel(mywindow)
mylabel.setText('Hello World!')
mylabel.setGeometry(QRect(200, 200, 200, 200))
mywindow.show()

# Enter Qt application main loop
sys.exit(app.exec_())