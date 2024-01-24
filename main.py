import locale
import sys
from PyQt6.QtWidgets import QApplication
import cliente

from MainWindow import *
import conexion
from facturacion import facturacion

from windowaux import *
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        var.calendar = Calendar()
        var.acercade = Acerca()
        var.print_facturas = print_dialog()
        var.ventana_salir = SalirVentana()
        var.dlg_abrir = FileDialogAbrir()
        conexion.Conexion.conexion()
        conexion.Conexion.cargar_provincias(var.ui.cmb_provincia_origen)
        conexion.Conexion.cargar_provincias(var.ui.cmb_provincia_destino)
        conexion.Conexion.cargar_provincias(var.ui.cmbProvincia)
        conexion.Conexion.cargar_provincias(var.ui.cmbProvincia_Cliente)
        conexion.Conexion.cargar_cmb_drivers_facturacion()
        conexion.Conexion.mostrardrivers()
        conexion.Conexion.mostrarclientes()
        conexion.Conexion.cargar_facturas()
        var.ui.frame.hide()

        '''
        
        ZONA DE EVENTOS
        
        
        
        
        
        
        '''

        '''
        combobox
        '''

        var.ui.cmb_provincia_origen.currentIndexChanged.connect(lambda: conexion.Conexion.sel_muni_parametrizado(var.ui.cmb_provincia_origen,var.ui.cmb_localidad_origen))
        var.ui.cmb_provincia_destino.currentIndexChanged.connect(lambda: conexion.Conexion.sel_muni_parametrizado(var.ui.cmb_provincia_destino,var.ui.cmb_localidad_destino))
        var.ui.cmbProvincia.currentIndexChanged.connect(lambda: conexion.Conexion.sel_muni_parametrizado(var.ui.cmbProvincia, var.ui.cmbLocalidad))
        var.ui.cmbProvincia_Cliente.currentIndexChanged.connect(lambda: conexion.Conexion.sel_muni_parametrizado(var.ui.cmbProvincia_Cliente,var.ui.cmbLocalidad_Cliente))

            ## Metodos para poder calcular la tarifa segun cambie el comboBox
        var.ui.cmb_localidad_origen.currentIndexChanged.connect(facturacion.Facturacion.calcular_tarifa)
        var.ui.cmb_localidad_destino.currentIndexChanged.connect(facturacion.Facturacion.calcular_tarifa)
                    # --------------------------------------  #

        '''
        botones
        '''
        var.ui.btnCalendar.clicked.connect(lambda: drivers.Drivers.set_calendar("fecha alta driver"))
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrir_calendar)
        var.ui.btnCalendar_2.clicked.connect(lambda: drivers.Drivers.set_calendar("fecha baja driver"))
        var.ui.btnCalendar_2.clicked.connect(eventos.Eventos.abrir_calendar)
        var.ui.btnCalendar_Cliente.clicked.connect(lambda: drivers.Drivers.set_calendar("fecha baja cliente"))
        var.ui.btnCalendar_Cliente.clicked.connect(eventos.Eventos.abrir_calendar)
        var.ui.btn_fecha_factura.clicked.connect(lambda: drivers.Drivers.set_calendar("fecha factura"))
        var.ui.btn_fecha_factura.clicked.connect(eventos.Eventos.abrir_calendar)
        var.ui.actionAcerca_de.triggered.connect(eventos.Eventos.abrir_acerca_de)
        var.ui.btn_menu_print.triggered.connect(eventos.Eventos.printear_informes)
        var.ui.btn_grabar_registro_viaje.clicked.connect(facturacion.Facturacion.insertar_datos_viaje)
        '''
      
        
        
        
        
        
        botones Driver
        '''
        var.ui.btnaltaDriver.clicked.connect(drivers.Drivers.alta_driver)
        var.ui.btnBuscarDri.clicked.connect(drivers.Drivers.get_from_dni)
        var.ui.btnModifDriver.clicked.connect(drivers.Drivers.modif_driver)
        var.ui.buttonGroup.buttonClicked.connect(conexion.Conexion.mostrardrivers)
        var.ui.buttonGroup.buttonClicked.connect(eventos.Eventos.limpiar)
        var.ui.btnBajaDriver.clicked.connect(drivers.Drivers.borrar_datos)
        var.ui.actionListarConductores.triggered.connect(informes.informes.report_conductores)

        '''
        botones Cliente
        '''
        var.ui.btnaltaCliente.clicked.connect(cliente.Cliente.alta_cliente)
        var.ui.btnBuscarCliente.clicked.connect(cliente.Cliente.get_from_dni)
        var.ui.btnModifCliente.clicked.connect(conexion.Conexion.modificar_cliente)
        var.ui.btnBajaCliente.clicked.connect(cliente.Cliente.baja_cliente)
        var.ui.botonesDeCliente.buttonClicked.connect(conexion.Conexion.mostrarclientes)
        var.ui.botonesDeCliente.buttonClicked.connect(eventos.Eventos.limpiar)
        var.ui.actionListar_Clientes.triggered.connect(informes.informes.reportclientes)
        var.ui.btnBuscar_Cli_facturacion.clicked.connect(cliente.Cliente.get_from_dni)
        '''
              botones Facturacion
              '''
        var.ui.btn_facturar.clicked.connect(facturacion.Facturacion.crear_registro)
        '''
        zona de eventos salir
        '''
        var.ui.actionSalir.triggered.connect(eventos.Eventos.show_salir)
        var.ui.actionCrear_Copia_Seguridad.triggered.connect(eventos.Eventos.crear_back_up)
        var.ui.actionRestarurar_Copia.triggered.connect(eventos.Eventos.restaurar_back_up)

        """
        zona de eventos cajas
        """
        var.ui.txtDni.editingFinished.connect(lambda: drivers.Drivers.validar_dni(var.ui.txtDni.text()))
        var.ui.txtDni_3.editingFinished.connect(lambda: cliente.Cliente.validar_dni(var.ui.txtDni_3.text()))
        var.ui.txtNombre.editingFinished.connect(eventos.Eventos.format_caja_texto)
        var.ui.txtDni_2.editingFinished.connect(eventos.Eventos.format_caja_texto)
        var.ui.txtSalario.editingFinished.connect(eventos.Eventos.format_caja_texto)
        var.ui.txtMovil.editingFinished.connect(drivers.Drivers.validar_tlf)
        var.ui.txtMovil_Cliente.editingFinished.connect(cliente.Cliente.validar_tlf)
        var.ui.txtSalario.editingFinished.connect(drivers.Drivers.validar_salario)

        """
        
        eventos de la menubar
        
        """
        var.ui.Salir.triggered.connect(eventos.Eventos.show_salir)
        var.ui.btnLimpiar.triggered.connect(eventos.Eventos.limpiar)
        var.ui.actionExportar_Datos_XLS.triggered.connect(eventos.Eventos.exportar_datos_xls)
        var.ui.actionImportar_Datos_XLS.triggered.connect(eventos.Eventos.importar_datos)
        var.ui.actionImportar_Datos_Cliente_XLS.triggered.connect(eventos.Eventos.importar_datos_clientes)
        '''
        
        status var
    
        '''

        eventos.Eventos.cargastatusbar(self)

        '''
        eventos de tablas  
        '''
        eventos.Eventos.resize_tabDriver2(self)
        eventos.Eventos.resize_tabClientes(self)
        eventos.Eventos.resize_tab_facturas(self)
        var.ui.tabDriver2.clicked.connect(drivers.Drivers.get_from_tab)
        var.ui.tabClientes.clicked.connect(cliente.Cliente.get_from_tab)
        var.ui.tab_facturas.clicked.connect(facturacion.Facturacion.mostrar_datos_factura)

    def closeEvent(self, event):

        mbox = QtWidgets.QMessageBox.information(self, "Salir", "Estas seguro de salir?",
                                                 QtWidgets.QMessageBox.StandardButton.Yes |
                                                 QtWidgets.QMessageBox.StandardButton.No)

        if mbox == QtWidgets.QMessageBox.StandardButton.Yes:
            app.quit()
        if mbox == QtWidgets.QMessageBox.StandardButton.No:
            event.ignore()


if __name__ == '__main__':
    app = QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())
