#!/usr/bin/env python

# Just to check presence of essential libraries
from . import imports

from .imports import qtpy
from qtpy import QtCore, QtWidgets

from .viewer import Viewer

def run_app():
    import sys
    if len(sys.argv) < 2:
        path = "."
    else:
        path = sys.argv[1]

    app = QtWidgets.QApplication(sys.argv)
    QtCore.QCoreApplication.setApplicationName("pydiq")
    QtCore.QCoreApplication.setOrganizationName("UNRC")

    viewer = Viewer(path)
    viewer.show()

    sys.exit(app.exec_())

