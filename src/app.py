#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

import ui


def main():
  application = QtGui.QApplication(sys.argv)
  window = ui.MainWindow()
  sys.exit(application.exec_())


if __name__ == '__main__':
  main()
