from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

n = 0
num_ver = '1.0.0.1'


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Программа v. {0}".format(num_ver))
        self.setGeometry(300, 250, 350, 200)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Бесполезная история с ачивками")
        self.main_text.move(10, 10)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("Нажать")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)

    def add_label(self):
        global n
        n += 1
        self.new_text.setText('Нажатий {0}'.format(n))
        self.new_text.move(100, 50)
        self.new_text.adjustSize()
        if n == 10:
            self.main_text.setText('Ачивка #ДЖУН за {0} нажатий'.format(n))
            self.main_text.adjustSize()
        elif n == 50:
            self.main_text.setText('Ачивка #УПЕРТЫЙСЫКИНСЫН за {0} нажатий'.format(n))
            self.main_text.adjustSize()
        elif n == 90:
            self.main_text.setText('Ачивка #НАКРАЮБЕЗДНЫ за {0} нажатий'.format(n))
            self.main_text.adjustSize()
        if n == 100:
            sys.exit(0)


def applications():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    applications()
