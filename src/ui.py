# -*- coding: utf-8 -*-

from PyQt4 import QtGui


class MainWindow(QtGui.QMainWindow):

  def __init__(self):
    super(MainWindow, self).__init__()
    self.init()

  def init(self):
    self.resize(800, 480)
    self.center()
    self.setWindowTitle('%s - %s' % ("Jaylen", "0.1.0"))
    self.setWindowIcon(QtGui.QIcon('resources/main.png'))
    self.statusBar().showMessage('ready')
    self.buildMainMenu()
    self.show()

  def closeEvent(self, event):
    buttons = QtGui.QMessageBox.Yes | QtGui.QMessageBox.No
    default = QtGui.QMessageBox.No
    box = QtGui.QMessageBox()
    reply = box.question(self, "Confirm application exit", "Do you really want to exit?", buttons, default)
    if reply == QtGui.QMessageBox.Yes:
      event.accept()
    else:
      event.ignore()

  def center(self):
    frameGeometry = self.frameGeometry()
    frameGeometry.moveCenter(QtGui.QDesktopWidget().availableGeometry().center())
    self.move(frameGeometry.topLeft())

  def buildMainMenu(self):
    exitAction = QtGui.QAction('&Exit', self)
    exitAction.setShortcut('Ctrl+Q')
    exitAction.setStatusTip('Exit application')
    exitAction.triggered.connect(QtGui.qApp.quit)
    menuBar = self.menuBar()
    fileMenu = menuBar.addMenu('&File')
    fileMenu.addAction(exitAction)