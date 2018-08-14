import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *

if __name__ == '__main__':
    myApp = QApplication(sys.argv)
    try:
        appLabel = QLabel()
        appLabel.setText("Inicio de la ventana")
        appLabel.setAlignment(Qt.AlignCenter)
        appLabel.setWindowTitle("Mi primera aplicacion")
        appLabel.setGeometry(300,300,250,175)
        appLabel.show()
        myApp.exec_()
        sys.exit()
    except NameError:
        print("Name Error:", sys.exc_info()[1])
        pass

