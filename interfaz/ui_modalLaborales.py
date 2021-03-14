# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modalLaboralestsGMwm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_modalFecha(object):
    def setupUi(self, modalFecha):
        if not modalFecha.objectName():
            modalFecha.setObjectName(u"modalFecha")
        modalFecha.resize(420, 597)
        modalFecha.setStyleSheet(u"border-color: rgb(255,255,255);\n"
"border-width: 7px;")
        self.lbl1 = QLabel(modalFecha)
        self.lbl1.setObjectName(u"lbl1")
        self.lbl1.setGeometry(QRect(20, 20, 351, 41))
        self.lbl1.setStyleSheet(u"background: rgba(255, 255,255,0);\n"
"color: #ffdf00;\n"
"font-size: 14px; ")
        self.lblFondoModal = QLabel(modalFecha)
        self.lblFondoModal.setObjectName(u"lblFondoModal")
        self.lblFondoModal.setGeometry(QRect(-10, -20, 441, 621))
        #self.lblFondoModal.setStyleSheet(u"background-image: url(\"img/FONDO.png\");")
        self.calendarWidget = QCalendarWidget(modalFecha)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(19, 60, 381, 241))
        self.grupoBotones = QGroupBox(modalFecha)
        self.grupoBotones.setObjectName(u"grupoBotones")
        self.grupoBotones.setGeometry(QRect(20, 320, 381, 181))
        self.grupoBotones.setStyleSheet(u"\n"
"\n"
#"background: rgba(0, 0,0,0);\n"
"color: #ffdf00;\n"
"font-size: 14px; ")
        self.checkLunes = QCheckBox(self.grupoBotones)
        self.checkLunes.setObjectName(u"checkLunes")
        self.checkLunes.setGeometry(QRect(20, 30, 81, 20))
        self.checkLunes.setStyleSheet(u"\n"
#"background: rgba(255, 255,255,0);\n"
"color: #ffffff;\n"
#"font-weight: bold;\n"
"font-size: 14px; ")
        self.checkMartes = QCheckBox(self.grupoBotones)
        self.checkMartes.setObjectName(u"checkMartes")
        self.checkMartes.setGeometry(QRect(20, 63, 81, 20))
        self.checkMartes.setStyleSheet(u"\n"
#"background: rgba(255, 255,255,0);\n"
"color: #ffffff;\n"
"font-size: 14px; ")
        self.checkMier = QCheckBox(self.grupoBotones)
        self.checkMier.setObjectName(u"checkMier")
        self.checkMier.setGeometry(QRect(20, 97, 101, 20))
        self.checkMier.setStyleSheet(u"\n"
#"background: rgba(255, 255,255,0);\n"
"color: #ffffff;\n"
"font-size: 14px; ")
        self.checkSabado = QCheckBox(self.grupoBotones)
        self.checkSabado.setObjectName(u"checkSabado")
        self.checkSabado.setGeometry(QRect(150, 65, 91, 20))
        self.checkSabado.setStyleSheet(u"\n"
#"background: rgba(255, 255,255,0);\n"
"color: #ffffff;\n"
"font-size: 14px; ")
        self.checkViernes = QCheckBox(self.grupoBotones)
        self.checkViernes.setObjectName(u"checkViernes")
        self.checkViernes.setGeometry(QRect(150, 31, 91, 20))
        self.checkViernes.setStyleSheet(u"\n"
#"background: rgba(255, 255,255,0);\n"
"color: #ffffff;\n"
"font-size: 14px; ")
        self.checkDom = QCheckBox(self.grupoBotones)
        self.checkDom.setObjectName(u"checkDom")
        self.checkDom.setGeometry(QRect(150, 98, 121, 20))
        self.checkDom.setStyleSheet(u"\n"
#"background: rgba(255, 255,255,0);\n"
"color: #ffffff;\n"
"font-size: 14px; ")
        self.checkJueves = QCheckBox(self.grupoBotones)
        self.checkJueves.setObjectName(u"checkJueves")
        self.checkJueves.setGeometry(QRect(20, 131, 91, 20))
        self.checkJueves.setStyleSheet(u"\n"
#"background: rgba(255, 255,255,0);\n"
"color: #ffffff;\n"
"font-size: 14px; ")
        self.btnAceptarFecha = QPushButton(modalFecha)
        self.btnAceptarFecha.setObjectName(u"btnAceptarFecha")
        self.btnAceptarFecha.setGeometry(QRect(148, 520, 121, 41))
        self.btnAceptarFecha.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAceptarFecha.setStyleSheet(u"font-size: 18px; font-weight: bold; font-family: Roboto; color: #009999;\n"
"background: rgb(250,250,250);\n"
"border-radius: 10px;")
        self.lblFondoModal.raise_()
        self.lbl1.raise_()
        self.calendarWidget.raise_()
        self.grupoBotones.raise_()
        self.btnAceptarFecha.raise_()

        self.retranslateUi(modalFecha)

        QMetaObject.connectSlotsByName(modalFecha)
    # setupUi

    def retranslateUi(self, modalFecha):
        modalFecha.setWindowTitle(QCoreApplication.translate("modalFecha", u"D\u00edas Laborables", None))
        self.lbl1.setText(QCoreApplication.translate("modalFecha", u"Seleccione la fecha incial del proyecto:", None))
        self.lblFondoModal.setText("")
        self.grupoBotones.setTitle(QCoreApplication.translate("modalFecha", u"Seleccione los d\u00edas de la semana que no se trabajar\u00e1n:", None))
        self.checkLunes.setText(QCoreApplication.translate("modalFecha", u"Lunes", None))
        self.checkMartes.setText(QCoreApplication.translate("modalFecha", u"Martes", None))
        self.checkMier.setText(QCoreApplication.translate("modalFecha", u"Mi\u00e9rcoles", None))
        self.checkSabado.setText(QCoreApplication.translate("modalFecha", u"S\u00e1bado", None))
        self.checkViernes.setText(QCoreApplication.translate("modalFecha", u"Viernes", None))
        self.checkDom.setText(QCoreApplication.translate("modalFecha", u"Domingo", None))
        self.checkJueves.setText(QCoreApplication.translate("modalFecha", u"Jueves", None))
        self.btnAceptarFecha.setText(QCoreApplication.translate("modalFecha", u"Aceptar", None))
    # retranslateUi

