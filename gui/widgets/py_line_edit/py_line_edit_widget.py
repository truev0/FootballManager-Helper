# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtWidgets import QLineEdit

from PySide6.QtCore import Qt

from PySide6.QtGui import QKeyEvent

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QLineEdit {{
background-color: {_bg_color_active};
border-radius: {_radius}px;
border: {_border_size}px solid transparent;
padding-left: 10px;
padding-right: 10px;
selection-color: {_selection_color};
selection-background-color: {_context_color};
color: {_color};
}}
QLineEdit:focus {{
border: {_border_size}px solid {_context_color};
background-color: {_bg_color_active};
}}
'''


# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyLineEdit(QLineEdit):
    """It's a custom QLineEdit that can be used in Python"""

    def __init__(
            self,
            text="",
            place_holder_text="",
            radius=8,
            border_size=2,
            color="#FFF",
            selection_color="#FFF",
            bg_color_active="#1b1e23",
            context_color="#00ABE8",
    ):
        """
        It sets the stylesheet for the QLineEdit widget

        :param text: The text that will be displayed in the line edit
        :param place_holder_text: The text that will be displayed when the line edit is empty
        :param radius: The radius of the border, defaults to 8 (optional)
        :param border_size: The size of the border around the text field, defaults to 2 (optional)
        :param color: The color of the text, defaults to #FFF (optional)
        :param selection_color: The color of the text when it's selected, defaults to #FFF (optional)
        :param bg_color_active: The background color of the text field when it's active, defaults to #1b1e23 (optional)
        :param context_color: The color of the context menu (right click menu), defaults to #00ABE8 (optional)
        """
        super().__init__()
        self.KEYS_MAPPING = {
            ".": ","
        }
        # PARAMETERS
        if text:
            self.setText(text)
        if place_holder_text:
            self.setPlaceholderText(place_holder_text)

        # SET STYLESHEET
        self.set_stylesheet(
            radius,
            border_size,
            color,
            selection_color,
            bg_color_active,
            context_color
        )

    # SET STYLESHEET
    def set_stylesheet(
            self,
            radius,
            border_size,
            color,
            selection_color,
            bg_color_active,
            context_color
    ):
        """
        > This function takes in a bunch of arguments and applies them to the stylesheet

        :param radius: The radius of the corners of the button
        :param border_size: The size of the border around the button
        :param color: The color of the button
        :param selection_color: The color of the selected item
        :param bg_color_active: The background color of the active tab
        :param context_color: The color of the context menu
        """
        # APPLY STYLESHEET
        style_format = style.format(
            _radius=radius,
            _border_size=border_size,
            _color=color,
            _selection_color=selection_color,
            _bg_color_active=bg_color_active,
            _context_color=context_color
        )
        self.setStyleSheet(style_format)

    def keyPressEvent(self, event):
        """
        It takes a QKeyEvent, changes the letter to the one you want, and then passes it to the parent class

        :param event: The event that was triggered
        """
        event = self.change_letter(event)
        super().keyPressEvent(event)

    def change_letter(self, event):
        """
        It takes a QKeyEvent, and if the key pressed is a letter, it returns a new QKeyEvent with the same type, modifiers,
        and key, but with the text of the key changed to the text of the key in the KEYS_MAPPING dictionary

        :param event: The event that was triggered
        :return: The key event is being returned.
        """
        text = self.KEYS_MAPPING.get(event.text())
        if text is None:
            return event
        return QKeyEvent(event.type(), Qt.Key_unknown, event.modifiers(), text)
