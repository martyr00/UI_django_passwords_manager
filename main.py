import sys
from PyQt5 import QtWidgets
import sqlite3

from main_page import Ui_MainWindow
from category_create import Ui_CategoryCreate


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, metaclass=type):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def OpenCategoryCreate(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CategoryCreate()
        self.ui.setupUi(self.window)
        self.window.setWindowTitle('Создание категории')
        self.window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.setWindowTitle('Pass save')
    w.show()
    sys.exit(app.exec_())
