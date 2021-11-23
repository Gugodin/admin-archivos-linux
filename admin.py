import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QAbstractItemView, QMainWindow, QApplication, QTableWidgetItem, QDialog

class VentanaInicio(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./Views/inicio.ui", self)
        self.labelError.setStyleSheet("color: red")
        self.pushButton.clicked.connect(self.entrar)

    def entrar(self):
        if self.Entry.text() != '':
            print('hay algo')
        else: 
            self.labelError.setText('')



def vista():
    app = QApplication(sys.argv)
    GUI = VentanaInicio()
    GUI.show()
    
    sys.exit(app.exec_())

vista()