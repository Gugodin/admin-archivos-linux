from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(493, 317)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Entry = QLineEdit(self.centralwidget)
        self.Entry.setObjectName(u"Entry")
        self.Entry.setGeometry(QRect(80, 130, 361, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 100, 371, 20))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(QFont.Bold)
        self.label.setFont(font)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(170, 190, 161, 41))
        self.labelError = QLabel(self.centralwidget)
        self.labelError.setObjectName(u"labelError")
        self.labelError.setGeometry(QRect(90, 160, 171, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Entry.setText(QCoreApplication.translate("MainWindow", "C:\\Users\\humbe\\Desktop\\prueba", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pega la dirección del sistema a administrar.", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.labelError.setText("")