from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QButtonGroup, QWidget, QMainWindow, QGridLayout, QLayout, \
    QLineEdit, QTableWidget, QSpinBox, QTableWidgetItem, QInputDialog, QMessageBox, QComboBox, QLabel
import sys

class Journal(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUi()
        self.btn.clicked.connect(self.add_num)
        self.Flag = False
        self.table.cellDoubleClicked[int, int].connect(self.edit_num)

    def initUi(self):
        self.resize(900, 800)
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["10 СС", "2 СС", "16 СС"])
        self.table.setGeometry(0, 0, 425, 750)
        self.table.move(450, 10)
        self.btn = QPushButton("Add", self)
        self.btn.setGeometry(0, 0, 400, 100)
        self.btn.move(10, 10)

    def add_num(self):
        text, ok = QInputDialog.getText(self, 'Add', 'Enter number in 10 system')
        if ok:
            try:
                num = int(text)
                minus = ""
                if num < 0:
                    minus += "-"
                    num *= -1
                self.table.insertRow(self.table.rowCount())
                i = self.table.rowCount() - 1
                self.table.setItem(i, 0, QTableWidgetItem(minus+str(num)))
                self.table.setItem(i, 1, QTableWidgetItem(minus+self.convert_base(num, 2, 10)))
                self.table.setItem(i, 2, QTableWidgetItem(minus+self.convert_base(num, 16, 10)))
            except:
                QMessageBox.critical(self, "Error", "Wrong number format")

    def edit_num(self, row, col):
        systemtxt = ""
        system = 0
        if col == 0:
            systemtxt = "10"
            system = 10
        elif col == 1:
            systemtxt = "2"
            system = 2
        else:
            systemtxt = "16"
            system = 16

        text, ok = QInputDialog.getText(self, 'Edit', 'Enter New '+systemtxt+' system')
        if ok:
            try:
                num = text
                minus = ""
                if "-" in num:
                    minus += "-"
                    num = num[1:]
                self.table.setItem(row, 0, QTableWidgetItem(minus + self.convert_base(num, 10, system)))
                self.table.setItem(row, 1, QTableWidgetItem(minus + self.convert_base(num, 2, system)))
                self.table.setItem(row, 2, QTableWidgetItem(minus + self.convert_base(num, 16, system)))
            except:
                QMessageBox.critical(self, "Error", "Wrong number format")



    def convert_base(self, num, to_base = 10, from_base = 10):
        if isinstance(num, str):
            n = int(num, from_base)
        else:
            n = int(num)
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n < to_base:
            return str(alphabet[n])
        else:
            return self.convert_base(n // to_base, to_base) + alphabet[n % to_base]




if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    qapp.setStyleSheet(open("newstyle.qss", 'r').read())
    main_windows = QMainWindow()
    j = Journal(main_windows)
    main_windows.setFixedSize(900, 800)
    main_windows.show()
    qapp.exec_()