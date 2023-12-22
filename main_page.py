import signal
import sqlite3
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 570)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 241, 401))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 121, 41))
        self.label_2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 100, 141, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 170, 141, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 200, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 230, 141, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 290, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(10, 320, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 350, 181, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.create_account)
        self.pushButton.clicked.connect(self.refresh_data)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(750, 420, 41, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 190, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(270, 40, 501, 371))
        self.tableWidget.setObjectName("tableWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Ошибка")
        self.msg.setText("Проверьте правильность введенных данных")
        self.msg.setIcon(QMessageBox.Warning)
        self.pushButton_2.clicked.connect(self.refresh_data)

        self.retranslateUi(MainWindow)
        self.action.triggered.connect(MainWindow.OpenCategoryCreate)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.show_table()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Логин"))
        self.label_3.setText(_translate("MainWindow", "Пароль"))
        self.label_4.setText(_translate("MainWindow", "Почта"))
        self.label_5.setText(_translate("MainWindow", "Сайт"))
        self.label_6.setText(_translate("MainWindow", "Категория"))
        self.pushButton.setText(_translate("MainWindow", "Создать"))
        self.pushButton_2.setText(_translate("MainWindow", "R"))
        self.menu.setTitle(_translate("MainWindow", "Категории"))
        self.action.setText(_translate("MainWindow", "Создать"))


        con = sqlite3.connect(r'pass_save.db')
        cur = con.cursor()

        category_titles = cur.execute('SELECT title FROM category').fetchall()
        list_category_titles = [category_title[0] for category_title in category_titles]

        i = 0
        for title in list_category_titles:
            i += 1
            self.comboBox.addItem("")
            self.comboBox.setItemText(i, _translate("MainWindow", title))
        self.show_table()

    def refresh_data(self):
        self.show_table()
        self.comboBox.clear()

        con = sqlite3.connect(r'pass_save.db')
        cur = con.cursor()

        category_titles = cur.execute('SELECT title FROM category').fetchall()
        list_category_titles = [category_title[0] for category_title in category_titles]

        self.comboBox.addItems(list_category_titles)

        con.close()

    def show_table(self):
        con = sqlite3.connect(r'pass_save.db')
        cur = con.cursor()
        cur.execute(
            'SELECT account.login, account.password, account.email, account.website, category.title FROM account JOIN category ON account.id_category = category.id_category;')
        data = cur.fetchall()
        con.close()
        if data:
            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setColumnCount(len(data[0]))
            column_headers = ['Логин', 'Пароль', 'Почта', 'Сайт', 'Категория']
            self.tableWidget.setHorizontalHeaderLabels(column_headers)

            for row_num, row_data in enumerate(data):
                for col_num, col_data in enumerate(row_data):
                    self.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))
        con.close()

    def create_account(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        email = self.lineEdit_3.text()
        website = self.lineEdit_4.text()
        category_title = self.comboBox.currentText()
        con = sqlite3.connect(r'pass_save.db')
        cur = con.cursor()

        id_category = cur.execute("SELECT id_category FROM category WHERE title = ?", (category_title,)).fetchall()
        print()
        id_category = id_category[0][0] if id_category else None
        if login and password and email and id_category:
            cur.execute(
                "INSERT INTO account (login, password, email, website, id_category) VALUES (?, ?, ?, ?, ?)",
                (login, password, email, website, id_category)
            )
        else:
            self.msg.exec_()

        con.commit()
        con.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.show_table()

    sys.exit(app.exec_())

# import signal
# import sqlite3
# import sys
#
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
#
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(807, 570)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.frame = QtWidgets.QFrame(self.centralwidget)
#         self.frame.setGeometry(QtCore.QRect(10, 10, 241, 401))
#         self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
#         self.frame.setObjectName("frame")
#         self.label_2 = QtWidgets.QLabel(self.frame)
#         self.label_2.setEnabled(True)
#         self.label_2.setGeometry(QtCore.QRect(10, 0, 121, 41))
#         self.label_2.setBaseSize(QtCore.QSize(0, 0))
#         font = QtGui.QFont()
#         font.setPointSize(20)
#         self.label_2.setFont(font)
#         self.label_2.setTextFormat(QtCore.Qt.PlainText)
#         self.label_2.setObjectName("label_2")
#         self.lineEdit = QtWidgets.QLineEdit(self.frame)
#         self.lineEdit.setGeometry(QtCore.QRect(10, 40, 141, 20))
#         self.lineEdit.setObjectName("lineEdit")
#         self.label_3 = QtWidgets.QLabel(self.frame)
#         self.label_3.setGeometry(QtCore.QRect(10, 60, 101, 31))
#         font = QtGui.QFont()
#         font.setPointSize(20)
#         self.label_3.setFont(font)
#         self.label_3.setObjectName("label_3")
#         self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
#         self.lineEdit_2.setGeometry(QtCore.QRect(10, 100, 141, 20))
#         self.lineEdit_2.setObjectName("lineEdit_2")
#         self.label_4 = QtWidgets.QLabel(self.frame)
#         self.label_4.setGeometry(QtCore.QRect(10, 130, 101, 31))
#         font = QtGui.QFont()
#         font.setPointSize(20)
#         self.label_4.setFont(font)
#         self.label_4.setObjectName("label_4")
#         self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
#         self.lineEdit_3.setGeometry(QtCore.QRect(10, 170, 141, 20))
#         self.lineEdit_3.setObjectName("lineEdit_3")
#         self.label_5 = QtWidgets.QLabel(self.frame)
#         self.label_5.setGeometry(QtCore.QRect(10, 200, 101, 31))
#         font = QtGui.QFont()
#         font.setPointSize(20)
#         self.label_5.setFont(font)
#         self.label_5.setObjectName("label_5")
#         self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
#         self.lineEdit_4.setGeometry(QtCore.QRect(10, 230, 141, 20))
#         self.lineEdit_4.setObjectName("lineEdit_4")
#         self.label_6 = QtWidgets.QLabel(self.frame)
#         self.label_6.setGeometry(QtCore.QRect(10, 290, 101, 31))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.label_6.setFont(font)
#         self.label_6.setObjectName("label_6")
#         self.comboBox = QtWidgets.QComboBox(self.frame)
#         self.comboBox.setGeometry(QtCore.QRect(10, 320, 141, 22))
#         self.comboBox.setObjectName("comboBox")
#         self.comboBox.addItem("")
#         self.pushButton = QtWidgets.QPushButton(self.frame)
#         self.pushButton.setGeometry(QtCore.QRect(10, 350, 181, 41))
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton.clicked.connect(self.create_account)
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(750, 420, 41, 41))
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(330, 190, 47, 13))
#         self.label.setText("")
#         self.label.setObjectName("label")
#         self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
#         self.comboBox_2.setGeometry(QtCore.QRect(270, 10, 251, 22))
#         self.comboBox_2.setObjectName("comboBox_2")
#         self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
#         self.tableWidget.setGeometry(QtCore.QRect(270, 40, 501, 371))
#         self.tableWidget.setObjectName("tableWidget")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 21))
#         self.menubar.setObjectName("menubar")
#         self.menu = QtWidgets.QMenu(self.menubar)
#         self.menu.setObjectName("menu")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#         self.action = QtWidgets.QAction(MainWindow)
#         self.action.setObjectName("action")
#         self.menu.addAction(self.action)
#         self.menubar.addAction(self.menu.menuAction())
#         self.msg = QMessageBox()
#         self.msg.setWindowTitle("Ошибка")
#         self.msg.setText("Проверьте правильность введенных данных")
#         self.msg.setIcon(QMessageBox.Warning)
#         self.pushButton_2.clicked.connect(self.refresh_data)
#         column_headers = ['№', 'Логин', 'Пароль', 'Почта', 'Сайт', 'Категория']
#         self.tableWidget.setHorizontalHeaderLabels(column_headers)
#
#         self.retranslateUi(MainWindow)
#         self.action.triggered.connect(MainWindow.OpenCategoryCreate)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#         self.show_table()
#
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.label_2.setText(_translate("MainWindow", "Логин"))
#         self.label_3.setText(_translate("MainWindow", "Пароль"))
#         self.label_4.setText(_translate("MainWindow", "Почта"))
#         self.label_5.setText(_translate("MainWindow", "Сайт"))
#         self.label_6.setText(_translate("MainWindow", "Категория"))
#         self.pushButton.setText(_translate("MainWindow", "Создать"))
#         self.pushButton_2.setText(_translate("MainWindow", "R"))
#         self.menu.setTitle(_translate("MainWindow", "Категории"))
#         self.action.setText(_translate("MainWindow", "Создать"))
#         self.comboBox.setItemText(0, _translate("MainWindow", 'Общее'))
#
#
#         con = sqlite3.connect(r'pass_save.db')
#         cur = con.cursor()
#
#         category_titles = cur.execute('SELECT title FROM category').fetchall()
#         list_category_titles = [category_title[0] for category_title in category_titles]
#
#         i = 0
#         for title in list_category_titles:
#             i += 1
#             self.comboBox.addItem("")
#             self.comboBox.setItemText(i, _translate("MainWindow", title))
#         self.show_table()
#
#     def refresh_data(self):
#         self.show_table()
#         self.comboBox.clear()
#         self.comboBox.addItem("Общее")
#
#         con = sqlite3.connect(r'pass_save.db')
#         cur = con.cursor()
#
#         category_titles = cur.execute('SELECT title FROM category').fetchall()
#         list_category_titles = [category_title[0] for category_title in category_titles]
#
#         self.comboBox.addItems(list_category_titles)
#
#         con.close()
#
#     def show_table(self):
#         column_headers = ['Логин', 'Пароль', 'Почта', 'Сайт', 'Категория']
#         self.tableWidget.setHorizontalHeaderLabels(column_headers)
#
#         con = sqlite3.connect(r'pass_save.db')
#         cur = con.cursor()
#         cur.execute('SELECT login, password, email, website, id_category  FROM account')
#         data = cur.fetchall()
#         con.close()
#         if data:
#             self.tableWidget.setRowCount(len(data))
#             self.tableWidget.setColumnCount(len(data[0]))
#
#             for row_num, row_data in enumerate(data):
#                 for col_num, col_data in enumerate(row_data):
#                     self.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))
#         con.close()
#
#     def create_account(self):
#         login = self.lineEdit.text()
#         password = self.lineEdit_2.text()
#         email = self.lineEdit_3.text()
#         website = self.lineEdit_4.text()
#         category_title = self.comboBox.currentText()
#         con = sqlite3.connect(r'pass_save.db')
#         cur = con.cursor()
#
#         id_category = cur.execute("SELECT id_category FROM category WHERE title = ?", (category_title,)).fetchall()
#         id_category = id_category[0][0] if id_category else None
#
#         cur.execute(
#             "INSERT INTO account (login, password, email, website, id_category) VALUES (?, ?, ?, ?, ?)",
#             (login, password, email, website, id_category)
#         )
#
#         con.commit()
#         con.close()
#
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     ui.show_table()
#
#     sys.exit(app.exec_())