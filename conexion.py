import datetime
from datetime import datetime
from PyQt6 import QtWidgets, QtSql
from PyQt6.QtGui import QIcon

import Ventanas
import cliente
import conexion
import drivers
from Facturas import facturacion, facturacion_repository
import var


class Conexion:
    def borrarCliente(dni):
        try:

            fecha = datetime.now()
            fecha = fecha.strftime("%d/%m/%Y")
            valor = None
            query = QtSql.QSqlQuery()
            query.prepare('SELECT bajacliente FROM listadoClientes WHERE dnicliente = :dni ')
            query.bindValue(':dni', dni)
            if query.exec():
                while query.next():
                    valor = query.value(0)
            print(valor)
            if valor == "" or valor is None:
                fecha = datetime.now()
                fecha = fecha.strftime("%d/%m/%Y")
                queryFecha = QtSql.QSqlQuery()
                queryFecha.prepare('update listadoClientes set bajaCliente = :fechabaja where dnicliente = :dni')
                queryFecha.bindValue(':dni', str(dni))
                queryFecha.bindValue(':fechabaja', str(fecha))
                if queryFecha.exec():
                    Ventanas.Ventanas.ventana_info("Se ha dado de baja al empleado")
            else:
                Ventanas.Ventanas.mensaje_warning("El empeado ya esta dado de baja")


        except Exception as error:
            print("No se ha podido dar de baja al cliente", error)

    def modificar_cliente(self):
        try:
            cliente_a_modificar = cliente.Cliente.recuperar_datos()
            if cliente.Cliente.validar_datos(cliente_a_modificar):
                cliente_verificacion = conexion.Conexion.buscar_segun_dni_cliente(cliente_a_modificar[0])
                cliente_verificacion.pop(0)
                print(cliente_a_modificar)
                if cliente_a_modificar != cliente_verificacion:
                    query = QtSql.QSqlQuery()
                    query.prepare(
                        "update listadoClientes set  razon = :razon , direccion = :direccion ,telefono = :telf , provCliente = :pc , muniCliente = :mc , bajaCliente = :bc where dnicliente = :dni;")
                    query.bindValue(":dni", cliente_a_modificar[0])
                    query.bindValue(":razon", cliente_a_modificar[1])
                    query.bindValue(":direccion", cliente_a_modificar[2])
                    query.bindValue(":telf", cliente_a_modificar[3])
                    query.bindValue(":pc", cliente_a_modificar[4])
                    query.bindValue(":mc", cliente_a_modificar[5])
                    query.bindValue(":bc", cliente_a_modificar[6])
                    if query.exec():
                        Ventanas.Ventanas.ventana_info("modificacion realizada")
                        conexion.Conexion.mostrarclientes()
                    else:
                        Ventanas.Ventanas.mensaje_warning(str(query.lastError()))

                else:
                    Ventanas.Ventanas.mensaje_warning("No se ha modificado el cliente")
            else:
                Ventanas.Ventanas.mensaje_warning("Campos vaios")

        except Exception as error:

            print(error, query.lastError())

    def conexion(self=None):
        var.bbdd = 'bbdd.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(var.bbdd)
        if not db.open():
            print("Error de conexion")
            return False
        else:
            print("Base de datos conectada")
            return True

    def cargar_provincias(comboBox):
        try:
            comboBox.clear()
            query = QtSql.QSqlQuery()
            query.prepare("select provincia from provincias")
            if query.exec():
                comboBox.addItem("")
                while query.next():
                    # print(str(query.value(0)))
                    comboBox.addItem(query.value(0))
        except Exception as error:
            print("Error en la carga del combo prov: ", error)

    def sel_muni_parametrizado(comboBoxProvincia, comboBoxLocalidad):
        try:
            print(type(comboBoxLocalidad))
            comboBoxLocalidad.clear()
            id = 0
            prov = comboBoxProvincia.currentText()
            query = QtSql.QSqlQuery()
            query.prepare("select idprov from provincias where provincia = :prov")
            query.bindValue(':prov', prov)
            if query.exec():
                while query.next():
                    id = query.value(0)
            query1 = QtSql.QSqlQuery()
            query1.prepare("select municipio from municipios where idprov = :id")
            query1.bindValue(":id", int(id))
            if query1.exec():
                comboBoxLocalidad.addItem('')
                while query1.next():
                    comboBoxLocalidad.addItem(query1.value(0))
        except Exception as error:
            print("Error en la carga de municipios", error)

    ### Cargar los conductores en el combo box
    def cargar_cmb_drivers_facturacion(self=None):
        try:
            var.ui.cmb_listado_conductores.clear()
            query = QtSql.QSqlQuery()
            query.prepare("select codigo, apeldri from drivers where bajadri = '' order by codigo")
            var.ui.cmb_listado_conductores.addItem("")
            if query.exec():
                while query.next():
                    var.ui.cmb_listado_conductores.addItem(str(query.value(0)) + "  ||  " + str(query.value(1)))
        except Exception as error:
            print("Error en la carga de municipios", error)

    @staticmethod
    def guardardri(newdriver):
        try:
            print(newdriver)
            query = QtSql.QSqlQuery()
            query2 = QtSql.QSqlQuery()
            query2.prepare("select * from drivers where dnidri = :dni")
            query2.bindValue(':dni', newdriver[0])

            if newdriver[10] == '' and not query2.next():
                query.prepare('insert into drivers(dnidri, altadri, apeldri, nombredri, direcciondri, provdri, '
                              'munidri, movildri, salario, carnet, bajadri ) VALUES (:dni, :alta, :apel, :nombre, :direccion, '
                              ':provincia, :municipio, :movil, :salario, :carnet, :bajadri)')
            else:
                newdriver[10] = ''
                query.prepare("UPDATE drivers SET altadri = :alta, apeldri = :apel, nombredri = :nombre, direcciondri "
                              "= :direccion, provdri = :provincia, munidri = :municipio, movildri = :movil, "
                              "salario = :salario, carnet = :carnet ,bajadri = :bajadri WHERE dnidri = :dni;")

            query.bindValue(':dni', str(newdriver[0]))
            query.bindValue(':alta', str(newdriver[1]))
            query.bindValue(':apel', str(newdriver[2]))
            query.bindValue(':nombre', str(newdriver[3]))
            query.bindValue(':direccion', str(newdriver[4]))
            query.bindValue(':provincia', str(newdriver[5]))
            query.bindValue(':municipio', str(newdriver[6]))
            query.bindValue(':movil', str(newdriver[7]))
            query.bindValue(':salario', str(newdriver[8]))
            query.bindValue(':carnet', str(newdriver[9]))
            query.bindValue(':bajadri', str(newdriver[10]))
            if query.exec():
                return True

            else:
                print("Error al ejecutar la consulta:", query.lastError().text())
                return False
            # select de los datos de los conductores de la base de datos

        except Exception as error:
            print("Error al guardar el conductor", error)

    def modificar(driver):
        try:

            registro = conexion.Conexion.buscar_segun_codigo(driver[0])
            query = QtSql.QSqlQuery()

            # print(driver)
            # nuevoRegistro = driver
            # nuevoRegistro.pop(2)
            # print(nuevoRegistro)

            if registro != driver:
                nuevo_array = driver[:2] + driver[3:]
                driver.pop(0)
                if not drivers.Drivers.validar_datos(nuevo_array):
                    Ventanas.Ventanas.mensaje_warning("Campos Vacios")

                else:

                    query.prepare(
                        'UPDATE drivers SET altadri = :alta, apeldri = :apel, nombredri = :nombre, direcciondri = :direccion, provdri = :provincia, munidri = :municipio, movildri = :movil, salario = :salario, carnet = :carnet , bajadri = :bajadri WHERE dnidri = :dni ')
                    query.bindValue(':dni', str(driver[0]))
                    query.bindValue(':alta', str(driver[1]))
                    query.bindValue(':apel', str(driver[2]))
                    query.bindValue(':nombre', str(driver[3]))
                    query.bindValue(':direccion', str(driver[4]))
                    query.bindValue(':provincia', str(driver[5]))
                    query.bindValue(':municipio', str(driver[6]))
                    query.bindValue(':movil', str(driver[7]))
                    query.bindValue(':salario', str(driver[8]))
                    query.bindValue(':carnet', str(driver[9]))
                    query.bindValue(':bajadri', str(driver[10]))

                    if query.exec():
                        mbox = QtWidgets.QMessageBox()
                        mbox.setWindowTitle('Aviso')
                        mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                        mbox.setText('Se ha modificado la tabla')
                        icon = QIcon('./img/taxiIcon.png')
                        mbox.setWindowIcon(icon)
                        mbox.exec()

                    else:
                        Ventanas.Ventanas.mensaje_warning("Dni ya esta en la base de datos")

            else:
                Ventanas.Ventanas.mensaje_warning("No se han modificado los campos")
                # select de los datos de los conductores de la base de datos

        except Exception as error:
            print("Error al guardar el conductor", error)

    def mostrardrivers(self=None):
        try:
            registros = list()
            query1 = QtSql.QSqlQuery()
            query1.prepare("select codigo ,apeldrI ,nombredri ,movildri, "
                           "carnet,bajadri from drivers")
            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]
                    registros.append(row)

            drivers.Drivers.cargartabla(registros)



        except Exception as error:
            print("error al mostrar resultados", error)

    def mostrarclientes(self=None):
        try:
            registros = list()
            query1 = QtSql.QSqlQuery()
            query1.prepare("select codigo , razon ,telefono, provCliente, bajaCliente from listadoClientes")

            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]
                    registros.append(row)

            else:
                print(query1.lastError())
            cliente.Cliente.cargartabla(registros)



        except Exception as error:
            print("error al mostrar resultados", error)

    def buscar_segun_codigo(codigo):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM drivers WHERE codigo = :codigo")
            query.bindValue(":codigo", int(codigo))
            if query.exec():
                while query.next():
                    for i in range(12):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print("Error en fichero conexion datos de 1 driver: ", error)

    def buscar_segun_codigo_cliente(codigo):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM listadoClientes WHERE codigo = :codigo")
            query.bindValue(":codigo", int(codigo))
            if query.exec():
                while query.next():
                    for i in range(8):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print("Error en fichero conexion datos de 1 driver: ", error)

    def buscar_segun_dni(dni):

        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM drivers WHERE dnidri = :dnidri")
            query.bindValue(':dnidri', str(dni))
            if query.exec():
                while query.next():
                    for i in range(12):
                        registro.append(str(query.value(i)))
            else:
                Ventanas.Ventanas.mensaje_warning("Dni no esta en la base de datos")
            if registro[11] != '':
                var.ui.rbtAlta.isChecked()
            return registro

        except Exception as error:
            print("Error al buscar segun dni: ", error)

    def buscar_segun_dni_cliente(dni):

        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM listadoClientes WHERE dnicliente = :dnidri")
            query.bindValue(':dnidri', str(dni))
            if query.exec():
                while query.next():
                    for i in range(8):
                        registro.append(str(query.value(i)))

            if registro[7] != '':
                var.ui.rbtAlta.isChecked()
            return registro

        except Exception as error:
            print("Error al buscar segun dni: ", error)

    def borrarDriver(dni):
        try:

            fecha = datetime.now()
            fecha = fecha.strftime("%d/%m/%Y")
            valor = None
            query = QtSql.QSqlQuery()
            query.prepare('SELECT bajadri FROM drivers WHERE dnidri = :dni ')
            query.bindValue(':dni', dni)
            if query.exec():
                while query.next():
                    valor = query.value(0)

            if valor == "":
                fecha = datetime.now()
                fecha = fecha.strftime("%d/%m/%Y")
                queryFecha = QtSql.QSqlQuery()
                queryFecha.prepare('update drivers set bajadri = :fechabaja, altadri = :altadri where dnidri = :dni')
                queryFecha.bindValue(':dni', str(dni))
                queryFecha.bindValue(':fechabaja', str(fecha))
                queryFecha.bindValue(':altadri', '')
                if queryFecha.exec():

                    Ventanas.Ventanas.ventana_info("Se ha dado de baja al conductor")

                else:
                    Ventanas.Ventanas.mensaje_warning("No se ha podido dar de baja el conductor")
            else:
                Ventanas.Ventanas.mensaje_warning("El empleado ya esta dado de baja")

        except Exception as error:
            print("No se ha podido dar de baja al conductor", error)

    def select_all_driver(self):

        try:
            # Inicializar una lista vacía para almacenar los resultados de la consulta
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM drivers order by apeldri")
            if query.exec():
                while query.next():
                    # Crear una lista 'row' que contiene los valores de cada columna en el resultado actual
                    row = [query.value(i) for i in range(query.record().count())]
                    registro.append(row)
            return registro

        except Exception as error:
            print("Error al buscar segun dni: ", error)

    @staticmethod
    def guardarCliente(nuevoCliente):
        try:
            query = QtSql.QSqlQuery()
            query2 = QtSql.QSqlQuery()
            query2.prepare("select * from listadoClientes  where dnicliente = :dni")
            query2.bindValue(':dni', nuevoCliente[0])

            if query2.exec() and query2.next() and nuevoCliente[6] != '':
                query.prepare('update listadoClientes set bajaCliente = :bajaCliente where dnicliente = :dni')
                query.bindValue(':dni', str(nuevoCliente[0]))
                query.bindValue(':bajaCliente', '')
            else:
                query.prepare(
                    'insert into listadoClientes (dnicliente, razon, direccion, telefono, provCliente, muniCliente, '
                    'bajaCliente ) VALUES (:dni, :razon, :direccion, :telefono, :provincia, :municipio, :bajaCliente)')
                query.bindValue(':dni', str(nuevoCliente[0]))
                query.bindValue(':razon', str(nuevoCliente[1]))
                query.bindValue(':direccion', str(nuevoCliente[2]))
                query.bindValue(':telefono', str(nuevoCliente[3]))
                query.bindValue(':provincia', str(nuevoCliente[4]))
                query.bindValue(':municipio', str(nuevoCliente[5]))
                query.bindValue(':bajaCliente', str(nuevoCliente[6]))

            if query.exec():
                return True

            else:
                print("Error al ejecutar la consulta:", query.lastError().text())
                return False
            # select de los datos de los conductores de la base de datos

        except Exception as error:
            print("Error al guardar el conductor", error)

    def dni_existe(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("select * from listadoClientes where dnicliente= :dni")
            query.bindValue(":dni", dni)

            if query.exec() and query.next():
                print('El DNI se encuentra en la base de datos, devuelve True')
                return True
            else:
                # El DNI no se encuentra en la base de datos, devuelve False
                return False

        except Exception as error:
            print("Error en el método de validar si DNI existe:", error)

    def dni_existe_no_esta_baja(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM listadoClientes WHERE dnicliente = :dni AND bajacliente IS ''")
            query.bindValue(":dni", dni)

            if query.exec() and query.next():
                # el dni exite en la base de datos y no esta de baja
                return True
            else:
                # El DNI no se encuentra en la base de datos, devuelve False
                return False

        except Exception as error:
            print("Error en el método de validar si DNI existe y el cliente no esta dado de baja", error)

        ### ZONA FACTURACION ###

    def cargar_facturas(self=None):

        try:
            registros_facturas = []
            query = QtSql.QSqlQuery()
            query.prepare('select  numFactura,dniCliente from facturas')
            if query.exec():
                while query.next():
                    row = row = [query.value(i) for i in range(query.record().count())]
                    registros_facturas.append(row)
                    facturacion.Facturacion.cargartabla(registros_facturas)

        except Exception as error:
            print("Error al cargar facturas", query.lastError())

    def provincia_segun_municipio(nombre_municipio):
        try:
            id_provincia = None
            nombre_provincia = None
            query_obtener_id_provincia = QtSql.QSqlQuery()
            query_obtener_nombre_provincia = QtSql.QSqlQuery()
            query_obtener_id_provincia.prepare('SELECT idprov from municipios where municipio = :municipio')
            query_obtener_id_provincia.bindValue(':municipio', nombre_municipio)
            if query_obtener_id_provincia.exec():
                while query_obtener_id_provincia.next():
                    id_provincia = query_obtener_id_provincia.value(0)
            query_obtener_nombre_provincia.prepare('SELECT provincia from provincias where idprov = :idprov')
            query_obtener_nombre_provincia.bindValue(':idprov', id_provincia)
            if query_obtener_nombre_provincia.exec():
                while query_obtener_nombre_provincia.next():
                    nombre_provincia = query_obtener_nombre_provincia.value(0)
            return nombre_provincia

        except Exception as error:
            print("Error al obtener una provincia segun el municipio")
