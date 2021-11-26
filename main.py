import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import subprocess, re

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
        self.nameFile = []
        self.separado = []
    
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
            self.ui.buscar.clicked.connect(lambda:self.buscarPalabra())

        else:
            self.ui.labelError.setText('Debe de escribir alguna dirección')

    def rellenarTabla(self,isSearch=[]):
        if len(isSearch) == 0:
            self.nameFile.clear()
            pipe = subprocess.Popen('ls -l "'+str(self.direccion)+'"',  stdout=subprocess.PIPE).stdout
            output = pipe.read()
            texto = output.__str__()    
            self.separado = texto.split(str(chr(92))+'n')
            self.separado.pop()
            self.totalCargados = self.separado[0]
            self.separado.pop(0)
            for i in range (len(self.separado)):
                self.separado[i] = self.separado[i].split(' ')
            for i in range(len(self.separado)):
                
                while self.separado[i].count('') != 0:

                    self.separado[i].remove('')
            self.ui.tabla.setRowCount(len(self.separado))
            
            for i in range(len(self.separado)):
                self.listaPermisos.append(self.separado[i][0])  
                name = ''
                if len(self.separado[i]) > 9:
                    for x in range(8,len(self.separado[i])):
                        name += self.separado[i][x] + ' '
                else:
                    name = self.separado[i][8]
                self.nameFile.append(name)
                self.ui.tabla.setItem(i,0,QTableWidgetItem(name))
                usuario = self.separado[i][2]
                self.ui.tabla.setItem(i,1,QTableWidgetItem(usuario))
                fecha = self.separado[i][6]+'/'+self.separado[i][5]+'/'+self.separado[i][7]
                self.ui.tabla.setItem(i,2,QTableWidgetItem(fecha)) 

        else:
            self.ui.tabla.clearContents()
            self.ui.tabla.setRowCount(len(isSearch[0]))

            for i in range(len(isSearch[0])):
                name = isSearch[0][i]
                user = self.separado[isSearch[1][i]][2]
                date = self.separado[isSearch[1][i]][6]+'/'+self.separado[isSearch[1][i]][5]+'/'+self.separado[isSearch[1][i]][7]
                self.ui.tabla.setItem(i,0,QTableWidgetItem(name))
                self.ui.tabla.setItem(i,1,QTableWidgetItem(user))
                self.ui.tabla.setItem(i,2,QTableWidgetItem(date))

            # print(p.span()[0])
            # print(self.nameFile)

    def buscarPalabra(self):
        if self.ui.busqueda.text() == '':
            self.rellenarTabla()
            self.ui.opcion1.setText('')
            self.ui.opcion2.setText('')
            self.ui.recomendacion.setText('')
        elif self.ui.busqueda.text()[0] != '.':
            self.ui.opcion1.setText('')
            self.ui.opcion2.setText('')
            self.ui.recomendacion.setText('')
            aBuscar = self.ui.busqueda.text()
            listTemp = [[],[]]
            for i in range(len(self.nameFile)):
                p = re.search(aBuscar, self.nameFile[i])
                if p is not None :
                    if p.span()[0] == 0 and p.span()[1] == len(aBuscar):
                        listTemp[0].append(self.nameFile[i])
                        listTemp[1].append(i)
            self.rellenarTabla(listTemp)
        elif self.ui.busqueda.text()[0] == '.':
            aBuscar = self.ui.busqueda.text()
            listTemp = [[],[]]

            for i in range(len(self.nameFile)):
                p = re.search(aBuscar, self.nameFile[i])
                if p is not None :
                    listTemp[0].append(self.nameFile[i])
                    listTemp[1].append(i)
            self.turinMachine(aBuscar)
            self.rellenarTabla(listTemp)
            
    def turinMachine(self,buscado):
        self.ui.recomendacion.setText('Te recomendamos buscar:')
        if buscado == '.txt':
            self.ui.opcion1.setText('.pdf')
            self.ui.opcion2.setText('.docx')
        elif buscado == '.pdf':
            self.ui.opcion1.setText('.txt')
            self.ui.opcion2.setText('.docx')
        elif buscado == '.docx':
            self.ui.opcion1.setText('.txt')
            self.ui.opcion2.setText('.pdf')
        elif buscado == '.py':
            self.ui.opcion1.setText('.html')
            self.ui.opcion2.setText('.js')
        elif buscado == '.html':
            self.ui.opcion1.setText('.py')
            self.ui.opcion2.setText('.js')
        elif buscado == '.js':
            self.ui.opcion1.setText('.html')
            self.ui.opcion2.setText('.py')
        elif buscado == '.jpg':
            self.ui.opcion1.setText('.png')
            self.ui.opcion2.setText('.jpge')
        elif buscado == '.png':
            self.ui.opcion1.setText('.jpg')
            self.ui.opcion2.setText('.jpge')
        elif buscado == '.jpge':
            self.ui.opcion1.setText('.png')
            self.ui.opcion2.setText('.jpg')
        elif buscado == '.mp4':
            self.ui.opcion1.setText('.moc')
            self.ui.opcion2.setText('.mkv')
        elif buscado == '.mov':
            self.ui.opcion1.setText('.mvk')
            self.ui.opcion2.setText('.mp4')
        elif buscado == '.mkv':
            self.ui.opcion1.setText('.mp4')
            self.ui.opcion2.setText('.mov')      


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
   