from PyQt5 import QtWidgets
from Projeler.Hesap_Makinesi.arayuz import Ui_MainWindow

class hm_arayuz(QtWidgets.QMainWindow,Ui_MainWindow):
    ilksayi = None
    ikincisayi = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        #rakamlar
        self.sayi_0.clicked.connect(self.f_rakambasma)
        self.sayi_1.clicked.connect(self.f_rakambasma)
        self.sayi_2.clicked.connect(self.f_rakambasma)
        self.sayi_3.clicked.connect(self.f_rakambasma)
        self.sayi_4.clicked.connect(self.f_rakambasma)
        self.sayi_5.clicked.connect(self.f_rakambasma)
        self.sayi_6.clicked.connect(self.f_rakambasma)
        self.sayi_7.clicked.connect(self.f_rakambasma)
        self.sayi_8.clicked.connect(self.f_rakambasma)
        self.sayi_9.clicked.connect(self.f_rakambasma)

        self.nokta_button.clicked.connect(self.f_ondalik)
        self.arti_eksi_button.clicked.connect(self.f_isaret)
        self.yuzde_button.clicked.connect(self.f_yuzde)

        self.arti_button.clicked.connect(self.f_aritmetik)
        self.eksi_button.clicked.connect(self.f_aritmetik)
        self.bolu_button.clicked.connect(self.f_aritmetik)
        self.carpi_button.clicked.connect(self.f_aritmetik)

        self.arti_button.setCheckable(True)
        self.eksi_button.setCheckable(True)
        self.bolu_button.setCheckable(True)
        self.carpi_button.setCheckable(True)

        self.esittir_button.clicked.connect(self.f_sonuc)
        self.esittir_button.setCheckable(True)
        self.c_button.clicked.connect(self.f_temizle)

    def f_rakambasma(self):
        buton = self.sender()
        if ((self.arti_button.isChecked() or self.eksi_button.isChecked() or self.bolu_button.isChecked() or self.carpi_button.isChecked())and (not  self.ikincisayi)):
            self.label.setText(format(float(buton.text()),'.15g'))#.15g yuvarlama işlemi yaptırır 0 ı sildirmiş oluruz
            self.ikincisayi = True
        elif((self.ikincisayi)and (self.esittir_button.isChecked())):
            self.label.setText((format(float(buton.text()),".15g")))
            self.ikincisayi = True
            self.esittir_button.setChecked(False)
        else:
            if (("."in self.label.text())) and (buton.text() == "0"):
                self.label.setText(format(float(self.label.text() + buton.text()), '.15'))
            else:
                self.label.setText(format(float(self.label.text() + buton.text()), '.15g'))

    def f_ondalik(self):
        self.label.setText(self.label.text()+".")
        #koşullu durumu yazıp birden çok kez aynı işlemde nokta kullanılmasının engelle

    def f_isaret(self):
        buton = self.sender()
        deger = float(self.label.text())
        deger = deger*-1
        self.label.setText(format(deger,".15g"))

    def f_yuzde(self):
        deger = float(self.label.text())
        deger = deger *0.01
        self.label.setText(format(deger, ".15g"))

    def f_aritmetik(self):
        buton = self.sender()
        self.ilksayi = float(self.label.text())
        buton.setChecked(True)

    def f_sonuc(self):
        ikincideger = float(self.label.text())

        if self.arti_button.isChecked() :
            yenideger = self.ilksayi + ikincideger
            self.label.setText(format(yenideger,".15g"))
            self.arti_button.setChecked(False)

        elif self.eksi_button.isChecked() :
            yenideger = self.ilksayi - ikincideger
            self.label.setText(format(yenideger,".15g"))
            self.arti_button.setChecked(False)

        elif self.bolu_button.isChecked() :
            yenideger = self.ilksayi / ikincideger
            self.label.setText(format(yenideger,".15g"))
            self.arti_button.setChecked(False)

        elif self.carpi_button.isChecked() :
            yenideger = self.ilksayi * ikincideger
            self.label.setText(format(yenideger,".15g"))
            self.arti_button.setChecked(False)

        self.ilksayi = yenideger

    def f_temizle(self):
        self.ilksayi = 0
        self.ikincisayi =False
        self.label.setText("0")
        self.esittir_button.setChecked(False)
        self.bolu_button.setChecked(False)
        self.eksi_button.setChecked(False)
        self.arti_button.setChecked(False)
        self.carpi_button.setChecked(False)