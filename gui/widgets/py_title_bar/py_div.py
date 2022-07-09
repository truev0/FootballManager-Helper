# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtWidgets import QWidget, QHBoxLayout, QFrame


# CUSTOM LEFT MENU
# ///////////////////////////////////////////////////////////////
class PyDiv(QWidget):
    """It's a widget that displays a division in title bar"""

    def __init__(self, color):
        """
        It creates a QFrame with a line in it, and then adds it to a QHBoxLayout

        :param color: The color of the line
        """
        super().__init__()

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 5, 0, 5)
        self.frame_line = QFrame()
        self.frame_line.setStyleSheet(f"background: {color};")
        self.frame_line.setMaximumWidth(1)
        self.frame_line.setMinimumWidth(1)
        self.layout.addWidget(self.frame_line)
        self.setMaximumWidth(20)
        self.setMinimumWidth(20)
