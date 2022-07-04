# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtWidgets import QWidget, QHBoxLayout, QFrame, QLabel, \
    QSizePolicy, QSpacerItem

from PySide6.QtCore import Qt


# PY CREDITS BAR AND VERSION
# ///////////////////////////////////////////////////////////////
# This class is a widget that displays the credits for the Python version of the game.
class PyCredits(QWidget):
    def __init__(
        self,
        copyright_text,
        version,
        bg_two,
        font_family,
        text_size,
        text_description_color,
        radius=8,
        padding=10
    ):
        """
        The `__init__` function is a special function that is called when an object is created

        :param copyright_text: The text to display in the copyright section
        :param version: The version of the software
        :param bg_two: The background color of the second row of the footer
        :param font_family: The font family to use for the text
        :param text_size: The size of the text
        :param text_description_color: The color of the text
        :param radius: The radius of the rounded corners of the widget, defaults to 8 (optional)
        :param padding: The padding around the text, defaults to 10 (optional)
        """
        super().__init__()

        # PROPERTIES
        self._copyright = copyright_text
        self._version = version
        self._bg_two = bg_two
        self._font_family = font_family
        self._text_size = text_size
        self._text_description_color = text_description_color
        self._radius = radius
        self._padding = padding

        # SETUP UI
        self.setup_ui()

    def setup_ui(self):
        """It sets up the UI of the widget"""
        # ADD LAYOUT
        self.widget_layout = QHBoxLayout(self)
        self.widget_layout.setContentsMargins(0, 0, 0, 0)

        # BG STYLE
        style = f"""
        #bg_frame {{
            border-radius: {self._radius}px;
            background-color: {self._bg_two};
        }}
        .QLabel {{
            font: {self._text_size}pt "{self._font_family}";
            color: {self._text_description_color};
            padding-left: {self._padding}px;
            padding-right: {self._padding}px;
        }}
        """

        # BG FRAME
        self.bg_frame = QFrame()
        self.bg_frame.setObjectName("bg_frame")
        self.bg_frame.setStyleSheet(style)

        # ADD TO LAYOUT
        self.widget_layout.addWidget(self.bg_frame)

        # ADD BG LAYOUT
        self.bg_layout = QHBoxLayout(self.bg_frame)
        self.bg_layout.setContentsMargins(0, 0, 0, 0)

        # ADD COPYRIGHT TEXT
        self.copyright_label = QLabel(self._copyright)
        self.copyright_label.setAlignment(Qt.AlignVCenter)

        # ADD VERSION TEXT
        self.version_label = QLabel(self._version)
        self.version_label.setAlignment(Qt.AlignVCenter)

        # SEPARATOR
        self.separator = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # ADD TO LAYOUT
        self.bg_layout.addWidget(self.copyright_label)
        self.bg_layout.addSpacerItem(self.separator)
        self.bg_layout.addWidget(self.version_label)
