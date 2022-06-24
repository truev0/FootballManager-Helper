# IMPORT PYSIDE CORE
# ///////////////////////////////////////////////////////////
from pyside_core import *


# PY COMBO BOX
# ///////////////////////////////////////////////////////////
class PyComboBox(QComboBox):
    style_combobox = """ 
        QComboBox {{		
            background-color: {_dark_one};	
            color: {_text_foreground};
            border-radius: 4px;
            padding-left: 10px;
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
