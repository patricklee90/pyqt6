import sys

from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Signal and Slot")
        self.setWindowIcon(QIcon("qt.png"))

        self.setGeometry(500, 200, 500, 400)
        self.create_widgets()

    def create_widgets(self):
        btn = QPushButton("Click Me", self)
        # btn.move(100, 100)
        btn.setGeometry(100, 100, 100, 100)
        btn.setStyleSheet("background-color:red")
        btn.setIcon(QIcon("football.png"))
        btn.clicked.connect(self.clicked_btn)

        self.label = QLabel("My Label", self)
        # self.label.move(100, 200)
        self.label.setGeometry(100, 200, 200, 100)
        self.label.setStyleSheet("color:green")
        self.label.setFont(QFont("Times New Roman", 15))

    def clicked_btn(self):
        self.label.setText("Text is changed")
        self.label.setStyleSheet("background-color:red")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
