from PyQt5.QtWidgets import QApplication, QPushButton,  QWidget, QMainWindow, QTableWidget,  QTableWidgetItem,\
    QInputDialog, QMessageBox
import sys

class Table(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUi()
        self.btn.clicked.connect(self.add)
        self.table.cellDoubleClicked[int, int].connect(self.edit)

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

    def add(self):
        txt, true = QInputDialog.getText(self, 'Add', 'Enter number in 10 system')
        if true:
            try:
                number = int(txt)
                min = ""
                if number < 0:
                    min += "-"
                    number *= -1
                self.table.insertRow(self.table.rowCount())
                i = self.table.rowCount() - 1
                self.table.setItem(i, 0, QTableWidgetItem(min+str(number)))
                self.table.setItem(i, 1, QTableWidgetItem(min+self.convert(number, 2, 10)))
                self.table.setItem(i, 2, QTableWidgetItem(min+self.convert(number, 16, 10)))
            except:
                QMessageBox.critical(self, "Error", "Wrong number format")

    def edit(self, row, col):
        systxt = ""
        sys = 0
        if col == 0:
            systxt = "10"
            sys = 10
        elif col == 1:
            systxt = "2"
            sys = 2
        else:
            systxt = "16"
            sys = 16

        txt, true = QInputDialog.getText(self, 'Edit', 'Enter New '+systxt+' system')
        if true:
            try:
                number = txt
                min = ""
                if "-" in number:
                    min += "-"
                    number = number[1:]
                self.table.setItem(row, 0, QTableWidgetItem(min + self.convert(number, 10, sys)))
                self.table.setItem(row, 1, QTableWidgetItem(min + self.convert(number, 2, sys)))
                self.table.setItem(row, 2, QTableWidgetItem(min + self.convert(number, 16, sys)))
            except:
                QMessageBox.critical(self, "Error", "Wrong number format")



    def convert(self, number, to_base = 10, from_base = 10):
        if isinstance(number, str):
            n = int(number, from_base)
        else:
            n = int(number)
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n < to_base:
            return str(alphabet[n])
        else:
            return self.convert(n // to_base, to_base) + alphabet[n % to_base]




if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    qapp.setStyleSheet(open("newstyle.qss", 'r').read())
    main_windows = QMainWindow()
    j = Table(main_windows)
    main_windows.setFixedSize(900, 800)
    main_windows.show()
    qapp.exec_()