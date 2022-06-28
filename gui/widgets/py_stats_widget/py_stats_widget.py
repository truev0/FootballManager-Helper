

# IMPORT PYSIDE CORE
# ///////////////////////////////////////////////////////////////
from pyside_core import *

# IMPORT MODULES
# ///////////////////////////////////////////////////////////////
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import mplcursors

# IMPORT DICTS
# ///////////////////////////////////////////////////////////////
from gui.core.dicts import util_lists

# IMPORT PY COMBO BOX
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_combo_box import PyComboBox


# PY STATS WIDGET
# ///////////////////////////////////////////////////////////////
class PyStatsWidget(QWidget):
    def __init__(
            self,
            name,
            language,
            parent=None,
            dark_one="#1b1e23",
            text_foreground="#8a95aa",
            combo_border="#6c99f4",
            bg_two="#343b48",
            dark_three="21252d",
            axis_color="f5f6f9",
            color_title="dce1ec",
            bar_color="3f6fd1"
    ):
        super().__init__(parent)
        self.name = name
        self.language = language
        self.type_selector = PyComboBox(
            dark_one=dark_one,
            text_foreground=text_foreground,
            combo_border=combo_border,
        )
        self.combo_selector = PyComboBox(
            dark_one=dark_one,
            text_foreground=text_foreground,
            combo_border=combo_border
        )

        self.chart = _CustomCanvas(
            self,
            name=self.name,
            language=self.language,
            bg_two=bg_two,
            dark_three=dark_three,
            axis_color=axis_color,
            color_title=color_title,
            bar_color=bar_color
        )

        self.principal_layout = QVBoxLayout(self)
        self.alter_layout = QHBoxLayout()
        self.alter_layout.addWidget(self.type_selector)
        self.alter_layout.addWidget(self.combo_selector)
        self.principal_layout.addLayout(self.alter_layout)
        self.principal_layout.addWidget(self.chart)

        self.type_selector.currentIndexChanged.connect(self.updateDependentCombo)
        self.updateDependentCombo(self.type_selector.currentIndex())

        self.combo_selector.currentTextChanged.connect(
            self.chart.update_chart
        )

    def updateDependentCombo(self, index):
        self.combo_selector.clear()
        dependent_list = self.type_selector.itemData(index)
        if dependent_list:
            self.combo_selector.addItems(dependent_list)


