import sys

from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Button & Label")
        self.setWindowIcon(QIcon("qt.png"))

        self.setGeometry(500, 200, 500, 400)
        self.create_widgets()

    def create_widgets(self):
        btn = QPushButton("Click Me", self)
        # btn.move(100, 100)
        btn.setGeometry(100, 100, 100, 100)
        btn.setStyleSheet("background-color:red")
        btn.setIcon(QIcon("football.png"))

        label = QLabel("My Label", self)
        label.move(100, 200)
        label.setStyleSheet("color:green")
        label.setFont(QFont("Times New Roman", 15))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
