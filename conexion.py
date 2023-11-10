from PyQt6 import QtWidgets, QtSql, QtCore
from PyQt6.QtGui import QIcon

import conexion
import drivers
import var


class Conexion:

    def conexion(self=None):

        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('bbdd.sqlite')
        if not db.open():
            print("Error de conexion")
            return False
        else:
            print("Base de datos conectada")
            return True

    def cargaProv(self=None):
        try:
            var.ui.cmbProvincia.clear()
            query = QtSql.QSqlQuery()
            query.prepare("select provincia from provincias")
            if query.exec():
                var.ui.cmbProvincia.addItem("")
                while query.next():
                    # print(str(query.value(0)))
                    var.ui.cmbProvincia.addItem(query.value(0))
        except Exception as error:
            print("Error en la carga del combo prov: ", error)

    def selMuni(self=None):
        try:
            var.ui.cmbLocalidad.clear()
            id = 0
            prov = var.ui.cmbProvincia.currentText()
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
                var.ui.cmbLocalidad.addItem('')
                while query1.next():
                    var.ui.cmbLocalidad.addItem(query1.value(0))

        except Exception as error:
            print("Error en la carga de municipios", error)

    @staticmethod
    def guardardri(newdriver):
        try:
            query = QtSql.QSqlQuery()
            for i in newdriver:
                if i.strip() == "":

                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle("Aviso")
                    mbox.setIcon((QtWidgets.QMessageBox.Icon.Warning))
                    mensaje = "Campos vacios"
                    mbox.setText(mensaje)
                    icon = QIcon('./img/taxiIcon.png')
                    mbox.setWindowIcon(icon)
                    mbox.exec()
                    break

                else:

                    query.prepare('insert into drivers(dnidri, altadri, apeldri, nombredri, direcciondri, provdri, '
                                  'munidri, movildri, salario, carnet ) VALUES (:dni, :alta, :apel, :nombre, :direccion, '
                                  ':provincia, :municipio, :movil, :salario, :carnet)')
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
                    if query.exec():
                        mbox = QtWidgets.QMessageBox()
                        mbox.setWindowTitle('Aviso')
                        mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                        mbox.setText('Empleado dado de alta')
                        icon = QIcon('./img/taxiIcon.png')
                        mbox.setWindowIcon(icon)
                        mbox.exec()
                        break
                    else:
                        mbox = QtWidgets.QMessageBox()
                        mbox.setWindowTitle('Aviso')
                        mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                        mbox.setText("El DNI ya se encuentra en la base de datos")
                        mbox.exec()
                        break
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
            #print(registros)

        except Exception as error:
            print("error al mostrar resultados", error)


    @staticmethod
    def oneDriver(codigo):
        print(codigo, "codigo que me devuelve")
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


    def buscar_segun_dni(dni):

        query = QtSql.QSqlQuery()
        query.prepare('select * from drivers where dnidri = :dni')
        query.bindValue(':dnidri', str(dni))
        if query.exec():
            while query.next():
                codigo = query.value(0)
        registro = conexion.Conexion.oneDriver(codigo)

        return registro


