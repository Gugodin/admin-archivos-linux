from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import shlex,subprocess

from Views.ui_ModalView import Ui_Dialog

class ModalWindow(QDialog):
    def __init__(self,action,nombreDeArchivo, direccion):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.nombreArchivo = nombreDeArchivo
        self.direccion = direccion
        self.accion = action

        self.ui.aceptar.clicked.connect(self.acepto)

        if self.accion == 1:  
            self.ui.text.setText('Crear archivo')    
        elif self.accion == 2:
            self.ui.text.setText('Editar archivo')  
        elif self.accion == 3:
            self.ui.text.setText('Estás seguro que quieres eliminar el archivo: ') 
            self.ui.nombreA.setText(self.nombreArchivo) 
            self.ui.entrada.setGeometry(QRect(20, 90, 0, 0))
            

            
            
    def acepto(self):
        print('Acepto')
        if self.accion == 1:      
            self.crearArchivo()
        elif self.accion == 2:
            self.editarArchivo()
        elif self.accion == 3:
            self.eliminarArchivo()

    def crearArchivo(self):
        print(self.direccion)
        if self.ui.entrada.text() !=  '':
            subprocess.call(shlex.split('touch "'+self.direccion+'\\'+self.ui.entrada.text()+'"'))
            self.close()
        else:
            print('No hay nombre de archivo')
        


    def editarArchivo(self):
        if self.ui.entrada.text() !=  '':
            subprocess.call(shlex.split('mv "'+self.direccion+'\\'+self.nombreArchivo+'"'+' "'+self.direccion+'\\'+self.ui.entrada.text()+'"'))
            self.close()
        else:
            print('No hay nombre de archivo')

    def eliminarArchivo(self):
        subprocess.call(shlex.split('rm "'+self.direccion+'\\'+self.nombreArchivo+'"'))
        self.close()