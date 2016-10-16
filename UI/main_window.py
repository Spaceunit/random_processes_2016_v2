import sys
from json import load, JSONDecodeError
from math import pi

from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QMainWindow, QTabWidget, QVBoxLayout, QLabel,
                             QGridLayout, QLineEdit, QFileDialog, QMessageBox)
from matplotlib import pyplot