# IMPORT PYSIDE CORE
# ///////////////////////////////////////////////////////////////
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# IMPORT MODULES
# ///////////////////////////////////////////////////////////////
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from pyside_core import *  # lgtm [py/polluting-import]

# IMPORT MPLSOCCER
# ///////////////////////////////////////////////////////////////
from .py_radar_chart import Radar


# PY SPYDER WIDGET
# ///////////////////////////////////////////////////////////////
class PySpyderWidget(QWidget):

    def __init__(
        self,
        language="en",
        parent=None,
        bg_two="#343b48",
        bg_one="#343b48",
        dark_three="#21252d",
        axis_color="#f5f6f9",
        color_title="#dce1ec",
        line_color="#3f6fd1",
    ):
        super().__init__(parent)

        self.language = language

        self.spyder_chart = _CustomSpyder(
            self,
            language=self.language,
            bg_two=bg_two,
            bg_one=bg_one,
            dark_three=dark_three,
            axis_color=axis_color,
            color_title=color_title,
            line_color=line_color,
        )

        self.principal_layout = QVBoxLayout(self)
        self.principal_layout.addWidget(self.spyder_chart)


class _CustomSpyder(FigureCanvas):

    def __init__(
        self,
        parent,
        bg_two,
        bg_one,
        dark_three,
        axis_color,
        color_title,
        line_color,
        language="en",
    ):

        self.fig, self.ax = radar_mosaic(radar_height=0.915,
                                         title_height=0.06,
                                         fig_height=14)
        super(_CustomSpyder, self).__init__(self.fig)
        # COLORS
        self.bg_two = bg_two
        self.bg_one = bg_one
        self.dark_three = dark_three
        self.axis_color = axis_color
        self.color_title = color_title
        self.line_color = line_color
        self.COLORS = ["#FF5A5F", "#007A87", "#FFB400"]

        # Inner Dataframes
        self._inner_squad = None
        self._inner_scouting = None
        self._inner_old_squad = None

        self.language = language

        self.fig.set_facecolor(self.bg_one)
        self.ax["radar"].axis("off")
        self.ax["title"].set_facecolor(self.bg_one)
        self.ax["radar"].set_facecolor(self.bg_one)
        self.ax["radar"].xaxis.label.set_color(self.bg_one)
        self.ax["radar"].yaxis.label.set_color(self.bg_one)
        self.ax["radar"].tick_params(axis="x", colors=self.bg_one)
        self.ax["radar"].tick_params(axis="y", colors=self.bg_one)

        self._parent = parent
        self._data = None
        self.setParent(parent)

    def set_data(self, data):
        if self._data is None and self._inner_squad is None:
            self._data = data
            self._inner_squad = data
        elif self._data is not None and self._inner_scouting is None:
            self._data = pd.concat([self._data, data], axis=0)
            self._data.reset_index(drop=True, inplace=True)
            self._inner_scouting = data
        elif self._data is not None and self._inner_old_squad is None:
            self._data = pd.concat([self._data, data], axis=0)
            self._data.reset_index(drop=True, inplace=True)
            self._inner_old_squad = data
        elif self._data is not None and self._inner_scouting is not None:
            self._data = None
            self._data = self._inner_squad
            self._data = pd.concat([self._data, data], axis=0)
            self._data = pd.concat([self._data, self._inner_old_squad], axis=0)
            self._data.reset_index(drop=True, inplace=True)

    def set_chart(self, players, squads, opts):
        if opts:
            self.ax["radar"].clear()
            self.ax["title"].clear()
            self.ax["title"].axis("off")
            if self._data is not None and len(players) <= 3:
                min_ranges = []
                max_ranges = []
                column_index_name = self._data.columns[0]
                tmp_df = self._data[self._data[column_index_name].isin(
                    players)]
                for o in opts:
                    a = tmp_df[o].min()
                    a = a - (a * 0.15)

                    b = tmp_df[o].max()
                    b = b + (b * 0.15)

                    min_ranges.append(a)
                    max_ranges.append(b)

                radar = Radar(
                    opts,
                    min_ranges,
                    max_ranges,
                    round_int=[False] * len(opts),
                    num_rings=6,
                    ring_width=1,
                    center_circle_radius=1,
                )

                radar.setup_axis(ax=self.ax["radar"], facecolor=self.bg_one)
                radar.draw_circles(
                    ax=self.ax["radar"],
                    facecolor=self.dark_three,
                    edgecolor=self.dark_three,
                )
                # /////////////////////////////////////////////////////////////////////////////
                opts.append(column_index_name)
                tmp_df = tmp_df.loc[:, opts]
                tmp_df = tmp_df.set_index(column_index_name)

                values1 = tmp_df.iloc[0].tolist()
                if players[0] == players[1]:
                    values2 = tmp_df.iloc[0].tolist()
                else:
                    values2 = tmp_df.iloc[1].tolist()
                # /////////////////////////////////////////////////////////////////////////////
                radar_output = radar.draw_radar_compare(
                    values1,
                    values2,
                    ax=self.ax["radar"],
                    kwargs_radar={
                        "facecolor": self.COLORS[0],
                        "alpha": 0.15
                    },
                    kwargs_compare={
                        "facecolor": self.COLORS[1],
                        "alpha": 0.15
                    },
                )
                radar_poly, radar_poly2, vertices1, vertices2 = radar_output

                radar.draw_range_labels(ax=self.ax["radar"],
                                        fontsize=10,
                                        color=self.axis_color)

                radar.draw_param_labels(ax=self.ax["radar"],
                                        fontsize=15,
                                        color=self.axis_color)
                vertices11 = np.append(vertices1, vertices1[0])
                vertices22 = np.append(vertices2, vertices2[0])
                vertices11 = np.reshape(vertices11,
                                        (int(len(vertices11) / 2), 2))
                vertices22 = np.reshape(vertices22,
                                        (int(len(vertices22) / 2), 2))
                self.ax["radar"].scatter(
                    vertices1[:, 0],
                    vertices1[:, 1],
                    c=self.COLORS[0],
                    marker="D",
                    s=90,
                    zorder=2,
                )
                self.ax["radar"].scatter(
                    vertices2[:, 0],
                    vertices2[:, 1],
                    c=self.COLORS[1],
                    marker="D",
                    s=90,
                    zorder=2,
                )
                self.ax["radar"].plot(
                    vertices11[:, 0],
                    vertices11[:, 1],
                    self.COLORS[0],
                    linewidth=2.5,
                    linestyle=":",
                    zorder=2,
                )
                self.ax["radar"].plot(
                    vertices22[:, 0],
                    vertices22[:, 1],
                    self.COLORS[1],
                    linewidth=2.5,
                    linestyle=":",
                    zorder=2,
                )
                var1, var2 = change_squad(squads, self.language)
                self.ax["title"].text(
                    0.01,
                    0.65,
                    players[0],
                    fontsize=18,
                    color=self.COLORS[0],
                    ha="left",
                    va="center",
                )
                self.ax["title"].text(
                    0.99,
                    0.65,
                    players[1],
                    fontsize=18,
                    color=self.COLORS[1],
                    ha="right",
                    va="center",
                )
                self.ax["title"].text(
                    0.01,
                    0.1,
                    var1,
                    fontsize=10,
                    color=self.COLORS[0],
                    ha="left",
                    va="center",
                )
                self.ax["title"].text(
                    0.99,
                    0.1,
                    var2,
                    fontsize=10,
                    color=self.COLORS[1],
                    ha="right",
                    va="center",
                )
                self.fig.canvas.draw()


