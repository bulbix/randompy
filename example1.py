import sys
import time
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *


class SampleWindow(QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Sample Window")
        self.setGeometry(300, 300, 200, 150)
        self.setWindowIcon(QIcon('foobar.ico'))

        self.setMinimumHeight(100)
        self.setMinimumWidth(250)
        self.setMaximumHeight(200)
        self.setMaximumWidth(800)
        self.setIconModes()
        self.setButton()
        self.show()
        print("Sample Window show in the GUI\n")

    def setIconModes(self):
        myIcon1 = QIcon('foobar.ico')
        myLabel1 = QLabel('sample', self)
        pixmap1 = myIcon1.pixmap(50, 50, QIcon.Active, QIcon.On)
        myLabel1.setPixmap(pixmap1)
        myLabel1.setToolTip("Icono")
        myLabel1.show()
        myIcon2 = QIcon('foobar.ico')
        myLabel2 = QLabel('sample', self)
        pixmap2 = myIcon2.pixmap(50, 50, QIcon.Disabled, QIcon.Off)
        myLabel2.setPixmap(pixmap2)
        myLabel2.move(50, 0)
        myLabel2.setToolTip("Icono2")
        myLabel2.show()
        myIcon3 = QIcon('foobar.ico')
        myLabel3 = QLabel('sample', self)
        pixmap3 = myIcon3.pixmap(50, 50, QIcon.Selected, QIcon.On)
        myLabel3.setPixmap(pixmap3)
        myLabel3.move(100, 0)
        myLabel3.setToolTip("Icono3")
        myLabel3.show()

    def setButton(self):
        """ Function to add a quit button
        """
        myButton = QPushButton('Quit', self)
        myButton.move(50, 100)
        myButton.clicked.connect(self.quitApp)

    def quitApp(self):
        response = self.msgApp("Confirmation", "This will quit the application.Do you want to Continue?")
        if response == "Y":
            myApp.quit()
        else:
            pass

    def msgApp(self, title, msg):
        userInfo = QMessageBox.question(self, title, msg, QMessageBox.Yes | QMessageBox.No)
        if userInfo == QMessageBox.Yes:
            return "Y"
        if userInfo == QMessageBox.No:
            return "N"


if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        myWindow = SampleWindow()
        QToolTip.setFont(QFont("Decorative", 8, QFont.Bold))
        QCoreApplication.processEvents()
        #time.sleep(3)
        #myWindow.resize(300,300)
        #myWindow.setWindowTitle("Sample Window Resized")
        #myWindow.repaint()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print(sys.exc_info())
    except SystemExit:
        print("Closing Window")
    except Exception:
        print(sys.exc_info())

