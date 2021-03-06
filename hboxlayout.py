import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Layouts")
        self.setWindowIcon(QIcon("qt.png"))
        self.setGeometry(500, 200, 500, 400)

        hbox = QHBoxLayout()

        btn1 = QPushButton("Button One")
        btn2 = QPushButton("Button Two")
        btn3 = QPushButton("Button Three")
        btn4 = QPushButton("Button Four")

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)

        self.setLayout(hbox)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
