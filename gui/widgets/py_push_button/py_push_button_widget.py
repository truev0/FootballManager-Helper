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
# It's a QPushButton that can be connected to a Python function
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
        """
        The function takes in a bunch of parameters, sets them, and then sets the style sheet

        :param text: The text that will be displayed on the button
        :param radius: The radius of the button's corners
        :param color: the color of the text
        :param bg_color: The background color of the button when it's not being hovered over or pressed
        :param bg_color_hover: The background color of the button when the mouse is hovering over it
        :param bg_color_pressed: The background color of the button when it is pressed
        :param parent: The parent widget of the button
        :param name: The name of the button
        """
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
        """
        The function get_name() returns the value of the private variable _name
        :return: The name of the person.
        """
        return self._name
