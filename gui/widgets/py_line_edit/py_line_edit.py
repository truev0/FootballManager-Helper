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
        event = self.change_letter(event)
        super().keyPressEvent(event)

    def change_letter(self, event):
        text = self.KEYS_MAPPING.get(event.text())
        if text is None:
            return event
        return QKeyEvent(event.type(), Qt.Key_unknown, event.modifiers(), text)
