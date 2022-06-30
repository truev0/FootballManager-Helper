# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtWidgets import QWidget, QHBoxLayout, QFrame


# CUSTOM LEFT MENU
# ///////////////////////////////////////////////////////////////
# It's a widget that displays a division problem and allows the user to enter an answer
class PyDiv(QWidget):
    def __init__(self, color):
        """
        It creates a horizontal layout, adds a frame to it, sets the frame's background color, sets the frame's maximum and
        minimum height, and then adds the layout to the widget

        :param color: The color of the line
        """
        super().__init__()

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(5, 0, 5, 0)
        self.frame_line = QFrame()
        self.frame_line.setStyleSheet(f"background: {color};")
        self.frame_line.setMaximumHeight(1)
        self.frame_line.setMinimumHeight(1)
        self.layout.addWidget(self.frame_line)
        self.setMaximumHeight(1)
