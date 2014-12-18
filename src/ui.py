# -*- coding: utf-8 -*-

from PyQt4 import QtGui


class MainWindow(QtGui.QWidget):

  def __init__(self):
    super(MainWindow, self).__init__()
    self.initUI()

  def initUI(self):
    self.setGeometry(100, 200, 800, 400)
    self.setWindowTitle('%s - %s' % ("Jaylen", "0.1.0"))
    self.setWindowIcon(QtGui.QIcon('resources/main.png'))
    self.show()
