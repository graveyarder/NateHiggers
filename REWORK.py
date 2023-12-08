import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.pushButton = QPushButton("Draw Circle")
        self.layout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.drawCircle)

    def drawCircle(self):
        painter = QPainter(self)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Random color
        painter.setPen(color)
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        painter.drawEllipse(x, y, diameter, diameter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
