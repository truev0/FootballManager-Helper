

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from pyside_core import *

# IMPORT MODULES
# ///////////////////////////////////////////////////////////////
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

graph = {
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
    'Ent Cl': 'Entradas Completadas',
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

# TODO continuar editando este widget
# PY STATS WIDGET
# ///////////////////////////////////////////////////////////////
class PyStatsWidget(QWidget):
    def __init__(
            self,
            language,
            parent=None,
            dark_one="#1b1e23",
            text_foreground="#8a95aa",
            combo_border="#6c99f4"
    ):
        super().__init__(parent)

        self.combo_selector = _QCustomCombo(
            dark_one=dark_one,
            text_foreground=text_foreground,
            combo_border=combo_border
        )
        self.combo_selector.addItem("Choose a stat")

        self.chart = _CustomCanvas(self)

        self.principal_layout = QVBoxLayout(self)
        self.alter_layout = QHBoxLayout()

        self.alter_layout.addWidget(self.combo_selector)
        self.principal_layout.addLayout(self.alter_layout)
        self.principal_layout.addWidget(self.chart)

        self.combo_selector.currentTextChanged.connect(
            self.chart.update_chart
        )


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
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(6, 5), dpi=100)
        super().__init__(fig)
        self._actual_list = ['']
        self._data = None
        self.setParent(parent)
        plt.title("Initial chart")
        # plt.show()
        fig.patch.set_facecolor('#343b48')  # BG TWO
        self.ax.set_facecolor('#21252d')  # Dark Three
        self.ax.tick_params(axis='x', colors='#f5f6f9')  # Icon active
        self.ax.tick_params(axis='y', colors='#f5f6f9')
        self.ax.title.set_color('#dce1ec')  # Text title
        plt.tight_layout()

    def set_data(self, data):
        self._data = data

    def get_head_list(self):
        return self._actual_list[0]

    def add_to_list(self, list):
        self._actual_list[0] = list[0]
        for i in range(1, len(list)):
            self._actual_list.append(list[i])

    def update_chart(self, new_parameter):
        self.ax.clear()
        if self._data is not None:
            custom_df = self._data[[self._actual_list[0], new_parameter]]
            if new_parameter in self._actual_list:
                custom_df.plot.bar(
                    x=self._actual_list[0],
                    y=new_parameter,
                    ax=self.ax,
                    color='#3f6fd1'  # Context pressed
                )
                plt.subplots_adjust(bottom=0.22)
                plt.title(graph[new_parameter], color='#dce1ec')
                self.ax.tick_params(axis='x', rotation=80)
                plt.axhline(y=custom_df[new_parameter].mean(), color='r', linestyle='--')
                plt.xlabel("")
                plt.draw()
            else:
                self.ax.clear()
