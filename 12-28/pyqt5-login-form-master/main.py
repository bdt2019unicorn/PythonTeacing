import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

import sqlite3

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)

    def loginfunction(self):
        email=self.email.text()
        password=self.password.text()

        connection = sqlite3.connect("cosudulieu.db")
        sql = "SELECT * FROM nguoidung WHERE dangnhap=\'" + email + "\' AND matkhau=\'" + password + "\'"
        table = connection.execute(sql)
        list = []
        for row in table: 
            list.append(row)
        connection.close()

        if len(list)==1: 
            print("Successfully logged in with email: " + email + "and password:" + password)
        else: 
            print("Khong co nguoi dung hoac dang nhap sai mat khau")

    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("createacc.ui",self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    def createaccfunction(self):
        email = self.email.text()
        if self.password.text()==self.confirmpass.text():
            password=self.password.text()

            connection = sqlite3.connect("cosudulieu.db")
            sql = "INSERT INTO nguoidung(dangnhap, matkhau) VALUES (\'" + email + "\', \'" + password + "\')"
            connection.execute(sql)
            connection.commit()
            connection.close()

            print("Successfully created acc with email: ", email, "and password: ", password)
            login=Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)



app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()