class _CustomCanvas(FigureCanvas):
    def __init__(
            self,
            parent,
            language,
            name,
            bg_two,
            dark_three,
            axis_color,
            color_title,
            bar_color,
    ):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(6, 5), sharey=True)
        super().__init__(self.fig)
        # COLORS
        self.bg_two = bg_two
        self.dark_three = dark_three
        self.axis_color = axis_color
        self.color_title = color_title
        self.bar_color = bar_color

        self._name = name
        self._language = language
        self._actual_list = ['']
        self._data = None
        self._parent = parent
        self.setParent(parent)
        if self._name == "graph_statistics" and self._language == "en":
            self.ax.set_title("Statistics Chart", fontsize=15, color=self.color_title)
        elif self._name == "graph_statistics" and self._language == "es":
            self.ax.set_title("Gráfico de Estadísticas", fontsize=15, color=self.color_title)
        elif self._name == "graph_metrics" and self._language == "en":
            self.ax.set_title("Metrics Chart", fontsize=15, color=self.color_title)
        elif self._name == "graph_metrics" and self._language == "es":
            self.ax.set_title("Gráfico de Métricas", fontsize=15, color=self.color_title)

        self.fig.patch.set_facecolor(self.bg_two)
        self.ax.set_facecolor(self.dark_three)
        self.ax.xaxis.label.set_color(self.axis_color)
        self.ax.yaxis.label.set_color(self.axis_color)
        self.ax.tick_params(axis='x', colors=self.axis_color)
        self.ax.tick_params(axis='y', colors=self.axis_color)
        self.ax.title.set_color(self.color_title)

    def count_actual_list(self):
        return len(self._actual_list)

    def set_data(self, data):
        self._data = data

    def add_to_list(self, e_list):
        if len(self._actual_list) == 1:
            self._actual_list[0] = e_list[0]
            if len(e_list) > 1:
                for i in range(1, len(e_list)):
                    self._actual_list.append(e_list[i])
        else:
            for e in e_list:
                self._actual_list.append(e)

    def update_chart(self, new_parameter):
        if self._data is not None:
            self.ax.clear()
            curr = self._parent.type_selector.currentText()
            if curr in ("Statistics", "Estadisticas"):
                if new_parameter in self._actual_list:
                    custom_df = self._data.iloc[:, :1]
                    custom_df = custom_df.join(
                        self._data[new_parameter]
                    )

                    custom_df.plot.bar(
                        x=custom_df.columns[0],
                        y=custom_df.columns[1],
                        ax=self.ax,
                        color=self.bar_color,
                        legend=None
                    )
                    self.fig.subplots_adjust(bottom=0.22)
                    if self._language == 'en':
                        self.ax.set_title(util_lists.stats_list_en[new_parameter],
                                          fontsize=15, color=self.color_title)
                    elif self._language == 'es':
                        self.ax.set_title(util_lists.stats_list_es[new_parameter],
                                          fontsize=15, color=self.color_title)

                    self.ax.tick_params(axis='x', rotation=80)
                    self.ax.axhline(y=custom_df[new_parameter].mean(), color='r', linestyle='--')
                    self.ax.set_xlabel("")
                    cursor = mplcursors.cursor(hover=mplcursors.HoverMode.Transient)

                    @cursor.connect("add")
                    def on_add(sel):
                        try:
                            x, y, width, height = sel.artist[sel.index].get_bbox().bounds
                            if ((x+width/2)+4) > len(custom_df):
                                sel.annotation.set(
                                    text=f"{custom_df[custom_df.columns[0]][sel.index]}: {height:g}",
                                    position=(-10, 0), anncoords="offset points"
                                )
                            else:
                                sel.annotation.set(
                                    text=f"{custom_df[custom_df.columns[0]][sel.index]}: {height:g}",
                                    position=(10, 0), anncoords="offset points"
                                )
                            sel.annotation.xy = (x + width / 2, y + height)
                            sel.annotation.get_bbox_patch().set(alpha=0.8)
                        except TypeError:
                            pass
                else:
                    self.ax.clear()
            elif curr in ("Metrics", "Metricas"):
                if new_parameter in self._actual_list:
                    custom_df = self._data.iloc[:, :1]
                    custom_df = custom_df.join(
                        self._data[
                            [
                                util_lists.metrics_list[new_parameter][0],
                                util_lists.metrics_list[new_parameter][1]
                            ]
                        ]
                    )
                    tmp_x = custom_df.columns[1]
                    tmp_y = custom_df.columns[2]
                    custom_df.plot.scatter(
                        x=tmp_x,
                        y=tmp_y,
                        ax=self.ax,
                        color=self.bar_color,
                        legend=None
                    )
                    self.fig.subplots_adjust(bottom=0.1)
                    if self._language == 'en':
                        self.ax.set_xlabel(util_lists.stats_list_en[tmp_x], size=12)
                        self.ax.set_ylabel(util_lists.stats_list_en[tmp_y], size=12)
                    elif self._language == 'es':
                        self.ax.set_xlabel(util_lists.stats_list_es[tmp_x], size=12)
                        self.ax.set_ylabel(util_lists.stats_list_es[tmp_y], size=12)
                    self.ax.set_title(new_parameter, color=self.color_title, size=15)

                    self.ax.axhline(y=custom_df[tmp_y].mean(), color='r', linestyle=':')
                    self.ax.axvline(x=custom_df[tmp_x].mean(), color='r', linestyle=':')
                    cursor = mplcursors.cursor(hover=mplcursors.HoverMode.Transient)

                    @cursor.connect("add")
                    def on_add(sel):
                        try:
                            if self._language == 'en':
                                sel.annotation.set_text(
                                    "{}\n{}: {:.2f}\n{}: {:.2f}".format(custom_df[custom_df.columns[0]][sel.index],
                                                                        util_lists.stats_list_en[custom_df.columns[1]],
                                                                        sel.target[0],
                                                                        util_lists.stats_list_en[custom_df.columns[2]],
                                                                        sel.target[1])
                                )
                            elif self._language == 'es':
                                sel.annotation.set_text(
                                    "{}\n{}: {:.2f}\n{}: {:.2f}".format(custom_df[custom_df.columns[0]][sel.index],
                                                                        util_lists.stats_list_es[custom_df.columns[1]],
                                                                        sel.target[0],
                                                                        util_lists.stats_list_es[custom_df.columns[2]],
                                                                        sel.target[1])
                                )
                            sel.annotation.get_bbox_patch().set(alpha=0.8)
                        except KeyError:
                            pass
                else:
                    self.ax.clear()
            self.ax.grid(False)
            self.fig.canvas.draw()
