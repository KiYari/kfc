from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *

class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        self.sumb = ""
        self.suma = 0
        super(MyWindow, self).__init__()
        uic.loadUi('src/kfc.ui', self)
        self.tenders_cb = self.findChild(QCheckBox, "tenders_cb")
        self.tights_cb = self.findChild(QCheckBox, "tights_cb")
        self.lits_cb = self.findChild(QCheckBox, "lits_cb")
        self.corn_cb = self.findChild(QCheckBox, "corn_cg")
        self.tenders_sb = self.findChild(QSpinBox, "tenders_sb")
        self.tights_sb = self.findChild(QSpinBox, "tights_sb")
        self.lits_sb = self.findChild(QSpinBox, "lits_sb")
        self.corn_sb = self.findChild(QSpinBox, "corn_sb")
        self.textEdit = self.findChild(QTextEdit, "textEdit")
        self.check_button = self.findChild(QPushButton, "check_button")


        self.check_button.clicked.connect(self.butt)

    def butt(self):
        self.sumb = ""
        self.suma = 0
        if self.tenders_cb.isChecked() == True and self.tenders_sb.value() != 0:
            self.sumb += str(self.tenders_sb.value())
            self.suma += self.tenders_sb.value() * 109
            self.sumb += " * 109 Extra Crispy Tenders\n"
        if self.tights_cb.isChecked() == True and self.tights_sb.value() != 0:
            self.sumb += str(self.tights_sb.value())
            self.suma += self.tights_sb.value()*399
            self.sumb += " * 399 Anime Chick's Tights\n"
        if self.lits_cb.isChecked() == True and self.lits_sb.value() != 0:
           self.sumb += str(self.lits_sb.value())
           self.suma += self.lits_sb.value()*139
           self.sumb += " * 139 Chicken Littles\n"
        if self.corn_cb.isChecked() == True and self.corn_sb.value() != 0:
           self.sumb += str(self.corn_sb.value())
           self.suma += self.corn_sb.value()*159
           self.sumb += " * 159 Popcorn Nuggets\n"

        if self.sumb != "":
            self.sumb += "You have "
            self.sumb += str(self.suma)
            self.sumb += " to pay"
            self.sumb += "\nTY 4 eating here"
            self.textEdit.setText(self.sumb)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MyWindow()
    ui.show()
    sys.exit(app.exec_())
