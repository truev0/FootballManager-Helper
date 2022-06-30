# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import Qt

from PySide6.QtWidgets import QPushButton

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QPushButton {{
border: none;
padding-left: 10px;
padding-right: 5px;
color: {_color};
border-radius: {_radius};	
background-color: {_bg_color};
}}
QPushButton:hover {{
background-color: {_bg_color_hover};
}}
QPushButton:pressed {{	
background-color: {_bg_color_pressed};
}}
'''


# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyPushButton(QPushButton):
    def __init__(
            self,
            text,
            radius,
            color,
            bg_color,
            bg_color_hover,
            bg_color_pressed,
            parent=None,
            name=None
    ):
        super().__init__()

        # SET PARAMETRES
        self._name = name
        self.setText(text)
        if parent is not None:
            self.setParent(parent)
        self.setCursor(Qt.PointingHandCursor)

        # SET STYLESHEET
        custom_style = style.format(
            _color=color,
            _radius=radius,
            _bg_color=bg_color,
            _bg_color_hover=bg_color_hover,
            _bg_color_pressed=bg_color_pressed,
        )
        self.setStyleSheet(custom_style)

    def get_name(self):
        return self._name