

# IMPORT QT CORE
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
        self.type_selector = _QCustomCombo(
            dark_one=dark_one,
            text_foreground=text_foreground,
            combo_border=combo_border,
        )
        self.combo_selector = _QCustomCombo(
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


class _QCustomCombo(QComboBox):
    style_combobox = """ 
        QComboBox {{		
            background-color: {_dark_one};	
            color: {_text_foreground};
            padding-left: 40px;
            border-radius: 4px;
            font: 800 9pt "Segoe UI";
        }}
        
        QComboBox:on {{
            border: 2px solid #c2dbfe;
        }}
        
        QComboBox QListView {{
            font-size: 12px;
            border: 1px solid rgba(0, 0, 0, 10%);
            padding: 5px;
            background-color: {_dark_one};
            outline: 0px;
        }}
        """

    def __init__(
            self,
            text_foreground,
            dark_one,
            combo_border
    ):
        QComboBox.__init__(self)
        # LABEL SETUP
        style = self.style_combobox.format(
            _dark_one=dark_one,
            _text_foreground=text_foreground,
            _combo_border=combo_border
        )
        self.setMaximumWidth(200)
        self.setMinimumHeight(40)
        self.setStyleSheet(style)


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
        fig, self.ax = plt.subplots(figsize=(6, 5), dpi=100)
        super().__init__(fig)
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
            plt.title("Statistics Chart")
        elif self._name == "graph_statistics" and self._language == "es":
            plt.title("Gráfico de Estadísticas")
        elif self._name == "graph_metrics" and self._language == "en":
            plt.title("Metrics Chart")
        elif self._name == "graph_metrics" and self._language == "es":
            plt.title("Gráfico de Métricas")

        fig.patch.set_facecolor(self.bg_two)
        self.ax.set_facecolor(self.dark_three)
        self.ax.xaxis.label.set_color(self.axis_color)
        self.ax.yaxis.label.set_color(self.axis_color)
        self.ax.tick_params(axis='x', colors=self.axis_color)
        self.ax.tick_params(axis='y', colors=self.axis_color)
        self.ax.title.set_color(self.color_title)
        plt.tight_layout()

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
            if curr == "Statistics" or curr == "Estadisticas":
                if new_parameter in self._actual_list:
                    custom_df = self._data.iloc[:, :1]
                    custom_df = custom_df.join(
                        self._data[new_parameter]
                    )
                    custom_df.plot.bar(
                        x=custom_df.columns[0],
                        y=custom_df.columns[1],
                        ax=self.ax,
                        color=self.bar_color
                    )
                    plt.subplots_adjust(bottom=0.22)
                    plt.title(util_lists.stats_list[new_parameter], color=self.color_title, size=15)
                    self.ax.tick_params(axis='x', rotation=80)
                    plt.axhline(y=custom_df[new_parameter].mean(), color='r', linestyle='--')
                    plt.xlabel("")
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
            elif curr == "Metrics" or curr == "Metricas":
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
                    custom_df.plot.scatter(
                        x=custom_df.columns[1],
                        y=custom_df.columns[2],
                        ax=self.ax,
                        color=self.bar_color
                    )
                    plt.subplots_adjust(bottom=0.1)
                    self.ax.set_xlabel(util_lists.stats_list[custom_df.columns[1]], size=12)
                    self.ax.set_ylabel(util_lists.stats_list[custom_df.columns[2]], size=12)
                    plt.title(new_parameter, color=self.color_title, size=15)
                    plt.axhline(y=custom_df[custom_df.columns[2]].mean(), color='r', linestyle=':')
                    plt.axvline(x=custom_df[custom_df.columns[1]].mean(), color='r', linestyle=':')
                    cursor = mplcursors.cursor(hover=mplcursors.HoverMode.Transient)

                    @cursor.connect("add")
                    def on_add(sel):
                        try:
                            sel.annotation.set_text(
                                "{}\n{}: {:.2f}\n{}: {:.2f}".format(custom_df[custom_df.columns[0]][sel.index],
                                                                    util_lists.stats_list[custom_df.columns[1]],
                                                                    sel.target[0],
                                                                    util_lists.stats_list[custom_df.columns[2]],
                                                                    sel.target[1])
                            )
                            sel.annotation.get_bbox_patch().set(alpha=0.8)
                        except KeyError:
                            pass
                else:
                    self.ax.clear()
            plt.draw()
