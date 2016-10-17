import sys
import numpy
from json import load, JSONDecodeError
from math import pi
from Lab1.uniform_distribution import chud

from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import (QWidget, QTextEdit, QAction, QDesktopWidget, QApplication, QPushButton, QMainWindow,
                             QTabWidget, QVBoxLayout, QLabel,
                             QGridLayout, QLineEdit, QFileDialog, QMessageBox, QToolTip)
from PyQt5.QtGui import QIcon
from matplotlib import pyplot


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.sizeHint()
        self.setFont(QFont("Menlo", 14))
        QToolTip.setFont(QFont('Menlo', 14))
        self.statusBar().showMessage('Ready')
        self.statusBar()
        self.setGeometry(500, 500, 550, 550)
        self.center()
        self.setWindowTitle('Random processes 2016_v2 by Oleksiy Polshchak KM-42')
        self.setWindowIcon(QIcon('icon/ic_account_balance_black_24px.svg'))

        #Building some buttons
        tab1_button = self.create_new_button(0, 'icon/ic_tab_black_24px.svg', 'Lab1', 0, [25, 50], 'Open Lab #1', True)
        tab2_button = self.create_new_button(0, 'icon/ic_tab_unselected_black_24px.svg', 'Lab2', 0, [125, 50],
                                             'Open Lab #2', False)
        tab3_button = self.create_new_button(0, 'icon/ic_tab_unselected_black_24px.svg', 'Lab3', 0, [225, 50],
                                             'Open Lab #3', False)
        tab4_button = self.create_new_button(0, 'icon/ic_tab_unselected_black_24px.svg', 'Lab4', 0, [325, 50],
                                             'Open Lab #4', False)
        tab2_button = self.create_new_button(0, 'icon/ic_tab_unselected_black_24px.svg', 'Lab5', 0, [425, 50],
                                             'Open Lab #5', False)

        self.center()
        self.show()

    def create_new_button(self, connect_to, icon_src, button_label, button_size, button_pos, tool_tip, ED_status):
        new_button = QPushButton(QIcon(icon_src), button_label, self)
        if button_size == 0:
            new_button.resize(new_button.sizeHint())
        else:
            new_button.resize(button_size[0], button_size[1])
        new_button.move(button_pos[0], button_pos[1])
        new_button.setToolTip(tool_tip)
        if connect_to == 0:
            pass
        else:
            new_button.clicked.connect(connect_to)
        new_button.setEnabled(ED_status)
        return new_button

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def make_some_think_or_just_klick(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
