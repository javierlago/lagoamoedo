import sys

import eventos
import var
from datetime import *
from PyQt6 import QtWidgets, QtCore, QtSql
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')

class Eventos:





    @staticmethod
    def limpiar():
        try:
            listalimpiar = [var.ui.txtDni, var.ui.txtDate, var.ui.txtDni_2, var.ui.txtNombre, var.ui.txtDireccion,
                            var.ui.txtMovil, var.ui.txtSalario,var.ui.lblCodDB]
            #var.ui.lblCheckDNI.hide()
            var.ui.lblCheckDNI.setText(" ")
            #var.ui.lblCheckDNI.setScaledContents(False)
            for i in listalimpiar:
                i.setText(None)
            chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]

            for i in chklicencia:
                i.setChecked(False)
            var.ui.cmbProvincia.setCurrentText("")
            var.ui.cmbLocalidad.setCurrentText("")



        except Exception as error:
            print("Error al limpiar", error)

    @staticmethod
    def abrir_calendar():

        try:
            var.calendar.show()
        except Exception as error:
            print("erro en abrir", error)

    @staticmethod
    def abrir_acerca_de():

        try:
            var.acercade.show()

        except Exception as error:
            print("erro en abrir", error)

    @staticmethod
    def show_salir():
        try:
            var.ventana_salir.show()
        except Exception as error:
            print("erro en abrir", error)

    @staticmethod
    def hide_salir():
        try:
            var.ventana_salir.hide()
        except Exception as error:
            print("erro en abrir", error)

    @staticmethod
    def salir_acerca_de():

        try:
            var.acercade.hide()
        except Exception as error:
            print("erro en abrir", error)

    @staticmethod
    def salir():

        try:
            sys.exit()
        except Exception as error:
            print("erro en abrir", error)

    @staticmethod
    def devolver_fecha():
        fecha = datetime.now()
        fecha = fecha.strftime("%A-"+'%d-%m-%Y')
        return fecha

    @staticmethod
    def cargastatusbar(self):
        '''

        Formatear la fecha según el formato deseadofecha_actual.strftime()
        statusbar
        '''
        Eventos.devolver_fecha()
        try:
            fecha = Eventos.devolver_fecha()
            self.labelstatus = QtWidgets.QLabel(fecha, self)
            self.labelstatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
            var.ui.statusbar.addPermanentWidget(self.labelstatus, 1)
            self.labelstatusversion = QtWidgets.QLabel("Version: " + var.version, self)
            self.labelstatusversion.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
            var.ui.statusbar.addPermanentWidget(self.labelstatusversion, 0)
        except Exception as error:
            print('Error cargar el statusbar: ', error)

    @staticmethod


    @staticmethod
    def sel_estado():
        if var.ui.rbtTodos.isChecked():
            print("Pulsaste todos")
        elif var.ui.rbtAlta.isChecked():
            print("Pulsaste Alta")
        elif var.ui.rbtBaja.isChecked():
            print("Pulsaste Baja")


    def resize_tabDriver2(self):
        try:
            header = var.ui.tabDriver2.horizontalHeader()
            for i in range(5):
                if i == 0 or i == 4 or i == 3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)


        except Exception as error:
            print("error resize tab driver", error)

    @staticmethod
    def format_caja_texto(self=None):
        try:
            var.ui.txtDni_2.setText(var.ui.txtDni_2.text().title())
            var.ui.txtNombre.setText(var.ui.txtNombre.text().title())
            var.ui.txtSalario.setText(str(locale.currency(float(var.ui.txtSalario.text()))))

        except Exception as error:
            print("error letra capital", error)


