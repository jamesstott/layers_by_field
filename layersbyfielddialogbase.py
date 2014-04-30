# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layersbyfielddialogbase.ui'
#
# Created: Fri Mar 28 11:23:31 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_LayersByFieldDialog(object):
    def setupUi(self, LayersByFieldDialog):
        LayersByFieldDialog.setObjectName(_fromUtf8("LayersByFieldDialog"))
        LayersByFieldDialog.resize(307, 232)
        LayersByFieldDialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.verticalLayout = QtGui.QVBoxLayout(LayersByFieldDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(LayersByFieldDialog)
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.inputLayerCombo = QtGui.QComboBox(LayersByFieldDialog)
        self.inputLayerCombo.setObjectName(_fromUtf8("inputLayerCombo"))
        self.verticalLayout.addWidget(self.inputLayerCombo)
        self.label_2 = QtGui.QLabel(LayersByFieldDialog)
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.splitFieldCombo = QtGui.QComboBox(LayersByFieldDialog)
        self.splitFieldCombo.setObjectName(_fromUtf8("splitFieldCombo"))
        self.verticalLayout.addWidget(self.splitFieldCombo)
        self.label_3 = QtGui.QLabel(LayersByFieldDialog)
        self.label_3.setEnabled(False)
        self.label_3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_3.setVisible(False)
        self.verticalLayout.addWidget(self.label_3)
        self.progressBar = QtGui.QProgressBar(LayersByFieldDialog)
        self.progressBar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.progressBar.setProperty(_fromUtf8("value"), 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.buttonBox = QtGui.QDialogButtonBox(LayersByFieldDialog)
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(LayersByFieldDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), LayersByFieldDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), LayersByFieldDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LayersByFieldDialog)

    def retranslateUi(self, LayersByFieldDialog):
        LayersByFieldDialog.setWindowTitle(QtGui.QApplication.translate("LayersByFieldDialog", "Layers from field", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("LayersByFieldDialog", "Input layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("LayersByFieldDialog", "Split by field", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("LayersByFieldDialog", "Save to", None, QtGui.QApplication.UnicodeUTF8))

