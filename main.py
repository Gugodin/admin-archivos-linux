from os import sep
import sys
import platform
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import subprocess

from Views.ui_main import Ui_MainWindow
from Views.ventana2 import Ui_window2

class ventana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.labelError.setStyleSheet('color:red')
        self.ui.pushButton.clicked.connect(self.entrar)
    
    def entrar(self):
        if self.ui.Entry.text() != '':
            self.direccion = self.ui.Entry.text()
            self.ui = Ui_window2()
            self.ui.setupUi(self)

            self.rellenarTabla()


        else:
            self.ui.labelError.setText('Debe de escribir alguna dirección')

    def rellenarTabla(self): 
        pipe = subprocess.Popen('ls -l "'+str(self.direccion)+'"',  stdout=subprocess.PIPE).stdout
        output = pipe.read()
        texto = output.__str__()    
        separado = texto.split(str(chr(92))+'n')
        separado.pop()
        self.totalCargados = separado[0]
        separado.pop(0)
        for i in range (len(separado)):
            separado[i] = separado[i].split(' ')
        for i in range(len(separado)):
    
            while separado[i].count('') != 0:

                separado[i].remove('')
                
        for i in range(len(separado)):
            print(separado[i])
            # print(separado[i][6]+'/'+separado[i][5]+'/'+separado[i][7])
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ventana()
    window.show()
    sys.exit(app.exec())
   