def radar_mosaic(radar_height=0.915, title_height=0.06, fig_height=14):

    if title_height + radar_height > 1:
        error_msg = (
            "Reduce one of the radar_height or title_height so the total is <= 1."
        )
        raise ValueError(error_msg)
    end_note_height = 1 - radar_height - title_height
    fig_width = fig_height * radar_height
    figure, axes = plt.subplot_mosaic(
        [["title"], ["radar"], ["endnote"]],
        gridspec_kw={
            "height_ratios": [title_height, radar_height, end_note_height],
            "bottom": 0,
            "left": 0,
            "top": 1,
            "right": 1,
            "hspace": 0,
        },
        figsize=(fig_width, fig_height),
    )
    axes["title"].axis("off")
    axes["endnote"].axis("off")
    return figure, axes


def change_squad(inner_squad, lang):
    inner_var1 = ""
    inner_var2 = ""
    if lang == "en":
        if "Actual" in inner_squad[0]:
            inner_var1 = "Actual Squad list"
        elif "Scouting" in inner_squad[0]:
            inner_var1 = "Scouting Squad list"
        elif "Old" in inner_squad[0]:
            inner_var1 = "Old Squad list"

        if "Actual" in inner_squad[1]:
            inner_var2 = "Actual Squad list"
        elif "Scouting" in inner_squad[1]:
            inner_var2 = "Scouting Squad list"
        elif "Old" in inner_squad[1]:
            inner_var2 = "Old Squad list"
    elif lang == "es":
        if "Actual" in inner_squad[0]:
            inner_var1 = "Lista actual del equipo"
        elif "Scouting" in inner_squad[0]:
            inner_var1 = "Lista de scouting"
        elif "Old" in inner_squad[0]:
            inner_var1 = "Lista vieja del equipo"

        if "Actual" in inner_squad[1]:
            inner_var2 = "Lista actual del equipo"
        elif "Scouting" in inner_squad[1]:
            inner_var2 = "Lista de scouting"
        elif "Old" in inner_squad[1]:
            inner_var2 = "Lista vieja del equipo"

    return inner_var1, inner_var2
