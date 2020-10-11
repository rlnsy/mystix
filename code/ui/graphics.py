from PyQt5 import QtGui
import pyqtgraph as pg
from typing import cast


pg.setConfigOptions(antialias=True)


class GraphicsError(Exception):
    pass


class Graphics:

    def __init__(self):
        self.app = QtGui.QApplication([])
        self.windows = {}

    def add_window(self, name: str, width: int = 500, height: int = 500) -> None:
        if name in self.windows:
            raise GraphicsError("Window '%s' already exists" % name)
        else:
            w = pg.GraphicsLayoutWidget(show=True, title=name)
            w.resize(width, height)
            self.windows[name] = w

    def display(self) -> None:
        self.app.exec()

    def get_window(self, window_name: str) -> pg.GraphicsLayoutWidget:
        if window_name not in self.windows:
            raise GraphicsError("Window '%s' does not exist" % window_name)
        else:
            return cast(pg.GraphicsLayoutWidget, self.windows[window_name])
