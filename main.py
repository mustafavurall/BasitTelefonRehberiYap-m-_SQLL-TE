#ana çatı

from PyQt6.QtWidgets import QApplication
from _form import FormWindow


uygulama=QApplication([])
pencere = FormWindow()
pencere.show()
uygulama.exec()