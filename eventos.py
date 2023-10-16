import sys
from datetime import datetime

from PyQt6.uic.properties import QtGui

import var
from datetime import *

class Eventos():


    def limpiar(self):
            try:
                listalimpiar = [var.ui.txtDni, var.ui.txtDate, var.ui.txtDni_2, var.ui.txtNombre, var.ui.txtDireccion, var.ui.txtMovil, var.ui.txtSalario]
                var.ui.lblCheckDNI.setText(None)
                var.ui.lblCheckDNI.setScaledContents(False)
                for i in listalimpiar:
                    i.setText(None)

            except Exception as error:
                print("Error al limpiar", error)
    @staticmethod
    def abrirCalendar(self):

        try:
            var.calendar.show()
        except Exception as error:
            print("erro en abrir", error)

    @staticmethod
    def abrirAcercaDe(self):

        try:
            var.acercade.show()

        except Exception as error:
            print("erro en abrir", error)

    @staticmethod
    def showSalir(self):
        try:
            var.ventana_salir.show()
        except Exception as error:
            print("erro en abrir", error)

    def hideSalir(self):
        try:
            var.ventana_salir.hide()
        except Exception as error:
            print("erro en abrir", error)


    @staticmethod
    def salirAcercaDe(self):

        try:
            var.acercade.hide()
        except Exception as error:
            print("erro en abrir", error)
    @staticmethod
    def salir(self):

        try:
            sys.exit()
        except Exception as error:
            print("erro en abrir", error)


    def devolverFecha(self):
       fecha= datetime.now()
       fecha = fecha.strftime('%d-%m-%Y')
       return fecha