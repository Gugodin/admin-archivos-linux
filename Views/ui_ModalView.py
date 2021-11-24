from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(335, 213)
        self.text = QLabel(Dialog)
        self.text.setObjectName(u"text")
        self.text.setGeometry(QRect(20, 30, 301, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(QFont.Bold)
        self.text.setFont(font)
        self.text.setAlignment(Qt.AlignCenter)
        self.aceptar = QPushButton(Dialog)
        self.aceptar.setObjectName(u"aceptar")
        self.aceptar.setGeometry(QRect(120, 150, 91, 31))
        self.entrada = QLineEdit(Dialog)
        self.entrada.setObjectName(u"entrada")
        self.entrada.setGeometry(QRect(20, 90, 301, 31))
        self.nombreA = QLabel(Dialog)
        self.nombreA.setObjectName(u"nombreA")
        self.nombreA.setGeometry(QRect(20, 90, 301, 31))
        self.nombreA.setFont(font)
        self.nombreA.setAlignment(Qt.AlignCenter)
        self.nombreA.raise_()
        self.text.raise_()
        self.aceptar.raise_()
        self.entrada.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.text.setText("")
        self.aceptar.setText(QCoreApplication.translate("Dialog", u"Aceptar", None))
        self.nombreA.setText("")
    # retranslateUi

