import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CategoryCreate(object):
    def setupUi(self, QuoteCreate):
        QuoteCreate.setObjectName("QuoteCreate")
        QuoteCreate.resize(431, 125)
        self.push_button = QtWidgets.QPushButton(QuoteCreate)
        self.push_button.setGeometry(QtCore.QRect(10, 70, 111, 31))
        self.push_button.setObjectName("pushButton")
        self.push_button.clicked.connect(self.create_category)
        self.push_button.clicked.connect(QuoteCreate.close)
        self.label_4 = QtWidgets.QLabel(QuoteCreate)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 291, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(QuoteCreate)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 401, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(QuoteCreate)
        QtCore.QMetaObject.connectSlotsByName(QuoteCreate)

    def retranslateUi(self, QuoteCreate):
        _translate = QtCore.QCoreApplication.translate
        QuoteCreate.setWindowTitle(_translate("QuoteCreate", "Dialog"))
        self.push_button.setText(_translate("QuoteCreate", "Сохранить"))
        self.label_4.setText(_translate("QuoteCreate", "Название Категории"))

    def create_category(self,):
        title = self.lineEdit.text()
        print(type(title))

        con = sqlite3.connect(r'pass_save.db')
        cur = con.cursor()

        cur.execute("INSERT INTO category (title) VALUES (?)", (title,))

        con.commit()
        con.close()
