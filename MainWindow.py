# Form implementation generated from reading ui file '.\templates\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MainWindow.resize(1215, 507)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1215, 507))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\templates\\../img/taxiIcon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"    background-color: rgb(186, 186, 186);\n"
"\n"
"}")
        MainWindow.setIconSize(QtCore.QSize(35, 35))
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayout.setContentsMargins(9, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.gridFrame = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridFrame.sizePolicy().hasHeightForWidth())
        self.gridFrame.setSizePolicy(sizePolicy)
        self.gridFrame.setObjectName("gridFrame")
        self._2 = QtWidgets.QGridLayout(self.gridFrame)
        self._2.setContentsMargins(0, 0, 0, 0)
        self._2.setSpacing(0)
        self._2.setObjectName("_2")
        self.PanPrincipal = QtWidgets.QTabWidget(parent=self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PanPrincipal.sizePolicy().hasHeightForWidth())
        self.PanPrincipal.setSizePolicy(sizePolicy)
        self.PanPrincipal.setMinimumSize(QtCore.QSize(0, 0))
        self.PanPrincipal.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.PanPrincipal.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.PanPrincipal.setObjectName("PanPrincipal")
        self.tabDrivers = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabDrivers.sizePolicy().hasHeightForWidth())
        self.tabDrivers.setSizePolicy(sizePolicy)
        self.tabDrivers.setMinimumSize(QtCore.QSize(974, 0))
        self.tabDrivers.setObjectName("tabDrivers")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabDrivers)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabDriver2 = QtWidgets.QTableWidget(parent=self.tabDrivers)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabDriver2.sizePolicy().hasHeightForWidth())
        self.tabDriver2.setSizePolicy(sizePolicy)
        self.tabDriver2.setStyleSheet("")
        self.tabDriver2.setAlternatingRowColors(True)
        self.tabDriver2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabDriver2.setObjectName("tabDriver2")
        self.tabDriver2.setColumnCount(6)
        self.tabDriver2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabDriver2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDriver2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDriver2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDriver2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDriver2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDriver2.setHorizontalHeaderItem(5, item)
        self.tabDriver2.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.tabDriver2, 3, 0, 1, 1)
        self.boxInfo = QtWidgets.QFrame(parent=self.tabDrivers)
        self.boxInfo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boxInfo.sizePolicy().hasHeightForWidth())
        self.boxInfo.setSizePolicy(sizePolicy)
        self.boxInfo.setMinimumSize(QtCore.QSize(0, 0))
        self.boxInfo.setAutoFillBackground(False)
        self.boxInfo.setStyleSheet("QWidget#boxInfo{\n"
"border-radius:10px;\n"
"border: 2px solid black;\n"
"}")
        self.boxInfo.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.boxInfo.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.boxInfo.setLineWidth(5)
        self.boxInfo.setObjectName("boxInfo")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.boxInfo)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lblCodigo = QtWidgets.QLabel(parent=self.boxInfo)
        self.lblCodigo.setStyleSheet("")
        self.lblCodigo.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblCodigo.setObjectName("lblCodigo")
        self.gridLayout_3.addWidget(self.lblCodigo, 0, 0, 1, 1)
        self.lblCodDB = QtWidgets.QLabel(parent=self.boxInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCodDB.sizePolicy().hasHeightForWidth())
        self.lblCodDB.setSizePolicy(sizePolicy)
        self.lblCodDB.setMinimumSize(QtCore.QSize(80, 24))
        self.lblCodDB.setMaximumSize(QtCore.QSize(80, 24))
        self.lblCodDB.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.lblCodDB.setText("")
        self.lblCodDB.setObjectName("lblCodDB")
        self.gridLayout_3.addWidget(self.lblCodDB, 0, 1, 1, 1)
        self.lblDNI = QtWidgets.QLabel(parent=self.boxInfo)
        self.lblDNI.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblDNI.setObjectName("lblDNI")
        self.gridLayout_3.addWidget(self.lblDNI, 0, 3, 1, 1)
        self.txtDni = QtWidgets.QLineEdit(parent=self.boxInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtDni.sizePolicy().hasHeightForWidth())
        self.txtDni.setSizePolicy(sizePolicy)
        self.txtDni.setMaxLength(9)
        self.txtDni.setObjectName("txtDni")
        self.gridLayout_3.addWidget(self.txtDni, 0, 4, 1, 2)
        self.lblCheckDNI = QtWidgets.QLabel(parent=self.boxInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCheckDNI.sizePolicy().hasHeightForWidth())
        self.lblCheckDNI.setSizePolicy(sizePolicy)
        self.lblCheckDNI.setMinimumSize(QtCore.QSize(24, 24))
        self.lblCheckDNI.setMaximumSize(QtCore.QSize(24, 24))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lblCheckDNI.setFont(font)
        self.lblCheckDNI.setText("")
        self.lblCheckDNI.setScaledContents(False)
        self.lblCheckDNI.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblCheckDNI.setObjectName("lblCheckDNI")
        self.gridLayout_3.addWidget(self.lblCheckDNI, 0, 6, 1, 1)
        self.tltDate = QtWidgets.QLabel(parent=self.boxInfo)
        self.tltDate.setStyleSheet("")
        self.tltDate.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tltDate.setObjectName("tltDate")
        self.gridLayout_3.addWidget(self.tltDate, 0, 12, 1, 2)
        self.txtDate = QtWidgets.QLineEdit(parent=self.boxInfo)
        self.txtDate.setObjectName("txtDate")
        self.gridLayout_3.addWidget(self.txtDate, 0, 14, 1, 1)
        self.btnCalendar = QtWidgets.QPushButton(parent=self.boxInfo)
        self.btnCalendar.setStyleSheet("border-radius:2px;\n"
"")
        self.btnCalendar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\templates\\../img/calendario.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCalendar.setIcon(icon1)
        self.btnCalendar.setIconSize(QtCore.QSize(24, 24))
        self.btnCalendar.setObjectName("btnCalendar")
        self.gridLayout_3.addWidget(self.btnCalendar, 0, 15, 1, 1)
        self.lblSurname = QtWidgets.QLabel(parent=self.boxInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSurname.sizePolicy().hasHeightForWidth())
        self.lblSurname.setSizePolicy(sizePolicy)
        self.lblSurname.setStyleSheet("")
        self.lblSurname.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblSurname.setObjectName("lblSurname")
        self.gridLayout_3.addWidget(self.lblSurname, 1, 0, 1, 1)
        self.txtDni_2 = QtWidgets.QLineEdit(parent=self.boxInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtDni_2.sizePolicy().hasHeightForWidth())
        self.txtDni_2.setSizePolicy(sizePolicy)
        self.txtDni_2.setObjectName("txtDni_2")
        self.gridLayout_3.addWidget(self.txtDni_2, 1, 1, 1, 2)
        self.lblName = QtWidgets.QLabel(parent=self.boxInfo)
        self.lblName.setStyleSheet("")
        self.lblName.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblName.setObjectName("lblName")
        self.gridLayout_3.addWidget(self.lblName, 1, 7, 1, 1)
        self.txtNombre = QtWidgets.QLineEdit(parent=self.boxInfo)
        self.txtNombre.setObjectName("txtNombre")
        self.gridLayout_3.addWidget(self.txtNombre, 1, 9, 1, 3)
        self.lblStreet = QtWidgets.QLabel(parent=self.boxInfo)
        self.lblStreet.setStyleSheet("")
        self.lblStreet.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lblStreet.setObjectName("lblStreet")
        self.gridLayout_3.addWidget(self.lblStreet, 2, 0, 1, 1)
        self.txtDireccion = QtWidgets.QLineEdit(parent=self.boxInfo)
        self.txtDireccion.setMinimumSize(QtCore.QSize(250, 20))
        self.txtDireccion.setMaximumSize(QtCore.QSize(250, 20))
        self.txtDireccion.setObjectName("txtDireccion")
        self.gridLayout_3.addWidget(self.txtDireccion, 2, 1, 1, 5)
        self.lblProvincia = QtWidgets.QLabel(parent=self.boxInfo)
        self.lblProvincia.setStyleSheet("")
        self.lblProvincia.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lblProvincia.setObjectName("lblProvincia")
        self.gridLayout_3.addWidget(self.lblProvincia, 2, 7, 1, 1)
        self.cmbProvincia = QtWidgets.QComboBox(parent=self.boxInfo)
        self.cmbProvincia.setObjectName("cmbProvincia")
        self.gridLayout_3.addWidget(self.cmbProvincia, 2, 10, 1, 2)
        self.lblLocalidad = QtWidgets.QLabel(parent=self.boxInfo)
        self.lblLocalidad.setStyleSheet("")
        self.lblLocalidad.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lblLocalidad.setObjectName("lblLocalidad")
        self.gridLayout_3.addWidget(self.lblLocalidad, 2, 12, 1, 1)
        self.cmbLocalidad = QtWidgets.QComboBox(parent=self.boxInfo)
        self.cmbLocalidad.setObjectName("cmbLocalidad")
        self.gridLayout_3.addWidget(self.cmbLocalidad, 2, 13, 1, 2)
        self.rbtTodos = QtWidgets.QRadioButton(parent=self.boxInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbtTodos.sizePolicy().hasHeightForWidth())
        self.rbtTodos.setSizePolicy(sizePolicy)
        self.rbtTodos.setChecked(True)
        self.rbtTodos.setObjectName("rbtTodos")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rbtTodos)
        self.gridLayout_3.addWidget(self.rbtTodos, 3, 8, 1, 2)
        self.rbtAlta = QtWidgets.QRadioButton(parent=self.boxInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbtAlta.sizePolicy().hasHeightForWidth())
        self.rbtAlta.setSizePolicy(sizePolicy)
        self.rbtAlta.setObjectName("rbtAlta")
        self.buttonGroup.addButton(self.rbtAlta)
        self.gridLayout_3.addWidget(self.rbtAlta, 3, 10, 2, 1)
        self.rbtBaja = QtWidgets.QRadioButton(parent=self.boxInfo)
        self.rbtBaja.setChecked(False)
        self.rbtBaja.setObjectName("rbtBaja")
        self.buttonGroup.addButton(self.rbtBaja)
        self.gridLayout_3.addWidget(self.rbtBaja, 3, 11, 2, 1)
        self.lblMovil = QtWidgets.QLabel(parent=self.boxInfo)
        self.lblMovil.setStyleSheet("")
        self.lblMovil.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lblMovil.setObjectName("lblMovil")
        self.gridLayout_3.addWidget(self.lblMovil, 4, 0, 1, 1)
        self.txtMovil = QtWidgets.QLineEdit(parent=self.boxInfo)
        self.txtMovil.setObjectName("txtMovil")
        self.gridLayout_3.addWidget(self.txtMovil, 4, 1, 2, 2)
        self.lblSalario = QtWidgets.QLabel(parent=self.boxInfo)
        self.lblSalario.setStyleSheet("")
        self.lblSalario.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblSalario.setObjectName("lblSalario")
        self.gridLayout_3.addWidget(self.lblSalario, 4, 3, 1, 1)
        self.txtSalario = QtWidgets.QLineEdit(parent=self.boxInfo)
        self.txtSalario.setText("")
        self.txtSalario.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.txtSalario.setObjectName("txtSalario")
        self.gridLayout_3.addWidget(self.txtSalario, 4, 4, 2, 2)
        self.lblTxt = QtWidgets.QLabel(parent=self.boxInfo)
        self.lblTxt.setText("")
        self.lblTxt.setPixmap(QtGui.QPixmap(".\\templates\\img/euro.png"))
        self.lblTxt.setScaledContents(True)
        self.lblTxt.setObjectName("lblTxt")
        self.gridLayout_3.addWidget(self.lblTxt, 4, 6, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.boxInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setMaximumSize(QtCore.QSize(50, 24))
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 4, 7, 1, 2)
        self.lblCarnet = QtWidgets.QLabel(parent=self.boxInfo)
        self.lblCarnet.setObjectName("lblCarnet")
        self.gridLayout_3.addWidget(self.lblCarnet, 6, 0, 1, 1)
        self.chkA = QtWidgets.QCheckBox(parent=self.boxInfo)
        self.chkA.setChecked(True)
        self.chkA.setObjectName("chkA")
        self.gridLayout_3.addWidget(self.chkA, 6, 1, 1, 1)
        self.chkB = QtWidgets.QCheckBox(parent=self.boxInfo)
        self.chkB.setObjectName("chkB")
        self.gridLayout_3.addWidget(self.chkB, 6, 2, 1, 1)
        self.chkC = QtWidgets.QCheckBox(parent=self.boxInfo)
        self.chkC.setObjectName("chkC")
        self.gridLayout_3.addWidget(self.chkC, 6, 3, 1, 1)
        self.chkD = QtWidgets.QCheckBox(parent=self.boxInfo)
        self.chkD.setObjectName("chkD")
        self.gridLayout_3.addWidget(self.chkD, 6, 4, 1, 1)
        self.btnaltaDriver = QtWidgets.QPushButton(parent=self.boxInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnaltaDriver.sizePolicy().hasHeightForWidth())
        self.btnaltaDriver.setSizePolicy(sizePolicy)
        self.btnaltaDriver.setMinimumSize(QtCore.QSize(150, 24))
        self.btnaltaDriver.setMaximumSize(QtCore.QSize(150, 24))
        self.btnaltaDriver.setObjectName("btnaltaDriver")
        self.gridLayout_3.addWidget(self.btnaltaDriver, 7, 5, 1, 2)
        self.btnBajaDriver = QtWidgets.QPushButton(parent=self.boxInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBajaDriver.sizePolicy().hasHeightForWidth())
        self.btnBajaDriver.setSizePolicy(sizePolicy)
        self.btnBajaDriver.setMinimumSize(QtCore.QSize(150, 24))
        self.btnBajaDriver.setMaximumSize(QtCore.QSize(150, 24))
        self.btnBajaDriver.setObjectName("btnBajaDriver")
        self.gridLayout_3.addWidget(self.btnBajaDriver, 7, 7, 1, 4)
        self.btnModifDriver = QtWidgets.QPushButton(parent=self.boxInfo)
        self.btnModifDriver.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnModifDriver.sizePolicy().hasHeightForWidth())
        self.btnModifDriver.setSizePolicy(sizePolicy)
        self.btnModifDriver.setMinimumSize(QtCore.QSize(150, 24))
        self.btnModifDriver.setMaximumSize(QtCore.QSize(150, 24))
        self.btnModifDriver.setAutoFillBackground(False)
        self.btnModifDriver.setObjectName("btnModifDriver")
        self.gridLayout_3.addWidget(self.btnModifDriver, 7, 11, 1, 1)
        self.gridLayout_2.addWidget(self.boxInfo, 2, 0, 1, 1)
        self.PanPrincipal.addTab(self.tabDrivers, "")
        self.tabCars = QtWidgets.QWidget()
        self.tabCars.setObjectName("tabCars")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tabCars)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.PanPrincipal.addTab(self.tabCars, "")
        self._2.addWidget(self.PanPrincipal, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.gridFrame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1215, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(parent=self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMaximumSize(QtCore.QSize(1920, 1080))
        self.toolBar.setIconSize(QtCore.QSize(24, 24))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionAcerca_de = QtGui.QAction(parent=MainWindow)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.Salir = QtGui.QAction(parent=MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\templates\\../img/salir.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Salir.setIcon(icon2)
        self.Salir.setObjectName("Salir")
        self.btnLimpiar = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\templates\\../img/pincel.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnLimpiar.setIcon(icon3)
        self.btnLimpiar.setText("")
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.actionSalir = QtGui.QAction(parent=MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menuHelp.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.Salir)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.btnLimpiar)

        self.retranslateUi(MainWindow)
        self.PanPrincipal.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btnCalendar, self.txtDni_2)
        MainWindow.setTabOrder(self.txtDni_2, self.txtNombre)
        MainWindow.setTabOrder(self.txtNombre, self.cmbProvincia)
        MainWindow.setTabOrder(self.cmbProvincia, self.txtDireccion)
        MainWindow.setTabOrder(self.txtDireccion, self.cmbLocalidad)
        MainWindow.setTabOrder(self.cmbLocalidad, self.txtMovil)
        MainWindow.setTabOrder(self.txtMovil, self.txtSalario)
        MainWindow.setTabOrder(self.txtSalario, self.txtDni)
        MainWindow.setTabOrder(self.txtDni, self.txtDate)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CarTeis"))
        item = self.tabDriver2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Codigo"))
        item = self.tabDriver2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Apellidos"))
        item = self.tabDriver2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tabDriver2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Móvil"))
        item = self.tabDriver2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Licencias"))
        item = self.tabDriver2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Fecha Baja"))
        self.lblCodigo.setText(_translate("MainWindow", "Codigo:"))
        self.lblDNI.setText(_translate("MainWindow", "DNI:"))
        self.tltDate.setText(_translate("MainWindow", "<html><head/><body><p>Fecha de Alta:</p></body></html>"))
        self.lblSurname.setText(_translate("MainWindow", "Apellidos"))
        self.lblName.setText(_translate("MainWindow", "<html><head/><body><p>Nombre</p></body></html>"))
        self.lblStreet.setText(_translate("MainWindow", "Direccion"))
        self.lblProvincia.setText(_translate("MainWindow", "Provincia"))
        self.lblLocalidad.setText(_translate("MainWindow", "Localidad"))
        self.rbtTodos.setText(_translate("MainWindow", "Todos"))
        self.rbtAlta.setText(_translate("MainWindow", "Alta"))
        self.rbtBaja.setText(_translate("MainWindow", "Baja"))
        self.lblMovil.setText(_translate("MainWindow", "Movil:"))
        self.lblSalario.setText(_translate("MainWindow", "Salario"))
        self.label.setText(_translate("MainWindow", "Estado:"))
        self.lblCarnet.setText(_translate("MainWindow", "Tipo de carnet"))
        self.chkA.setText(_translate("MainWindow", "A"))
        self.chkB.setText(_translate("MainWindow", "B"))
        self.chkC.setText(_translate("MainWindow", "C"))
        self.chkD.setText(_translate("MainWindow", "D"))
        self.btnaltaDriver.setText(_translate("MainWindow", "Alta"))
        self.btnBajaDriver.setText(_translate("MainWindow", "Baja"))
        self.btnModifDriver.setText(_translate("MainWindow", "Modificar"))
        self.PanPrincipal.setTabText(self.PanPrincipal.indexOf(self.tabDrivers), _translate("MainWindow", "Conductores"))
        self.PanPrincipal.setTabText(self.PanPrincipal.indexOf(self.tabCars), _translate("MainWindow", "Taxis"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuHelp.setTitle(_translate("MainWindow", "Ayuda"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de..."))
        self.Salir.setText(_translate("MainWindow", "salir"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
