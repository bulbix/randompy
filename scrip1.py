from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
import numpy as np
import sys

app = QApplication(sys.argv)

dlg = loadUi('random.ui')
gender = ["Male", "Female"]


def generate_rand_list():
    dlg.listWidget.clear()
    lst = np.random.randint(1, 10, int(dlg.lineEdit.text()))
    for item in lst:
        dlg.listWidget.addItem(str(item) + '-' + np.random.choice(gender))


dlg.pushButton.clicked.connect(generate_rand_list)
dlg.show()
app.exec()
