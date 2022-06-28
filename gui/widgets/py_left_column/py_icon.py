# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

from PySide6.QtGui import QPixmap, QPainter

from PySide6.QtCore import Qt


# PY ICON WITH CUSTOM COLORS
# ///////////////////////////////////////////////////////////////
class PyIcon(QWidget):
    def __init__(
        self,
        icon_path,
        icon_color
    ):
        super().__init__()

        # PROPERTIES
        self._icon_path = icon_path
        self._icon_color = icon_color

        # SETUP UI
        self.setup_ui()

    def setup_ui(self):
        # LAYOUT
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # LABEL
        self.icon = QLabel()
        self.icon.setAlignment(Qt.AlignCenter)
        
        # PAINTER
        self.set_icon(self._icon_path, self._icon_color)

        # ADD TO LAYOUT
        self.layout.addWidget(self.icon)

    def set_icon(self, icon_path, icon_color=None):
        # GET COLOR
        if icon_color is not None:
            color = icon_color
        else:
            color = self._icon_color

        # PAINTER / PIXMAP
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)       
        painter.end()

        # SET PIXMAP
        self.icon.setPixmap(icon)
