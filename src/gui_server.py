# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_server.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QListWidgetItem
from NetworkConnection.server import Server
from NetworkConnection.db_api import create_db, add_user, get_users, find_by_fio

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Server_epta")
        MainWindow.resize(802, 607)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(390, 30, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 30, 231, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.electorsWidget = QtWidgets.QListWidget(self.centralwidget)
        self.electorsWidget.setGeometry(QtCore.QRect(450, 140, 256, 161))
        self.electorsWidget.setObjectName("electorsWidget")
        self.finishButton = QtWidgets.QPushButton(self.centralwidget)
        self.finishButton.setGeometry(QtCore.QRect(480, 460, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.finishButton.setFont(font)
        self.finishButton.setObjectName("finishButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 340, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.yesLabel = QtWidgets.QLabel(self.centralwidget)
        self.yesLabel.setGeometry(QtCore.QRect(510, 340, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.yesLabel.setFont(font)
        self.yesLabel.setObjectName("yesLabel")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 380, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.noLabel = QtWidgets.QLabel(self.centralwidget)
        self.noLabel.setGeometry(QtCore.QRect(510, 380, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.noLabel.setFont(font)
        self.noLabel.setObjectName("noLabel")
        self.allWidget = QtWidgets.QListWidget(self.centralwidget)
        self.allWidget.setGeometry(QtCore.QRect(80, 110, 256, 371))
        self.allWidget.setObjectName("allWidget")
        self.fioEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.fioEdit.setGeometry(QtCore.QRect(400, 110, 201, 20))
        self.fioEdit.setObjectName("fioEdit")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(610, 110, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 80, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.updateButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateButton.setGeometry(QtCore.QRect(120, 500, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.updateButton.setFont(font)
        self.updateButton.setObjectName("updateButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.addButton.clicked.connect(self.add_voters)
        self.updateButton.clicked.connect(self.update_voters)
        self.finishButton.clicked.connect(self.finish)
        self.db_name = "voting.db"
        
        # Create a QThread object
        self.thread = QThread()
        # Create a server object
        self.server = Server(db_name=self.db_name)
        # Move server to the thread
        self.server.moveToThread(self.thread)
        # Connect signals and slots
        self.thread.started.connect(self.server.run)
        self.server.finished.connect(self.thread.quit)
        self.server.finished.connect(self.server.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # Step 6: Start the thread
        self.thread.start()
        self.thread.finished.connect(self.finish)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Server"))
        self.startButton.setText(_translate("MainWindow", "Начать голосование"))
        self.label.setText(_translate("MainWindow", "Вопрос голосования"))
        self.finishButton.setText(_translate("MainWindow", "Подсчитать голоса"))
        self.label_2.setText(_translate("MainWindow", "Да - "))
        self.yesLabel.setText(_translate("MainWindow", "0.0%"))
        self.label_4.setText(_translate("MainWindow", "Нет - "))
        self.noLabel.setText(_translate("MainWindow", "0.0%"))
        self.addButton.setText(_translate("MainWindow", "Добавить избирателя"))
        self.label_3.setText(_translate("MainWindow", "Все участники системы"))
        self.updateButton.setText(_translate("MainWindow", "Обновить"))

    def add_voters(self):
        fio = self.fioEdit.text()
        users = find_by_fio(db_name=self.db_name, table="voters", fio=fio)
        user = users[0]
        add_user(db_name=self.db_name, table="current_voters", fio=user["fio"], public_key=user["public_key"])
        users = get_users(self.db_name, table="current_voters")
        for user in users:
            self.electorsWidget.addItem(QListWidgetItem(user["fio"].upper()))

    def update_voters(self):
        self.allWidget.clear()
        users = get_users(self.db_name, table="voters")
        for user in users:
            self.allWidget.addItem(QListWidgetItem(user["fio"].upper()))

    def finish(self):
        self.server.is_active = False


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    err = app.exec_()
    sys.exit(err)
