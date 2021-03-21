from PyQt5 import QtCore, QtGui, QtWidgets


class Vehicle(object):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class InputWidget(QtGui.QWidget):
    def __init__(self):
        super(InputWidget, self).__init__()
        self.setFixedSize(240, 300)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.save_pushButton.clicked.connect(self.save)
        self.ui.cancel_pushButton.clicked.connect(self.cancel)

    def save(self):
        self.vehicle = Vehicle(params)

    def cancel(self):
        self.vehicle = None

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 20, 193, 103))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.brand_label = QtGui.QLabel(self.layoutWidget)
        self.brand_label.setObjectName(_fromUtf8("brand_label"))
        self.gridLayout.addWidget(self.brand_label, 0, 0, 1, 1)
        self.model_lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.model_lineEdit.setObjectName(_fromUtf8("model_lineEdit"))
        self.gridLayout.addWidget(self.model_lineEdit, 1, 3, 1, 1)
        self.brand_lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.brand_lineEdit.setObjectName(_fromUtf8("brand_lineEdit"))
        self.gridLayout.addWidget(self.brand_lineEdit, 0, 3, 1, 1)
        self.model_label = QtGui.QLabel(self.layoutWidget)
        self.model_label.setObjectName(_fromUtf8("model_label"))
        self.gridLayout.addWidget(self.model_label, 1, 0, 1, 1)
        self.year_label = QtGui.QLabel(self.layoutWidget)
        self.year_label.setObjectName(_fromUtf8("year_label"))
        self.gridLayout.addWidget(self.year_label, 2, 0, 1, 1)
        self.cancel_pushButton = QtGui.QPushButton(self.layoutWidget)
        self.cancel_pushButton.setObjectName(_fromUtf8("cancel_pushButton"))
        self.gridLayout.addWidget(self.cancel_pushButton, 3, 3, 1, 1)
        self.year_lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.year_lineEdit.setObjectName(_fromUtf8("year_lineEdit"))
        self.gridLayout.addWidget(self.year_lineEdit, 2, 3, 1, 1)
        self.save_pushButton = QtGui.QPushButton(self.layoutWidget)
        self.save_pushButton.setObjectName(_fromUtf8("save_pushButton"))
        self.gridLayout.addWidget(self.save_pushButton, 3, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(Form)