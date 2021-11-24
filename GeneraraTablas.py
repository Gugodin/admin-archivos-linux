import re
import matplotlib.pyplot as plt


class Permisos():
    def __init__(self,lista):
        self.listaPermisos = lista
        for i in range(len(self.listaPermisos)):
            self.countPermition(self.listaPermisos[i])
        self.generateLista()
        self.generarTablas()
        
    countsTypeFile = {
        '-': 0,
        'd': 0,
        'l': 0,
        's': 0,
        'p': 0,
    }

    counts = {
        'r': [0,0,0],
        'w': [0,0,0],
        'x': [0,0,0],
        'rw': [0,0,0],
        'rx': [0,0,0],
        'wx': [0,0,0],
        'rwx': [0,0,0],
        '-': [0,0,0]
    }
    
    # def verifyString(self,cad):
    #     p = re.compile('(-|d|s|l|p)(r|-)(w|-)(x|-)(r|-)(w|-)(x|-)(r|-)(w|-)(x|-)')
    #     a = cad
    #     if p.fullmatch(a) is not None:
    #         return True
    #     else:
    #         return False

    def countPermition(self,cad):
        cad = str(cad)

        charInitial = cad[0]

        if charInitial == '-':
            self.countsTypeFile['-'] = self.countsTypeFile['-'] + 1
        elif charInitial == 'd':
            self.countsTypeFile['d'] = self.countsTypeFile['d'] + 1
        elif charInitial == 'l':
            self.countsTypeFile['l'] = self.countsTypeFile['l'] + 1
        elif charInitial == 's':
            self.countsTypeFile['s'] = self.countsTypeFile['s'] + 1
        elif charInitial == 'p':
            self.countsTypeFile['p'] = self.countsTypeFile['p'] + 1

        user = ''
        other = ''
        group = ''

        for i in range(1,len(cad)):
            if i < 4:
                user = user + cad[i]
            if i > 3 and i < 7:
                group = group + cad[i]
            if i > 6 and i <= 9:
                other = other + cad[i]

        listString = [user,other,group]

        for i in range(0,3):

            if listString[i] == 'r--':
                self.counts['r'][i] = self.counts['r'][i] +1
            if listString[i] == '-w-':
                self.counts['w'][i] = self.counts['w'][i] +1
            if listString[i] == '--x':
                self.counts['x'][i] = self.counts['x'][i] +1
            if listString[i] == 'rw-':
                self.counts['rw'][i] = self.counts['rw'][i] +1
            if listString[i] == 'r-x':
                self.counts['rx'][i] = self.counts['rx'][i] +1
            if listString[i] == '-wx':
                self.counts['wx'][i] = self.counts['wx'][i] +1
            if listString[i] == 'rwx':
                self.counts['rwx'][i] = self.counts['rwx'][i] +1
            if listString[i] == '---':
                self.counts['-'][i] = self.counts['-'][i] +1



    def generateLista(self):
        tabla = [['Permisos','r','w','x','rw','rx','wx','rwx','-'],['Usuario'],['Grupo'],['Otros']]
        tabla2 =[['Tipos Archivos','Común','Directorios','Enlaces','Socket','Pipe'],['Conteo']]
        for i in range(3):
            for key in self.counts:

                tabla[i+1].append(self.counts[key][i])
                
        for key in self.countsTypeFile:
                tabla2[1].append(self.countsTypeFile[key])
        
        return tabla, tabla2

    def generarTablas(self):
        fig = plt.figure(figsize=(20, 6))
        ax1 = plt.subplot(2,2,1)
        table = ax1.table(cellText = self.generateLista()[0], loc = "center", cellLoc = 'center')
        ax1.axis('tight')
        ax1.axis('off')
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        ax1.set_title('\nTabla de permisos')

        ax2 = plt.subplot(2,2,3)
        table2 = ax2.table(cellText = self.generateLista()[1], loc = "center", cellLoc = 'center')
        ax2.axis('tight')
        ax2.axis('off')
        table2.auto_set_font_size(False)
        table2.set_fontsize(8)
        ax2.set_title('\nTabla de archivos')

        ax5 =plt.subplot(2,2,2)
        ax5.set_title('Leyendas')
        ax5.text(0.2, 0.9, 'r: Permiso de lectura', fontsize=10)
        ax5.text(0.2, 0.8, 'w: Permiso de escritura', fontsize=10)
        ax5.text(0.2, 0.7, 'x: Permiso de ejecución', fontsize=10)
        ax5.text(0.2, 0.6, 'rw: Permiso de lectura y escritura', fontsize=10)
        ax5.text(0.2, 0.5, 'rx: Permiso de lectura y ejecución', fontsize=10)
        ax5.text(0.2, 0.4, 'wx: Permiso de escritura y ejecución', fontsize=10)
        ax5.text(0.2, 0.3, 'rwx: Todos los permisos', fontsize=10)
        ax5.text(0.2, 0.2, '---: Ningún permiso', fontsize=10)
        ax5.axis('off')

        plt.show()
        