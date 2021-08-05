import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Window")
        self.setWindowIcon(QIcon("qt.png"))
        # self.setFixedHeight(200)
        # self.setFixedWidth(200)

        self.setGeometry(500, 300, 400, 300)
        # self.setStyleSheet("background-color:red")

        stylesheet = "background-color:red"
        self.setStyleSheet(stylesheet)


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())
