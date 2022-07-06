# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
import matplotlib.pyplot as plt
import mplcursors

# IMPORT PROCESSING, CHART AND CLUSTERING MODULES
# ///////////////////////////////////////////////////////////////
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget

# IMPORT DICTS
# ///////////////////////////////////////////////////////////////
from gui.core.dicts import util_lists

# IMPORT PY COMBO BOX
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_combo_box.py_combo_box_widget import PyComboBox


# PY STATS WIDGET
# ///////////////////////////////////////////////////////////////
# It's a widget that displays a list of statistics
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
        bar_color="3f6fd1",
    ):
        """
        It creates a custom widget that contains a combo box and a canvas.

        The combo box is used to select the type of chart to be displayed.

        The canvas is used to display the chart.

        The canvas is updated when the combo box is changed.

        The canvas is also updated when the type of chart is changed.

        The canvas is updated by calling the update_chart function.

        The update_chart function is defined in the _CustomCanvas class.

        The update_chart function is called by the currentTextChanged signal of the combo box.

        The update_chart function is also called by the currentIndexChanged signal of the type selector.

        The update_chart function is also called by the update_dependent_combo function.

        The update_dependent_combo function is called by the currentIndexChanged signal of the type selector.

        :param name: The name of the chart
        :param language: The language of the chart
        :param parent: The parent widget of the chart
        :param dark_one: background color of the widget, defaults to #1b1e23 (optional)
        :param text_foreground: The color of the text in the combo boxes, defaults to #8a95aa (optional)
        :param combo_border: The border color of the combo boxes, defaults to #6c99f4 (optional)
        :param bg_two: background color of the chart, defaults to #343b48 (optional)
        :param dark_three: background color of the chart, defaults to 21252d (optional)
        :param axis_color: color of the axis, defaults to f5f6f9 (optional)
        :param color_title: The color of the title of the chart, defaults to dce1ec (optional)
        :param bar_color: The color of the bars in the chart, defaults to 3f6fd1 (optional)
        """
        super().__init__(parent)
        self.setStyleSheet(
            '''
            QScrollBar::vertical {
            border: none;
            background-color: #2c313c;
            width: 8px;
            margin: 21px 0 21px 0;
            border-radius: 0px;
            }
            QScrollBar::handle:vertical {
            background: #568af2;
            min-height: 25px;
            border-radius: 4px
            }
            QScrollBar::add-line:vertical {
            border: none;
            background: #272c36;
            height: 20px;
            border-bottom-left-radius: 4px;
            border-bottom-right-radius: 4px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
            }
            QScrollBar::sub-line:vertical {
            border: none;
            background: #272c36;
            height: 20px;
            border-top-left-radius: 4px;
            border-top-right-radius: 4px;
            subcontrol-position: top;
            subcontrol-origin: margin;
            }
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
            background: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
            }
            '''
        )
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
            combo_border=combo_border,
        )

        self.chart = _CustomCanvas(
            self,
            name=self.name,
            language=self.language,
            bg_two=bg_two,
            dark_three=dark_three,
            axis_color=axis_color,
            color_title=color_title,
            bar_color=bar_color,
        )

        self.principal_layout = QVBoxLayout(self)
        self.alter_layout = QHBoxLayout()
        self.alter_layout.addWidget(self.type_selector)
        self.alter_layout.addWidget(self.combo_selector)
        self.principal_layout.addLayout(self.alter_layout)
        self.principal_layout.addWidget(self.chart)

        self.type_selector.currentIndexChanged.connect(
            self.update_dependent_combo)
        self.update_dependent_combo(self.type_selector.currentIndex())

        self.combo_selector.currentTextChanged.connect(self.chart.update_chart)

    def update_dependent_combo(self, index):
        """
        The function clears the dependent combo box, then adds the items from the dependent list to the dependent
        combo box

        :param index: The index of the item that was selected
        """
        self.combo_selector.clear()
        dependent_list = self.type_selector.itemData(index)
        if dependent_list:
            self.combo_selector.addItems(dependent_list)


