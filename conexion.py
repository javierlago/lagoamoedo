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
        '''
        Método para borrar un cliente de la base de datos según el DNI pasado por parametro.
        :param : Recibe un string con el DNI que se desea borrar.
        '''
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
        '''
        Modificacion de un cliente de la base de datos.Para realizar la modicicación se debera seleccionar un cliente de la tabla de clientes.Cuando se modifica el cliente se mostrara una ventana indicando que se ha realizado la modificación.Si no se ha modificado el cliente y se ejecuta el metodo se mostrara una ventana indicando que no se han realizado cambios en el cliente.

        '''
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
        '''
        Metodo que establece una conexión a la base de datos.
        :return: True en cado de que la conexion se realize.
        :rtype: Boolean
        '''
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
        '''
        Metodo que se le pasa por parametro un ComboBox y lo rellena con el resultado de la query realizada a la base de datos.
        :param : ComboBox que se desea rellenar
        :return:
        :rtype:
        '''
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
        '''
        Metodo que recibe dos comboBox y en funcio de del texto de el primer comboBox rellena el segundo comboBox en funcion del resultado obtenido en la primera query.
        :param comboBoxLocalidad:
        :param comboBoxProvincia:
        :type comboBoxLocalidad:
        :type comboBoxProvincia:

        '''
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
        '''
        Metodo que rellena un combobox de conductores en funcion del resultado de una query en la que se solicitan todos los conductores que estan dados de alta en la base de datos.Estes datos son formateados de una manera especifia para que solo se muestre el codigo y los apellido del conductor en el comboBox.
        '''
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
        '''
        Metodo para guardar o modificar un conductor en la base de datos.
        Recibe por parametro una lista con los datos del conductor a guardar o modificar.Antes de relizar la query se verifica si ese conductor existe en la base de datos para saber si se guarda o se modifica.

        :param newdriver:
        :type newdriver:
        :return: Devuelve true si se inserta o midifica  un conductor en la base de datos.
        :rtype: Boolean
        '''
        try:

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


        except Exception as error:
            print("Error al guardar el conductor", error)

    def modificar(driver):
        '''
        Metodo usado para modificar un conductor existente en la base de datos.Recibe por parametro una lista con los nuevos datos.
        Si se ejecuta el metodo y los datos no ha modificado respeto a lo existentes en la base de datos se mostrara un ventana informando de que no se han realizado cambios y en caso de que se realizen cambios tambiens se informa mediante una ventana al usuario.
        :param: Lista con los datos a modifacar.

        '''
        try:

            registro = conexion.Conexion.buscar_segun_codigo(driver[0])
            query = QtSql.QSqlQuery()

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
        '''
        Metodo que carga la tabla de conductores mostrando
        todos los conductoes existentes en la base de datos relizando una consulta
        '''
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
        '''
        Metodo que realiza una consulta a la base de datos y carga la tabla de clientes con los datos obtenidos de dicha consulta.
        :return:
        :rtype:
        '''
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
        """
        Metodo para buscar un driver en la tabla de driver a traves de un código
        :param : recibe un código para buscar en la tabla de drivers
        :return: Registro de el driver donde coincida con el codigo
        :rtype: Array de datos del driver.
        """
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
        '''
        Busca un cliente en la base de datos según su código.

        :param : codigo: Código del cliente a buscar (tipo String).
        :return: Lista con los registros encontrados para el cliente.
        :rtype: list
        '''

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
        '''
           Busca un conductor en la base de datos según su número de DNI.

           :param dni: Número de DNI del conductor a buscar (tipo String).
           :return: Lista con los registros encontrados para el conductor.
           :rtype: list
        '''

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
        '''
            Da de baja a un conductor en la base de datos según su número de DNI.

            :param dni: Número de DNI del conductor a dar de baja (tipo String).
            :return: None
            '''
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
        '''
           Realiza una consulta para obtener todos los registros de conductores en la base de datos.

           :return: Lista de listas que contiene los registros de conductores.
           :rtype: list
           '''
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
        '''
            Guarda un nuevo cliente en la base de datos o actualiza un cliente existente.

            :param nuevoCliente: Lista que contiene la información del nuevo cliente.
                                 [DNI, Razón social, Dirección, Teléfono, Provincia, Municipio, Estado de baja]
            :type nuevoCliente: list
            :return: True si la operación se realiza con éxito, False en caso contrario.
            :rtype: bool
            '''
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
        '''
            Verifica si un DNI existe en la base de datos de clientes.

            :param dni: Número de DNI a verificar (tipo String).
            :return: True si el DNI se encuentra en la base de datos, False en caso contrario.
            :rtype: bool
        '''
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
        '''
          Verifica si un DNI existe en la base de datos de clientes y el cliente no está dado de baja.

          :param dni: Número de DNI a verificar (tipo String).
          :return: True si el DNI existe y el cliente no está dado de baja, False en caso contrario.
          :rtype: bool
        '''
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
        '''
         Carga las facturas desde la base de datos y las muestra en una tabla.

         :param self: Puede ser un objeto de la clase que llama al método o None si es un método estático.
         :type self: object or None
         :return: None
         '''

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
        '''
        Obtiene el nombre de la provincia correspondiente a un municipio dado.

        :param nombre_municipio: Nombre del municipio para el cual se desea obtener la provincia.
        :type nombre_municipio: str
        :return: Nombre de la provincia correspondiente al municipio.
        :rtype: str or None
        '''

        try:
            nombre_provincia = None

            query_obtener_provincia = QtSql.QSqlQuery()
            query_obtener_provincia.prepare('SELECT p.provincia FROM provincias p '
                                            'INNER JOIN municipios m ON p.idprov = m.idprov '
                                            'WHERE m.municipio = :municipio')
            query_obtener_provincia.bindValue(':municipio', nombre_municipio)
            if query_obtener_provincia.exec():
                while query_obtener_provincia.next():
                    nombre_provincia = query_obtener_provincia.value(0)


            return nombre_provincia

        except Exception as error:

            print("Error al obtener una provincia según el municipio:", error)
