import os.path
import shutil
import sys
import zipfile

import xlwt
import xlrd
from PyQt6.QtGui import QIcon

import conexion

import var
from datetime import *
from PyQt6 import QtWidgets, QtCore, QtSql
import locale

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')


class Eventos:

    def importar_datos(self):
        try:
            filename = var.dlg_abrir.getOpenFileName(None, 'Importar datos', '', '*.xls;;Allfiles(*)')
            if var.dlg_abrir.accept and filename != '':
                file = filename[0]
                documento = xlrd.open_workbook(file)
                datos = documento.sheet_by_index(0)
                filas = datos.nrows
                columnas = datos.ncols

                for i in range(filas):
                    if i == 0:
                        pass
                    else:
                        new = []
                        for j in range(columnas):
                            if j == 1:
                                dato = str(datos.cell_value(i, j))
                                dato = xlrd.xldate.xldate_as_datetime(datos.cell_value(i, j),
                                                                      documento.datemode).strftime('%d/%m/%Y')
                                new.append(str(dato))
                            else:
                                new.append(str(datos.cell_value(i, j)))
                        conexion.Conexion.guardardri(new)
                    if i == filas - 1:
                        mbox = QtWidgets.QMessageBox()
                        mbox.setWindowTitle('Aviso')
                        mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                        mbox.setText('Empleado dado de alta')
                        icon = QIcon('./img/taxiIcon.png')
                        mbox.setWindowIcon(icon)
                        mbox.exec()
            conexion.Conexion.mostrardrivers()



        except Exception as error:
            print("Error al importar datos", error)

    def exportar_datos_xls(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            file = (str(fecha) + 'Datos.xls')
            directorio, filename = var.dlg_abrir.getSaveFileName(None, 'Exportar datos en XLS', file, '.xls')
            if var.dlg_abrir.accept and filename:
                wb = xlwt.Workbook()
                sheet1 = wb.add_sheet('conductores')
                sheet1.write(0, 0, 'ID')
                sheet1.write(0, 1, 'DNI')
                sheet1.write(0, 2, 'Fecha Alta')
                sheet1.write(0, 3, 'Apellidos')
                sheet1.write(0, 4, 'Nombre')
                sheet1.write(0, 5, 'Direccion')
                sheet1.write(0, 6, 'Provincia')
                sheet1.write(0, 7, 'Localidad')
                sheet1.write(0, 8, 'Movil')
                sheet1.write(0, 9, 'Salario')
                sheet1.write(0, 10, 'Licencias')
                sheet1.write(0, 11, 'Fecha baja')

                registros = conexion.Conexion.select_all_driver(self)

                for j, registro in enumerate(registros, 1):
                    for i, valor in enumerate(registro):
                        sheet1.write(j, i, valor)
                wb.save(directorio)
                mbox = QtWidgets.QMessageBox()
                mbox.setModal(True)

                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Se ha exportado los datos correctamente")
                mbox.exec()


        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("Error exportar datos en hoja de calculo", error)
            mbox.exec()

    def restaurar_back_up(self):
        try:
            filename = var.dlg_abrir.getOpenFileName(None, 'Restaurar copia de seguridad',
                                                     '', '*.zip;;All Files(*)')
            file = filename[0]
            if var.dlg_abrir.accept and file:
                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Copia restaturada")
                mbox.exec()
                conexion.Conexion.mostrardrivers()


        except Exception as error:

            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("Error en la copia de seguridad", error)
            mbox.exec()

    def crear_back_up(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            copia = str(fecha) + "_backup.zip"
            directorio, filename = var.dlg_abrir.getSaveFileName(None, 'Guardar copia de seguridad', copia, '.zip')
            if var.dlg_abrir.accept and filename is not None:
                fichzip = zipfile.ZipFile(copia, 'w')
                fichzip.write(var.bbdd, os.path.basename(var.bbdd), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(copia), str(directorio))
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Copia se seguridad creada")
                mbox.exec()



        except Exception as error:
            print(error)
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("Error en la copia de seguridad", error)
            mbox.exec()

    @staticmethod
    def limpiar():
        try:
            conexion.Conexion.mostrardrivers()
            listalimpiar = [var.ui.txtDni, var.ui.txtDate, var.ui.txtDni_2, var.ui.txtNombre, var.ui.txtDireccion,
                            var.ui.txtMovil, var.ui.txtSalario, var.ui.lblCodDB]
            # var.ui.lblCheckDNI.hide()
            var.ui.lblCheckDNI.setText(" ")
            # var.ui.lblCheckDNI.setScaledContents(False)
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
        fecha = fecha.strftime("%A-" + '%d-%m-%Y')
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
