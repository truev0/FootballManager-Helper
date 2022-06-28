# IMPORT PYSIDE CORE
# ///////////////////////////////////////////////////////////////
from pyside_core import *

# IMPORT MODULES
# ///////////////////////////////////////////////////////////////
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


# CLUSTERING WIDGET
# ///////////////////////////////////////////////////////////////
class PyClusteringWidget(QWidget):
    def __init__(
            self,
            language,
            parent=None,
            dark_one="#1b1e23",
            text_foreground="#8a95aa",
            bg_two="#343b48",
            dark_three="21252d",
            axis_color="f5f6f9",
            color_title="dce1ec"
    ):
        super().__init__(parent)
        self.language = language
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
        self.inner_layout = QHBoxLayout(self)
        self.inner_layout.setContentsMargins(0, 0, 0, 0)

        self.inner_chart = _PyCanvas(
            language=self.language,
            bg_two=bg_two,
            dark_three=dark_three,
            axis_color=axis_color,
            color_title=color_title
        )


        self.inner_layout.addWidget(self.inner_chart)

        self.right_frame = QFrame()
        self.right_frame.setFrameShape(QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.right_frame.setStyleSheet("background-color: #343b48; border-radius: 8px;")
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
        self.scroller_area_widget_content.setObjectName("scroller_area_widget_content")
        self.scroller_area_widget_content.setStyleSheet(
            "QLabel {font: 15pt; color: #dce1ec;}"
            "QLabel::hover {background-color: #21252d;}"
        )
        self.scroller_content_layout = QVBoxLayout(self.scroller_area_widget_content)
        self.scroller_content_layout.setContentsMargins(0, 0, 0, 0)

        self.scroller_area.setWidget(self.scroller_area_widget_content)

        self.right_layout.addWidget(self.scroller_area)

        self.inner_layout.addWidget(self.right_frame)

    def add_player_to_list(self, players):
        if self.scroller_area_widget_content.findChildren(QLabel):
            for i in range(len(self.scroller_area_widget_content.children())):
                item = self.scroller_area_widget_content.children()[i]
                if isinstance(item, QLabel):
                    self.scroller_content_layout.removeWidget(item)
                    item.deleteLater()

        for i in range(len(players)):
            label = QLabel(players[i], parent=self.scroller_area_widget_content)
            label.setMinimumHeight(50)
            label.setMaximumHeight(50)
            label.setAlignment(Qt.AlignCenter)
            self.scroller_content_layout.addWidget(label, i)


# PY CANVAS
# ///////////////////////////////////////////////////////////////
class _PyCanvas(FigureCanvas):
    def __init__(
            self,
            language,
            bg_two,
            dark_three,
            axis_color,
            color_title,
    ):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(6, 5))
        super().__init__(self.fig)
        # COLORS
        self.bg_two = bg_two
        self.dark_three = dark_three
        self.axis_color = axis_color
        self.color_title = color_title

        self.COLORS = {
            0: '#CF7175',
            1: '#E39C75',
            2: '#9A8EC2',
            3: '#77B986',
            4: '#708EBF',
        }

        self._language = language

        self.fig.patch.set_facecolor(self.bg_two)
        self.ax.set_facecolor(self.bg_two)
        self.ax.xaxis.label.set_color(self.axis_color)
        self.ax.yaxis.label.set_color(self.axis_color)
        self.ax.tick_params(axis='x', colors=self.axis_color)
        self.ax.tick_params(axis='y', colors=self.axis_color)
        self.ax.title.set_color(self.color_title)

    def update_chart(self, data, printable_names, player):
        self.ax.clear()
        texts = []
        self.ax.set_title("Clustering for players similar to " + player, fontsize=15, color=self.color_title)
        data.plot.scatter(
            x='x',
            y='y',
            ax=self.ax,
            c=data['cluster'].map(self.COLORS),
            s=100
        )
        self.ax.set(ylim=(-2, 2))
        for x, y, s in zip(
            data.x,
            data.y,
            data[data.columns[3]]
        ):
            if s in printable_names or s == player:
                texts.append(
                    self.ax.text(
                        x,
                        y,
                        s,
                        color=self.color_title
                    )
                )

        self.ax.set_xlabel('PC1', size=12, color=self.axis_color)
        self.ax.set_ylabel('PC2', size=12, color=self.axis_color)
        self.ax.grid(False)
        self.fig.canvas.draw()
