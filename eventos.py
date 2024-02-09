import os.path
import shutil
import sys
import zipfile

import xlwt
import xlrd

import Ventanas
import cliente
import conexion
import drivers
import informes

import var
from datetime import *

import locale
from PyQt6 import QtCore, QtGui, QtWidgets

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')


class Eventos:

    @staticmethod
    def abrir_window_print(self):
        '''
        Metodo para abrir la ventana para imprimir facturas.
        :param self:
        :type self:

        '''
        try:
            var.print_facturas.show()

        except Exception as error:
            print("erro en abrir", error)

    def importar_datos_clientes(self):
        '''
        Metodo para importar datos de los clientes desde un archivo XLS
        :return: None
        :rtype: None
        '''
        try:
            estado = 0
            inserciones = 0
            dniRepetidos = False
            dniMalFormdos = False
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
                            if j == 3:
                                new.append(int(datos.cell_value(i, j)))
                            else:
                                new.append(str(datos.cell_value(i, j)))
                        if cliente.Cliente.validar_dni(str(new[0])) and not conexion.Conexion.dni_existe(str(new[0])):
                            new.append('')
                            conexion.Conexion.guardarCliente(new)
                            inserciones = inserciones + 1
                        elif estado == 0:
                            if not cliente.Cliente.validar_dni(str(new[0])):
                                dniMalFormdos = True
                            if conexion.Conexion.dni_existe(str(new[0])):
                                dniRepetidos = True

                    if i == filas - 1:
                        if inserciones > 0:
                            Ventanas.Ventanas.ventana_info(f"Se han añadido  {inserciones} clientes.")
                        if dniRepetidos:
                            Ventanas.Ventanas.ventana_info(
                                'Existen Dni en el documento que ya estan en la base de datos')
                        if dniMalFormdos:
                            Ventanas.Ventanas.mensaje_warning('Dnis mal formados en el documeto')
            conexion.Conexion.mostrarclientes()
        except Exception as error:
            print("Error al importar datos", error)

    def importar_datos(self):
        '''
        Metodos par importar datos de conductores.
        :return: None
        :rtype: None
        '''
        try:
            estado = 0
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
                            dato = str(datos.cell_value(i, j))

                            if j == 1:
                                if datos.cell_type(i, j) == xlrd.XL_CELL_DATE:
                                    dato = xlrd.xldate.xldate_as_datetime(dato, documento.datemode).strftime('%d/%m/%Y')

                            new.append(str(dato))
                        if drivers.Drivers.validar_dni(str(new[0])):
                            new.append('')
                            conexion.Conexion.guardardri(new)
                        elif estado == 0:
                            Ventanas.Ventanas.ventana_info('Hay DNI incorrectos')
                            estado = 1
                    if i == filas - 1:
                        Ventanas.Ventanas.ventana_info('Empleados dados de alta')
            conexion.Conexion.mostrardrivers()
        except Exception as e:
            print(f"Error al importar datos: {str(e)}")

    def exportar_datos_xls(self):
        '''
        Metodo para expottar datos de los conductores.
        :return: None
        :rtype: None
        '''
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            file = (str(fecha) + 'Datos.xls')
            directorio, filename = var.dlg_abrir.getSaveFileName(None, 'Exportar datos en XLS', file, '.xls')
            if var.dlg_abrir.accept and filename != '':
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
            Ventanas.Ventanas.ventana_info("Se ha exportado los datos correctamente")


        except Exception as error:
            Ventanas.Ventanas.mensaje_warning("Error exportar datos en hoja de calculo", error)

    def restaurar_back_up(self):
        '''
        Metodo para restaurar la base de datos desde un archivo.
        :return:
        :rtype:
        '''
        try:
            filename = var.dlg_abrir.getOpenFileName(None, 'Restaurar copia de seguridad',
                                                     '', '*.zip;;All Files(*)')
            file = filename[0]
            if var.dlg_abrir.accept and file:
                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall(pwd=None)
                Ventanas.Ventanas.ventana_info("Copia restaurada")
                conexion.Conexion.mostrardrivers()

        except Exception as error:

            Ventanas.Ventanas.mensaje_warning("Error en la copia de seguridad", error)

    def crear_back_up(self):
        '''
        Metodo para crear un copia de seguridad de nuestra base de datos.

        :return: None
        :rtype: None
        '''
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            copia = str(fecha) + "_backup.zip"
            directorio, filename = var.dlg_abrir.getSaveFileName(None, 'Guardar copia de seguridad', copia, '.zip')
            if var.dlg_abrir.accept and filename != '':
                fichzip = zipfile.ZipFile(copia, 'w')
                fichzip.write(var.bbdd, os.path.basename(var.bbdd), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(copia), str(directorio))
                Ventanas.Ventanas.ventana_info("Copia se seguridad creada")



        except Exception as error:
            Ventanas.Ventanas.mensaje_warning("Error en la copia de seguridad", error)

    @staticmethod
    def limpiar():
        '''

         Metodo que pone en blanco todos los paneles de la interfaz.Este metodo esta asociado a un boton en el menuBar de la aplicacion.
        :return: None
        :rtype: None.

        '''
        try:
            conexion.Conexion.mostrardrivers()
            conexion.Conexion.mostrarclientes()
            conexion.Conexion.cargar_facturas()
            listalimpiar = [var.ui.txtDni, var.ui.txtDate, var.ui.txtDni_2, var.ui.txtNombre, var.ui.txtDireccion,
                            var.ui.txtMovil, var.ui.txtSalario, var.ui.lblCodDB, var.ui.txtDate_2,
                            var.ui.lblCodDB_Cliente, var.ui.txtDni_3, var.ui.txtRazonSocial,
                            var.ui.txtDireccion_Cliente, var.ui.txtMovil_Cliente, var.ui.txtDate_Cliente,
                            var.ui.txt_numero_factura, var.ui.txt_cif_cliente,
                            var.ui.txt_fecha_factura, var.ui.txt_subtotal, var.ui.txt_iva, var.ui.txt_total,
                            var.ui.txt_kilometros]
            # var.ui.lblCheckDNI.hide()
            var.ui.lblCheckDNI.setText(" ")
            var.ui.lblCheckDNI_Cliente.setText(" ")
            # var.ui.lblCheckDNI.setScaledContents(False)
            for i in listalimpiar:
                i.setText(None)
            chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]

            for i in chklicencia:
                i.setChecked(False)
            var.ui.cmbProvincia.setCurrentText("")
            var.ui.cmbProvincia_Cliente.setCurrentText("")
            var.ui.cmbLocalidad.setCurrentText("")
            var.ui.cmbLocalidad_Cliente.setCurrentText("")
            var.ui.tab_lineas_de_viaje.setRowCount(0)
            var.ui.btn_modificar_viaje.setVisible(False)
            var.ui.cmb_listado_conductores.setCurrentText("")
            var.ui.cmb_provincia_origen.setCurrentText('')
            var.ui.cmb_provincia_destino.setCurrentText('')
            var.ui.cmb_localidad_origen.setCurrentText('')
            var.ui.cmb_localidad_destino.setCurrentText('')
        except Exception as error:
            print("Error al limpiar", error)

    @staticmethod
    def abrir_calendar():
        '''
        Metod para abrir la ventana de calendario.
        :return: None
        :rtype: None
        '''

        try:
            var.calendar.show()

        except Exception as error:
            print("erro en abrir", error)


    @staticmethod
    def abrir_acerca_de():
        '''
        Meotodo utilizado para abrir el la ventana "Acerca de " donde se mostrara información sobre el programa.
        Este metodo se ejecuta al pulsar el boton que hay en el estatus bar del programa.
        :return: None
        :rtype: None
        '''

        try:
            var.acercade.show()

        except Exception as error:
            print("erro en abrir", error)

    @staticmethod
    def show_salir():
        '''
        Metodo que abre la ventana salir, indicado si quiere salir del programa.
        :return: None
        :rtype: None
        '''
        try:
            var.ventana_salir.show()
        except Exception as error:
            print("erro en abrir", error)

    @staticmethod
    def hide_salir():
        '''
        Metodo para ocular la ventana de dialogo de salir del programa.
        :return: None
        :rtype: None
        '''
        try:
            var.ventana_salir.hide()
        except Exception as error:
            print("erro en abrir", error)

    @staticmethod
    def salir_acerca_de():
        '''
        Metodo para ocultar el cuadro de dialogo en de la ventana "Acerca de", este metodo sera ejecutado cuando en la propia ventana se pulse sobre el boton aceptar
        :return: None
        :rtype: None
        '''

        try:
            var.acercade.hide()
        except Exception as error:
            print("erro en abrir", error)

    @staticmethod
    def salir():
        '''
        Metodo para salir del programa. Cuando en el cuadro de dialogo de la ventana "Salir" se pulsa el boton aceptar se ejecutara este metodo
        :return:
        :rtype:
        '''

        try:
            sys.exit()
        except Exception as error:
            print("erro en abrir", error)

    @staticmethod
    def devolver_fecha():
        '''
        Metodo que devuelve la fecha actual con un formato dia/mes/año
        :return: fecha
        :rtype: datetime
        '''
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
        '''
         Metodo para dar forma a la tabla de conductores
        :param self:
        :type self:
        :return: None
        :rtype: None

        '''
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
    def resize_tabClientes(self):
        '''
        Metodo para dar forma a la tabla de clientes


        :param self:
        :type self:
        :return:
        :rtype:
        '''
        try:
            header = var.ui.tabClientes.horizontalHeader()
            for i in range(5):
                if i == 0 or i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)


        except Exception as error:
            print("error resize tab driver", error)

    @staticmethod
    def resize_tab_facturas(self):
        """
           Método estático para redimensionar las columnas de una tabla de facturas en una interfaz de usuario.

           :param self: Referencia al objeto actual.
           :type self: object

           :raises: No se producen excepciones explícitas en este método, pero pueden ocurrir excepciones
                    durante la ejecución del código dentro del bloque try.

           :return: None

           """
        try:
            header = var.ui.tab_facturas.horizontalHeader();
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)


        except Exception as error:
            print("error resize tab driver", error)

    @staticmethod
    def format_caja_texto(self=None):
        """
        Método estático para formatear el texto en las cajas de texto de una interfaz de usuario.

        :param self: Referencia al objeto actual. Por defecto es None.
        :type self: object or None

        :raises: No se producen excepciones explícitas en este método, pero pueden ocurrir excepciones
                 durante la ejecución del código dentro del bloque try.

        :return: None

  .
        """
        try:
            var.ui.txtDni_2.setText(var.ui.txtDni_2.text().title())
            var.ui.txtNombre.setText(var.ui.txtNombre.text().title())
            # var.ui.txtSalario.setText(str(locale.currency(float(var.ui.txtSalario.text()))))

        except Exception as error:
            print("error letra capital", error)

    @staticmethod
    def printear_informes(self):
        """
          Método estático para imprimir informes seleccionados en una interfaz de usuario.

          :param self: Referencia al objeto actual.
          :type self: object

          :raises: No se producen excepciones explícitas en este método, pero pueden ocurrir excepciones
                   durante la ejecución del código dentro del bloque try.

          :return: None

          Descripción:
          Este método muestra un cuadro de diálogo para que el usuario seleccione los informes que desea imprimir.
          Los informes disponibles incluyen 'Informe de conductores' y 'Informe de clientes'.
          Después de que el usuario elige los informes y hace clic en 'Aceptar', se crean los informes correspondientes
          y se muestra un mensaje de confirmación. Si no se selecciona ningún informe, se muestra un mensaje de advertencia.
          """
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle("Realizar Informe")
            mbox.setWindowIcon(QtGui.QIcon("img/impresora.png"))
            mbox.setText("Seleccione informe/es")

            conductorcheck = QtWidgets.QCheckBox("Informe de conductores")
            clientecheck = QtWidgets.QCheckBox("Informe de clientes")

            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(conductorcheck)
            layout.addWidget(clientecheck)

            container = QtWidgets.QWidget()
            container.setLayout(layout)

            mbox.layout().addWidget(container, 1, 1, 1, mbox.layout().columnCount())

            mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Aceptar')
            mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('Cancelar')

            resultado = mbox.exec()

            if resultado == QtWidgets.QMessageBox.StandardButton.Yes:
                if conductorcheck.isChecked():
                    Ventanas.Ventanas.ventana_info("Se ha creado el infome clientes")
                    informes.informes.reportclientes(self)
                if clientecheck.isChecked():
                    Ventanas.Ventanas.ventana_info("Se ha creado el informe de condutores")
                    informes.informes.report_conductores(self)

                if not (conductorcheck.isChecked() or clientecheck.isChecked()):
                    Ventanas.Ventanas.ventana_info("Aviso", "No se ha seleccionado ningún informe")

        except Exception as error:
            print("Error en checkbox_informe", error)
