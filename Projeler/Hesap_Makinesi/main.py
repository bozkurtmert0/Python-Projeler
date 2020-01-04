import sys
from PyQt5.QtWidgets import QApplication
from Projeler.Hesap_Makinesi.hesapmakinesi import hm_arayuz

uygulama = QApplication(sys.argv)

hesapmakinesi = hm_arayuz()
sys.exit(uygulama.exec_())

