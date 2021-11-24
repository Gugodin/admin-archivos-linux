import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import subprocess

from Views.ui_main import Ui_MainWindow
from Views.ventana2 import Ui_window2
from GeneraraTablas import Permisos
from modal import ModalWindow 

class ventana(QMainWindow):
    listaPermisos = []
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
            self.ui.permisos.clicked.connect(self.generarTabla)
            
            self.ui.crear.clicked.connect(lambda:self.crearVentanaModal(1))
            self.ui.editar.clicked.connect(lambda:self.crearVentanaModal(2))
            self.ui.eliminar.clicked.connect(lambda:self.crearVentanaModal(3))


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
        self.ui.tabla.setRowCount(len(separado))
        
        for i in range(len(separado)):
            self.listaPermisos.append(separado[i][0])  
            name = ''
            if len(separado[i]) > 9:
                for x in range(8,len(separado[i])):
                    name += separado[i][x] + ' '
            else:
                name =separado[i][8]
            
            self.ui.tabla.setItem(i,0,QTableWidgetItem(name))
            usuario = separado[i][2]
            self.ui.tabla.setItem(i,1,QTableWidgetItem(usuario))
            fecha = separado[i][6]+'/'+separado[i][5]+'/'+separado[i][7]
            self.ui.tabla.setItem(i,2,QTableWidgetItem(fecha))

    def generarTabla(self):
        Permisos(self.listaPermisos)

    def crearVentanaModal(self,action):
        #HACE FALTA OBTENER EL NOMBRE DEL ARCHIVO SELECCIONADO DEN LA TABLA
        itemSeleccionado = None
        if action == 2 or action == 3:
            fila = self.ui.tabla.currentItem().row()
            itemSeleccionado = self.ui.tabla.item(fila,0).text()
        
        
        modalWindow = ModalWindow(action,itemSeleccionado,self.direccion)
        modalWindow.exec()
        self.rellenarTabla()
        

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ventana()
    window.show()
    sys.exit(app.exec())
   