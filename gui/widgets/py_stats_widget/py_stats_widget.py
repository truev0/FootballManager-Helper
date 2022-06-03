

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from pyside_core import *

# IMPORT MODULES
# ///////////////////////////////////////////////////////////////
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import pandas as pd

style = '''
QComboBox {{
border: 1px solid #ced4da;
border-radius: 4px;
padding-left: 10px;
}}

'''
# TODO continuar editando este widget
# PY STATS WIDGET
# ///////////////////////////////////////////////////////////////
class PyStatsWidget(QWidget):
    def __init__(
            self,
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


        self.fig, self.ax = plt.subplots()
        self.figure_widget = FigureCanvas(self.fig)
        plt.tight_layout()

        self.principal_layout = QVBoxLayout(self)
        self.alter_layout = QHBoxLayout()

        self.alter_layout.addWidget(self.combo_selector)
        self.principal_layout.addLayout(self.alter_layout)
        self.principal_layout.addWidget(self.figure_widget)


class _QCustomCombo(QComboBox):
    style_combobox = """ 
        QComboBox {{		
            background-color: {_dark_one};	
            color: {_text_foreground};
            padding-left: 40px;
            border-radius: 4px;
            border: 1px solid {_combo_border};
            font: 800 9pt "Segoe UI";
        }}
        
        QComboBox:on {{
            border: 4px solid #c2dbfe;
        }}
        
        QComboBox QListView {{
            font-size: 12px;
            border: 1px solid rgba(0, 0, 0, 10%);
            padding: 5px;
            background-color: #fff;
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

