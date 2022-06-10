

# IMPORT PYSIDE CORE
# ///////////////////////////////////////////////////////////////
import pandas as pd

from pyside_core import *

# IMPORT PYQTGRAPH
# ///////////////////////////////////////////////////////////////
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
import numpy as np

# IMPORT MODULES
# ///////////////////////////////////////////////////////////////
import plotly.offline as pyo
import plotly.graph_objects as go


stats_list = {
    'Mins': 'Minutes',
    'Svt': 'Saves Tipped',
    'Svp': 'Saves Parried',
    'Svh': 'Saves Held',
    'Conc': 'Conceded',
    'Pas %': '% Passes',
    'Ps C/90': "Completed Passes / 90'",
    'K Tck': 'Key Tackles',
    'Tck R': 'Tackles Ratio',
    'Int/90': 'Interceptions / 90',
    'Hdr %': '% Headers',
    'Hdrs W/90': 'Headers Won / 90',
    'Fls': 'Fouls',
    'K Ps/90': 'Key Passes / 90',
    'Ch C/90': 'Chances Created / 90',
    'Gls/90': 'Goals / 90',
    'Shot %': '% Shots',
    'Drb/90': 'Dribbles / 90',
    'Shot/90': 'Shots / 90',
    'Cr C/A': 'Crosses Completed vs Attempts',
    'ShT/90': 'Shots on Target / 90',
    'Dist/90': 'Distance Covered / 90',
    'Gls': 'Goals',
    'Ast': 'Assits',
    'Tall': 'Team allowed',
    'Tcon/90': 'Team conceded / 90',
    'Ps A/90': 'Passes Attempted / 90',
    'Pens S': 'Penalties Scored',
    'Av Rat': 'Average Rating',
    'Min': 'Minutos',
    'BDs': 'Translate 1',
    'BRe': 'Translate 2',
    'BAt': 'Translate 3',
    'Enc': 'Encajados',
    '% Pase': '% Pases',
    'Ps C/90': 'Pases Completados / 90',
    'Ent Cl': 'Entradas Clave',
    'Ent P': 'Promedio Entradas',
    'Rob/90': 'Robos / 90',
    'Rcg %': '% Cabezazos',
    'Cab G/90': 'Cabezazos Ganados / 90',
    'FC': 'Faltas Cometidas',
    'Pas Clv/90': 'Pases Clave / 90',
    'Oc C/90': 'Ocasiones Creadas / 90',
    'Gol/90': 'Goles / 90',
    'Asis/90': 'Asistencias / 90',
    '% disparos': '% Disparos',
    'Reg/90': 'Regates / 90',
    'Tir/90': 'Tiros / 90',
    'Cen.C/I': 'Centros Completados vs Intentados',
    'Cen.Com': 'Centros Completados',
    'TirP/90': 'Tiros a puerta / 90',
    'Dist/90': 'Distancia Recorrida / 90',
    'Gol': 'Goles',
    'Asis': 'Asistencias',
    'EnEq': 'Encajados Equipo',
    'EnEq/90': 'Encajados Equipo / 90',
    'Ps I/90': 'Pases Intentados / 90',
    'Pen M': 'Penalties Marcados',
    'Media': 'Media'
}

metrics_list = {
    "Ground Duels": ("Tck R", "Int/90")
}


# PY GRAPH WIDGET
# ///////////////////////////////////////////////////////////////
class PyGraphWidget(QWidget):

    def __init__(
            self,
            name,
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

        # COLORS FOR CHART
        self.bg_two = bg_two
        self.dark_three = dark_three
        self.axis_color = axis_color
        self.color_title = color_title
        self.bar_color = bar_color


        self.x_val = None
        self.usable_x_ticks = None
        self.x_ticks = None
        self._data = None
        self._actual_list = ['']
        self.isFirst = True

        self.name = name
        self.combo_selector = _QCustomCombo(
            dark_one=dark_one,
            text_foreground=text_foreground,
            combo_border=combo_border
        )

        if self.name == "graph_statistics":
            self.combo_selector.addItem("Choose a stat")
        elif self.name == "graph_metrics":
            self.combo_selector.addItem("Choose a metric")

        self.bottom_frame = QFrame()
        self.bottom_frame.setStyleSheet("background-color: red;")
        self.bottom_frame_layout = QHBoxLayout(self.bottom_frame)
        self.bottom_frame_layout.setContentsMargins(2, 2, 2, 2)

        self.graph_view = pg.plot()
        self.graph_view.setBackground(self.bg_two)
        self.graph_view.showGrid(x=True, y=True)
        axis_style = {'color': self.axis_color}

        self.bottom_frame_layout.addWidget(self.graph_view)

        self.principal_layout = QVBoxLayout(self)
        self.top_layout = QHBoxLayout()

        self.top_layout.addWidget(self.combo_selector)
        self.principal_layout.addLayout(self.top_layout)
        self.principal_layout.addWidget(self.bottom_frame)
        self.combo_selector.currentTextChanged.connect(
            self.update_graph
        )

    def set_data(self, data):
        self._data = data

    def add_to_list(self, main_list):
        self._actual_list[0] = main_list[0]
        if len(main_list) > 1:
            for i in range(1, len(main_list)):
                self._actual_list.append(main_list[i])

        self.x_ticks = self._data[self._actual_list[0]].values.tolist()
        self.x_val = list(range(1, len(self.x_ticks) + 1))
        self.create_ticks()

    def create_ticks(self):
        self.usable_x_ticks = []
        for i, item in enumerate(self.x_ticks):
            self.usable_x_ticks.append(
                (
                    self.x_val[i],
                    item
                )
            )

    def update_graph(self, new_parameter):
        mean_list = []
        self.graph_view.clear()
        self.graph_view.setTitle(stats_list[new_parameter], color=self.color_title, size="20pt")
        if self._data is not None:
            values = self._data[new_parameter].values.tolist()
            mean_value = self._data[new_parameter].mean()
            if new_parameter in self._actual_list:
                bargraph = _QBarGraph(
                    x=self.x_val,
                    height=values,
                    width=0.5,
                    brush=self.bar_color
                )
                for i in range(len(values)):
                    mean_list.append(mean_value)
                self.graph_view.addItem(bargraph)
                self.graph_view.plot(self.x_val, mean_list, pen='r')
            self.graph_view.setXRange(0, len(self.x_val))
            self.graph_view.setYRange(0, values[values.index(max(values)) + 1])
            # ax = self.graph_view.getAxis("bottom")
            # ax.setTicks([self.usable_x_ticks])


class _QCustomCombo(QComboBox):
    style_combobox = """ 
        QComboBox {{		
            background-color: {_dark_one};	
            color: {_text_foreground};
            padding-left: 20px;
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
            combo_border,
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


class _QBarGraph(pg.BarGraphItem):
    def __init__(self, *args, **kwargs):
        pg.BarGraphItem.__init__(self, *args, **kwargs)
        self.setAcceptHoverEvents(True)

    # def hoverEnterEvent(self, event):
    #     print(self.toolTip())

    def mouseClickEvent(self, event):
        print("Clicked")

########## WIDGET WITH PYQTGRAPH ##########