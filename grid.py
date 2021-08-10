import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Layouts")
        self.setWindowIcon(QIcon("qt.png"))
        self.setGeometry(500, 200, 500, 400)

        grid = QGridLayout()

        btn1 = QPushButton("Button One")
        btn2 = QPushButton("Button Two")
        btn3 = QPushButton("Button Three")
        btn4 = QPushButton("Button Four")
        btn5 = QPushButton("Button Five")
        btn6 = QPushButton("Button Six")
        btn7 = QPushButton("Button Seven")
        btn8 = QPushButton("Button Eight")

        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 0, 2)
        grid.addWidget(btn4, 0, 3)
        grid.addWidget(btn5, 1, 0)
        grid.addWidget(btn6, 1, 1)
        grid.addWidget(btn7, 1, 2)
        grid.addWidget(btn8, 1, 3)

        self.setLayout(grid)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