# It's a class to place graph
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
        """
        It's a function that creates a graph with a title, a background color, a color for the axis, a color for the
        title, and a color for the bars

        :param parent: The parent widget
        :param language: "en" or "es"
        :param name: The name of the graph
        :param bg_two: background color of the graph
        :param dark_three: dark background color
        :param axis_color: color of the axis
        :param color_title: color of the title
        :param bar_color: color of the bars
        """
        self.fig, self.ax = plt.subplots(1,
                                         dpi=100,
                                         figsize=(6, 5),
                                         sharey=True)
        super().__init__(self.fig)
        # COLORS
        self.bg_two = bg_two
        self.dark_three = dark_three
        self.axis_color = axis_color
        self.color_title = color_title
        self.bar_color = bar_color

        self._name = name
        self._language = language
        self._actual_list = [""]
        self._data = None
        self._parent = parent
        self.setParent(parent)
        if self._name == "graph_statistics" and self._language == "en":
            self.ax.set_title("Statistics Chart",
                              fontsize=15,
                              color=self.color_title)
        elif self._name == "graph_statistics" and self._language == "es":
            self.ax.set_title("Gráfico de Estadísticas",
                              fontsize=15,
                              color=self.color_title)
        elif self._name == "graph_metrics" and self._language == "en":
            self.ax.set_title("Metrics Chart",
                              fontsize=15,
                              color=self.color_title)
        elif self._name == "graph_metrics" and self._language == "es":
            self.ax.set_title("Gráfico de Métricas",
                              fontsize=15,
                              color=self.color_title)

        self.fig.patch.set_facecolor(self.bg_two)
        self.ax.set_facecolor(self.dark_three)
        self.ax.xaxis.label.set_color(self.axis_color)
        self.ax.yaxis.label.set_color(self.axis_color)
        self.ax.tick_params(axis="x", colors=self.axis_color)
        self.ax.tick_params(axis="y", colors=self.axis_color)
        self.ax.title.set_color(self.color_title)

    def count_actual_list(self):
        """
        It returns the length of the list of actual values
        :return: The length of the list.
        """
        return len(self._actual_list)

    def set_data(self, data):
        """
        Set the data attribute of the object to the value of the data parameter.

        :param data: The data to be plotted
        """
        self._data = data

    def add_to_list(self, e_list):
        """
        If the list is empty, add the first element of the list to be added. If the list is not empty, add all the elements
        of the list to be added

        :param e_list: a list of elements to be added to the list
        """
        if len(self._actual_list) == 1:
            self._actual_list[0] = e_list[0]
            if len(e_list) > 1:
                for i in range(1, len(e_list)):
                    self._actual_list.append(e_list[i])
        else:
            for e in e_list:
                self._actual_list.append(e)

    def change_language(self, new_lang):
        """
        Change_language() changes the language of the user to the new_lang argument.

        :param new_lang: The new language to change to
        """
        self._language = new_lang

    def update_chart(self, new_parameter):
        """
        It updates the chart with the new parameter selected by the user

        :param new_parameter: The parameter that is selected in the combobox
        """
        if self._data is not None:
            self.ax.clear()
            curr = self._parent.type_selector.currentText()
            if curr in ("Statistics", "Estadisticas"):
                if new_parameter in self._actual_list:
                    custom_df = self._data.iloc[:, :1]
                    custom_df = custom_df.join(self._data[new_parameter])

                    custom_df.plot.bar(
                        x=custom_df.columns[0],
                        y=custom_df.columns[1],
                        ax=self.ax,
                        color=self.bar_color,
                        legend=None,
                    )
                    self.fig.subplots_adjust(bottom=0.22)
                    if self._language == "en":
                        self.ax.set_title(
                            util_lists.stats_list_en[new_parameter],
                            fontsize=15,
                            color=self.color_title,
                        )
                    elif self._language == "es":
                        self.ax.set_title(
                            util_lists.stats_list_es[new_parameter],
                            fontsize=15,
                            color=self.color_title,
                        )

                    self.ax.tick_params(axis="x", rotation=80)
                    self.ax.axhline(y=custom_df[new_parameter].mean(),
                                    color="r",
                                    linestyle="--")
                    self.ax.set_xlabel("")
                    cursor = mplcursors.cursor(
                        hover=mplcursors.HoverMode.Transient)

                    @cursor.connect("add")
                    def on_add(sel):
                        try:
                            x, y, width, height = (
                                sel.artist[sel.index].get_bbox().bounds)
                            if ((x + width / 2) + 4) > len(custom_df):
                                sel.annotation.set(
                                    text=f"{custom_df[custom_df.columns[0]][sel.index]}"
                                         f": {height:g}",
                                    position=(-10, 0),
                                    anncoords="offset points",
                                )
                            else:
                                sel.annotation.set(
                                    text=f"{custom_df[custom_df.columns[0]][sel.index]}"
                                         f": {height:g}",
                                    position=(10, 0),
                                    anncoords="offset points",
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
                    custom_df = custom_df.join(self._data[[
                        util_lists.metrics_list[new_parameter][0],
                        util_lists.metrics_list[new_parameter][1],
                    ]])
                    tmp_x = custom_df.columns[1]
                    tmp_y = custom_df.columns[2]
                    custom_df.plot.scatter(x=tmp_x,
                                           y=tmp_y,
                                           ax=self.ax,
                                           color=self.bar_color,
                                           legend=None)
                    self.fig.subplots_adjust(bottom=0.1)
                    if self._language == "en":
                        self.ax.set_xlabel(util_lists.stats_list_en[tmp_x],
                                           size=12)
                        self.ax.set_ylabel(util_lists.stats_list_en[tmp_y],
                                           size=12)
                    elif self._language == "es":
                        self.ax.set_xlabel(util_lists.stats_list_es[tmp_x],
                                           size=12)
                        self.ax.set_ylabel(util_lists.stats_list_es[tmp_y],
                                           size=12)
                    self.ax.set_title(new_parameter,
                                      color=self.color_title,
                                      size=15)

                    self.ax.axhline(y=custom_df[tmp_y].mean(),
                                    color="r",
                                    linestyle=":")
                    self.ax.axvline(x=custom_df[tmp_x].mean(),
                                    color="r",
                                    linestyle=":")
                    cursor = mplcursors.cursor(
                        hover=mplcursors.HoverMode.Transient)

                    @cursor.connect("add")
                    def on_add(sel):
                        try:
                            if self._language == "en":
                                sel.annotation.set_text(
                                    "{}\n{}: {:.2f}\n{}: {:.2f}".format(
                                        custom_df[custom_df.columns[0]][
                                            sel.index],
                                        util_lists.stats_list_en[
                                            custom_df.columns[1]],
                                        sel.target[0],
                                        util_lists.stats_list_en[
                                            custom_df.columns[2]],
                                        sel.target[1],
                                    ))
                            elif self._language == "es":
                                sel.annotation.set_text(
                                    "{}\n{}: {:.2f}\n{}: {:.2f}".format(
                                        custom_df[custom_df.columns[0]][
                                            sel.index],
                                        util_lists.stats_list_es[
                                            custom_df.columns[1]],
                                        sel.target[0],
                                        util_lists.stats_list_es[
                                            custom_df.columns[2]],
                                        sel.target[1],
                                    ))
                            sel.annotation.get_bbox_patch().set(alpha=0.8)
                        except KeyError:
                            pass

                else:
                    self.ax.clear()
            self.ax.grid(False)
            self.fig.canvas.draw()
