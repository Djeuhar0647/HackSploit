import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from design import Ui_Dialog
import random


app = QtWidgets.QApplication(sys.argv)
    
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

def start_butt():
    login1 = 'djeu582'
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    tel = int('9')
    zag = ('+79')
    login2 = ''
    password2 = ''
    url_hack = ui.lineEdit.text()

    for i in range(tel):
        login2 += random.choice(login1)

    for j in range(tel):
        password2 += random.choice(chars)

    hack = ('Login: ' + zag + login2), ('Password: ' + password2)

    hack1 = str(hack)

    file = open('hack.txt', 'a')
    file.write('\n' + hack1)
    file.close


    
    ui.label_5.setText(f'Статус: Данные сохранены!')

ui.pushButton.clicked.connect(start_butt)

sys.exit(app.exec_())