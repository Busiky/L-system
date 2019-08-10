import sys
from math import pi, sin, cos

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QInputDialog
from PyQt5.QtGui import QPainter, QColor, QPen


class Fract(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.WIDTH, self.HEIGHT = 1800, 800
        self.setGeometry(100, 100, self.WIDTH, self.HEIGHT)
        self.setWindowTitle('L-system')
        self.x, self.y = 0, self.HEIGHT // 2
        self.line = 40
        self.angle = 0

        with open('lsystem.txt', 'r', encoding='utf-8') as file:
            self.rule = file.read().strip()

        self.rules = self.rule
        self.iterations()

    def iterations(self):
        n, ok = QInputDialog.getInt(self, 'Title', 'Type number of iterations', 0)
        if ok:
            temp = ''
            for j in range(n):
                self.line = int(self.line / 2) if int(self.line / 2) > 0 else 1
                self.y = self.y + 50 if self.y + 50 <= self.HEIGHT - 50 else self.HEIGHT - 50
                for i in range(len(self.rules)):
                    if self.rules[i] == 'F':
                        temp += self.rule
                    else:
                        temp += self.rules[i]
                self.rules = temp
                temp = ''
            # print(self.rules)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawFrac(qp)
        qp.end()

    def drawFrac(self, qp):
        pen = QPen(Qt.red, 1)
        qp.setPen(pen)
        for rule in self.rules:
            if rule == 'F':
                qp.drawLine(
                    self.x, self.y,
                    self.x + self.line * cos(self.angle * pi / 180),
                    self.y + self.line * sin(self.angle * pi / 180)
                )
                self.x = self.x + self.line * cos(self.angle * pi / 180)
                self.y = self.y + self.line * sin(self.angle * pi / 180)
            elif rule == '+':
                self.angle += 60
            elif rule == '-':
                self.angle -= 60


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frac = Fract()
    frac.show()
    sys.exit(app.exec())
