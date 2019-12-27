from Projeler.VucutKitleEndeksi.arayuz2 import Ui_VKE as Arayuz_ui
import sys
from PyQt5 import QtWidgets

class Arayuz_main(QtWidgets.QWidget,Arayuz_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.hesapla.clicked.connect(self.hesap)

    def hesap(self):
        kilo = float(self.kilobilgisi.text())
        boy = float(self.boybilgisi.text())
        vke = kilo / (boy ** 2)
        self.sonuc.setText(str(vke.__round__(1)))

        if 0<=vke <=18.4:
            self.durum.setText("Zayıf...")

        elif 18.5<=vke <=24.9:
            self.durum.setText("Normal..")

        elif 25.0<=vke <=29.9:
            self.durum.setText("Fazla Kilolu...")

        else :
            self.durum.setText("Obezsiniz.........")


if __name__ == "__main__" :
    uygulama = QtWidgets.QApplication(sys.argv)
    ekran = Arayuz_main()
    ekran.show()
    sys.exit(uygulama.exec_())

