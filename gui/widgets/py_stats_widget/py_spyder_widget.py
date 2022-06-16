

# IMPORT PYSIDE CORE
# ///////////////////////////////////////////////////////////////
from pyside_core import *

# IMPORT MODULES
# ///////////////////////////////////////////////////////////////
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import pandas as pd

# IMPORT DICTS
# ///////////////////////////////////////////////////////////////
from gui.core.dicts import util_lists


# PY SPYDER WIDGET
# ///////////////////////////////////////////////////////////////
class PySpyderWidget(QWidget):
    def __init__(
            self,
            language,
            parent=None,
            bg_two="#343b48",
            dark_three="#21252d",
            axis_color="#f5f6f9",
            color_title="#dce1ec",
            line_color="#3f6fd1"
    ):
        super().__init__(parent)
        self.language = language

        self.spyder_chart = None

        self.principal_layout = QVBoxLayout(self)
        self.principal_layout.addWidget(self.spyder_chart)


class _CustomSpyder(FigureCanvas):
    def __init__(
            self,
            parent,
            language,
            bg_two,
            dark_three,
            axis_color,
            color_title,
            line_color
    ):
        fig1, self.ax = plt.subplots(figsize=(6, 6), dpi=101)
        super().__init__(fig1)
        # COLORS
        self.bg_two = bg_two
        self.dark_three = dark_three
        self.axis_color = axis_color
        self.color_title = color_title
        self.line_color = line_color

        self._language = language
        self._parent = parent
        self._data = None
        self.setParent(parent)

    def set_data(self, data):
        if self._data is not None:
            self._data = pd.concat([self._data, data], axis=0)
        else:
            self._data = data
