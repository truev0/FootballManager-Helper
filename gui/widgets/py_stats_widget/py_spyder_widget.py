

# IMPORT PYSIDE CORE
# ///////////////////////////////////////////////////////////////
from pyside_core import *

# IMPORT MODULES
# ///////////////////////////////////////////////////////////////
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

# IMPORT DICTS
# ///////////////////////////////////////////////////////////////
from gui.core.dicts import util_lists


# PY SPYDER WIDGET
# ///////////////////////////////////////////////////////////////
class PySpyderWidget(QWidget):
    def __init__(
            self,
            parent=None,
            bg_two="#343b48",
            dark_three="#21252d",
            axis_color="#f5f6f9",
            color_title="#dce1ec",
            line_color="#3f6fd1"
    ):
        super().__init__(parent)

        self.spyder_chart = _CustomSpyder(
            self,
            bg_two=bg_two,
            dark_three=dark_three,
            axis_color=axis_color,
            color_title=color_title,
            line_color=line_color
        )

        self.principal_layout = QVBoxLayout(self)
        self.principal_layout.addWidget(self.spyder_chart)


class _CustomSpyder(FigureCanvas):
    def __init__(
            self,
            parent,
            bg_two,
            dark_three,
            axis_color,
            color_title,
            line_color,
            width=6,
            height=6,
            dpi=100
    ):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(width, height), subplot_kw={'projection': 'polar'})
        super(_CustomSpyder, self).__init__(self.fig)
        # COLORS
        self.bg_two = bg_two
        self.dark_three = dark_three
        self.axis_color = axis_color
        self.color_title = color_title
        self.line_color = line_color

        self._parent = parent
        self._data = None
        self.setParent(parent)

    def set_data(self, data):
        if self._data is not None:
            self._data = pd.concat([self._data, data], axis=0)
        else:
            self._data = data

    def set_chart(self, players, opts):
        angles = [n / float(len(opts)) * 2 * pi for n in range(len(opts))]
        angles += angles[:1]
        if self._data is not None:
            self.ax.clear()
            column_index_name = self._data.columns[0]
            tmp_df = self._data[self._data[column_index_name].isin(players)]
            opts.append(column_index_name)
            tmp_df = tmp_df.loc[:, opts]
            tmp_df = tmp_df.set_index(column_index_name)
            # EXTRACT VALUES FOR PLAYER 1
            values1 = tmp_df.iloc[0].tolist()
            values1 += values1[:1]
            # EXTRACT VALUES FOR PLAYER 2
            values2 = tmp_df.iloc[1].tolist()
            values2 += values2[:1]
            opts.remove(column_index_name)
            self.ax.set_xticks(angles[:-1], opts)
            # FILL FOR PLAYER 1
            self.ax.plot(angles, values1)
            self.ax.fill(angles, values1, 'teal', alpha=0.1)
            # FILL FOR PLAYER 2
            self.ax.plot(angles, values2)
            self.ax.fill(angles, values2, 'red', alpha=0.1)
            self.fig.canvas.draw()
        else:
            self.ax.clear()
