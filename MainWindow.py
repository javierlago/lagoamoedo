# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnSalir = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnSalir.setGeometry(QtCore.QRect(310, 330, 120, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSalir.sizePolicy().hasHeightForWidth())
        self.btnSalir.setSizePolicy(sizePolicy)
        self.btnSalir.setMinimumSize(QtCore.QSize(120, 20))
        self.btnSalir.setMaximumSize(QtCore.QSize(116, 20))
        font = QtGui.QFont()
        font.setFamily("ProFont IIx Nerd Font Mono")
        font.setPointSize(10)
        self.btnSalir.setFont(font)
        self.btnSalir.setMouseTracking(False)
        self.btnSalir.setAutoFillBackground(False)
        self.btnSalir.setObjectName("btnSalir")
        self.lblTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(260, 280, 231, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTitle.sizePolicy().hasHeightForWidth())
        self.lblTitle.setSizePolicy(sizePolicy)
        self.lblTitle.setMinimumSize(QtCore.QSize(120, 20))
        self.lblTitle.setMaximumSize(QtCore.QSize(240, 40))
        self.lblTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(parent=self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtGui.QAction(parent=MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionAcerca_de = QtGui.QAction(parent=MainWindow)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.menuArchivo.addAction(self.actionSalir)
        self.menuHelp.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CarTeis"))
        self.btnSalir.setText(_translate("MainWindow", "Salir"))
        self.lblTitle.setText(_translate("MainWindow", "CarTeis"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de .."))
