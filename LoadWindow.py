import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget


class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("MyWindow.ui", self)

app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())
