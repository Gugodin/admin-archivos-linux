from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_window2(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(695, 492)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.busqueda = QLineEdit(self.centralwidget)
        self.busqueda.setObjectName(u"busqueda")
        self.busqueda.setGeometry(QRect(20, 40, 341, 20))
        self.buscar = QPushButton(self.centralwidget)
        self.buscar.setObjectName(u"buscar")
        self.buscar.setGeometry(QRect(370, 40, 75, 23))
        self.permisos = QPushButton(self.centralwidget)
        self.permisos.setObjectName(u"permisos")
        self.permisos.setGeometry(QRect(530, 30, 111, 41))
        self.crear = QPushButton(self.centralwidget)
        self.crear.setObjectName(u"crear")
        self.crear.setGeometry(QRect(510, 130, 141, 51))
        self.editar = QPushButton(self.centralwidget)
        self.editar.setObjectName(u"editar")
        self.editar.setGeometry(QRect(510, 220, 141, 51))
        self.eliminar = QPushButton(self.centralwidget)
        self.eliminar.setObjectName(u"eliminar")
        self.eliminar.setGeometry(QRect(510, 310, 141, 51))
        self.opcion1 = QLabel(self.centralwidget)
        self.opcion1.setObjectName(u"opcion1")
        self.opcion1.setGeometry(QRect(200, 70, 81, 21))
        self.opcion2 = QLabel(self.centralwidget)
        self.opcion2.setObjectName(u"opcion2")
        self.opcion2.setGeometry(QRect(290, 70, 81, 21))
        self.recomendacion = QLabel(self.centralwidget)
        self.recomendacion.setObjectName(u"recomendacion")
        self.recomendacion.setGeometry(QRect(30, 70, 131, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(490, 370, 161, 101))
        self.label.setPixmap(QPixmap(u"../img/img.png"))
        self.label.setScaledContents(True)
        self.tabla = QTableWidget(self.centralwidget)
        if (self.tabla.columnCount() < 3):
            self.tabla.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setGeometry(QRect(20, 90, 433, 377))
        self.tabla.setColumnWidth(0,190)
        self.tabla.setColumnWidth(2,119)
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla.setDragDropOverwriteMode(False)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)   
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.permisos.setText(QCoreApplication.translate("MainWindow", u"Ver permisos", None))
        self.crear.setText(QCoreApplication.translate("MainWindow", u"Crear archivo", None))
        self.editar.setText(QCoreApplication.translate("MainWindow", u"Editar nombre de archivo", None))
        self.eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar archivo", None))
        self.opcion1.setText("")
        self.opcion2.setText("")
        self.recomendacion.setText("")
        self.label.setText("")
        ___qtablewidgetitem = self.tabla.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nombre del archivo", None));
        ___qtablewidgetitem1 = self.tabla.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Usuario", None));
        ___qtablewidgetitem2 = self.tabla.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
    # retranslateUi

