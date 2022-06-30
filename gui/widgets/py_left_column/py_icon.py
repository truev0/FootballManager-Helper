# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


# PY ICON WITH CUSTOM COLORS
# ///////////////////////////////////////////////////////////////
# It's a widget that displays an icon
class PyIcon(QWidget):

    def __init__(self, icon_path, icon_color):
        """
        The function __init__() is a special function in Python classes. It is run as soon as an object of a class is
        instantiated. The method is useful to do any initialization you want to do with your object

        :param icon_path: The path to the icon image
        :param icon_color: The color of the icon
        """
        super().__init__()

        # PROPERTIES
        self._icon_path = icon_path
        self._icon_color = icon_color

        # SETUP UI
        self.setup_ui()

    def setup_ui(self):
        """
        It creates a QLabel, sets its alignment, sets its icon, and adds it to the layout
        """
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
        """
        It takes an icon path, and a color, and returns a new icon with the color applied

        :param icon_path: The path to the icon you want to use
        :param icon_color: The color of the icon
        """
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
