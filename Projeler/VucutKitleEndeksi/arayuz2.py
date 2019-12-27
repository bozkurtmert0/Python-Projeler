# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arayuz2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VKE(object):
    def setupUi(self, VKE):
        VKE.setObjectName("VKE")
        VKE.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(VKE)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 40, 191, 88))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.boyLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.boyLabel.setObjectName("boyLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.boyLabel)
        self.boybilgisi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.boybilgisi.setObjectName("boybilgisi")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.boybilgisi)
        self.kiloLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.kiloLabel.setObjectName("kiloLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.kiloLabel)
        self.kilobilgisi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.kilobilgisi.setObjectName("kilobilgisi")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.kilobilgisi)
        self.hesapla = QtWidgets.QPushButton(self.formLayoutWidget)
        self.hesapla.setObjectName("hesapla")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.hesapla)
        self.sonuc = QtWidgets.QLabel(VKE)
        self.sonuc.setGeometry(QtCore.QRect(210, 40, 181, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sonuc.setFont(font)
        self.sonuc.setObjectName("sonuc")
        self.durum = QtWidgets.QLabel(VKE)
        self.durum.setGeometry(QtCore.QRect(140, 130, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.durum.setFont(font)
        self.durum.setObjectName("durum")

        self.retranslateUi(VKE)
        QtCore.QMetaObject.connectSlotsByName(VKE)

    def retranslateUi(self, VKE):
        _translate = QtCore.QCoreApplication.translate
        VKE.setWindowTitle(_translate("VKE", "VücutKitleEndeksi"))
        self.boyLabel.setText(_translate("VKE", "Boy"))
        self.kiloLabel.setText(_translate("VKE", "Kilo"))
        self.hesapla.setText(_translate("VKE", "Hesapla"))
        self.sonuc.setText(_translate("VKE", "Sonuç Bölümü"))
        self.durum.setText(_translate("VKE", "Durum"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VKE = QtWidgets.QWidget()
    ui = Ui_VKE()
    ui.setupUi(VKE)
    VKE.show()
    sys.exit(app.exec_())

