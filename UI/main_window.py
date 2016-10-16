import sys
from json import load, JSONDecodeError
from math import pi

from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import (QWidget, QTextEdit, QAction, QDesktopWidget, QApplication, QPushButton, QMainWindow, QTabWidget, QVBoxLayout, QLabel,
                             QGridLayout, QLineEdit, QFileDialog, QMessageBox)
from PyQt5.QtGui import QIcon
from matplotlib import pyplot

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QAction(QIcon('icon/ic_exit_to_app_black_48dp_2x.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q in Linux or Command+Q in MacOS')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(500, 500, 550, 550)
        self.center()
        self.setWindowTitle('Main window')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())