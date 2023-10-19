import sys
import var
from datetime import *
from PyQt6 import QtWidgets, QtCore


class Eventos:
    @staticmethod
    def limpiar():
        try:
            listalimpiar = [var.ui.txtDni, var.ui.txtDate, var.ui.txtDni_2, var.ui.txtNombre, var.ui.txtDireccion,
                            var.ui.txtMovil, var.ui.txtSalario]
            var.ui.lblCheckDNI.setText(None)
            var.ui.lblCheckDNI.setScaledContents(False)
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
    def cargaprov():
        try:
            prov = ["A Coruña", "Lugo", "Pontevedra", "Ferrol", "Santiago de Compostela", "Ourense"]
            var.ui.cmbProvincia.clear()
            var.ui.cmbProvincia.addItem('')
            for i, m in enumerate(prov):
                var.ui.cmbProvincia.addItem(str(m))

        except Exception as error:
            print("error al cargar", error)

    @staticmethod
    def sel_estado():
        if var.ui.rbtTodos.isChecked():
            print("Pulsaste todos")
        elif var.ui.rbtAlta.isChecked():
            print("Pulsaste Alta")
        elif var.ui.rbtBaja.isChecked():
            print("Pulsaste Baja")
