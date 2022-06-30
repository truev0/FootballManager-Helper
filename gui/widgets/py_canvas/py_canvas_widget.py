# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
import matplotlib.pyplot as plt

# IMPORT MODULES
# ///////////////////////////////////////////////////////////////
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)


# CLUSTERING WIDGET
# ///////////////////////////////////////////////////////////////
# This class is a widget that contains a Graphic of clustering
class PyClusteringWidget(QWidget):

    def __init__(
        self,
        language,
        parent=None,
        bg_two="#343b48",
        dark_three="21252d",
        axis_color="f5f6f9",
        color_title="dce1ec",
    ):
        """
        It creates a scrollable area on the right side of the chart, and the chart is on the left side

        :param language: The language of the chart
        :param parent: The parent widget
        :param bg_two: background color of the chart, defaults to #343b48 (optional)
        :param dark_three: background color of the chart, defaults to 21252d (optional)
        :param axis_color: color of the axis, defaults to f5f6f9 (optional)
        :param color_title: The color of the title of the chart, defaults to dce1ec (optional)
        """
        super().__init__(parent)
        self.language = language
        self.setStyleSheet("""
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
            """)
        self.inner_layout = QHBoxLayout(self)
        self.inner_layout.setContentsMargins(0, 0, 0, 0)

        self.inner_chart = _PyCanvas(
            language=self.language,
            bg_two=bg_two,
            dark_three=dark_three,
            axis_color=axis_color,
            color_title=color_title,
        )

        self.inner_layout.addWidget(self.inner_chart)

        self.right_frame = QFrame()
        self.right_frame.setFrameShape(QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.right_frame.setStyleSheet(
            "background-color: #343b48; border-radius: 8px;")
        self.right_frame.setMaximumWidth(300)
        self.right_layout = QHBoxLayout(self.right_frame)
        self.right_layout.setContentsMargins(0, 0, 0, 0)

        self.scroller_area = QScrollArea()
        self.scroller_area.setObjectName("scroller_area")
        self.scroller_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroller_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroller_area.setStyleSheet("border-radius: 8px;")
        self.scroller_area.setWidgetResizable(True)
        self.scroller_area_widget_content = QWidget()
        self.scroller_area_widget_content.setObjectName(
            "scroller_area_widget_content")
        self.scroller_area_widget_content.setStyleSheet(
            "QLabel {font: 15pt; color: #dce1ec;}"
            "QLabel::hover {background-color: #21252d;}")
        self.scroller_content_layout = QVBoxLayout(
            self.scroller_area_widget_content)
        self.scroller_content_layout.setContentsMargins(0, 0, 0, 0)

        self.scroller_area.setWidget(self.scroller_area_widget_content)

        self.right_layout.addWidget(self.scroller_area)

        self.inner_layout.addWidget(self.right_frame)

    def add_player_to_list(self, players):
        """
        It removes all the QLabels from the scroller_area_widget_content and then adds new ones based on the
        players list

        :param players: list of strings
        """
        if self.scroller_area_widget_content.findChildren(QLabel):
            for i in range(len(self.scroller_area_widget_content.children())):
                item = self.scroller_area_widget_content.children()[i]
                if isinstance(item, QLabel):
                    self.scroller_content_layout.removeWidget(item)
                    item.deleteLater()

        for i, item in enumerate(players):
            label = QLabel(item,
                           parent=self.scroller_area_widget_content)
            label.setMinimumHeight(50)
            label.setMaximumHeight(50)
            label.setAlignment(Qt.AlignCenter)
            self.scroller_content_layout.addWidget(label, i)


# PY CANVAS
# ///////////////////////////////////////////////////////////////
# It's a FigureCanvas that
# can be embedded in a wxPython application
class _PyCanvas(FigureCanvas):
    def __init__(
        self,
        language,
        bg_two,
        dark_three,
        axis_color,
        color_title,
    ):
        """
        Initialize Figure Canvas for the chart

        :param language: The language of the plot
        :param bg_two: background color
        :param dark_three: the background color of the graph
        :param axis_color: The color of the axis labels and ticks
        :param color_title: The color of the title
        """
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(6, 5))
        super().__init__(self.fig)
        # COLORS
        self.bg_two = bg_two
        self.dark_three = dark_three
        self.axis_color = axis_color
        self.color_title = color_title

        self.COLORS = {
            0: "#CF7175",
            1: "#E39C75",
            2: "#9A8EC2",
            3: "#77B986",
            4: "#708EBF",
        }

        self._language = language

        self.fig.patch.set_facecolor(self.bg_two)
        self.ax.set_facecolor(self.bg_two)
        self.ax.xaxis.label.set_color(self.axis_color)
        self.ax.yaxis.label.set_color(self.axis_color)
        self.ax.tick_params(axis="x", colors=self.axis_color)
        self.ax.tick_params(axis="y", colors=self.axis_color)
        self.ax.title.set_color(self.color_title)

    def update_chart(self, data, printable_names, player):
        """
        It takes a dataframe, a list of names to print, and a player name, and it plots the dataframe with the names
        in the list printed on the chart

        :param data: the dataframe with the data to plot
        :param printable_names: list of names to be printed on the chart
        :param player: The name of the player to be clustered
        """
        self.ax.clear()
        texts = []
        if self._language == "en":
            self.ax.set_title(
                "Clustering for players similar to " + player,
                fontsize=15,
                color=self.color_title,
            )
        elif self._language == "es":
            self.ax.set_title(
                "Clusters con jugadores similares a " + player,
                fontsize=15,
                color=self.color_title,
            )
        data.plot.scatter(x="x",
                          y="y",
                          ax=self.ax,
                          c=data["cluster"].map(self.COLORS),
                          s=100)
        self.ax.set(ylim=(-2, 2))
        for x, y, s in zip(data.x, data.y, data[data.columns[3]]):
            if s in printable_names or s == player:
                texts.append(self.ax.text(x, y, s, color=self.color_title))

        self.ax.set_xlabel("PC1", size=12, color=self.axis_color)
        self.ax.set_ylabel("PC2", size=12, color=self.axis_color)
        self.ax.grid(False)
        self.fig.canvas.draw()

    def change_language(self, new_language):
        """
        This function changes the language of the user to the new language.

        :param new_language: The new language to change to
        """
        self._language = new_language
