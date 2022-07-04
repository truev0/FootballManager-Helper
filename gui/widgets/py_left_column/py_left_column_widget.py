# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QWidget, \
    QVBoxLayout

from PySide6.QtCore import Signal, Qt

# IMPORT CLOSE BUTTON
# ///////////////////////////////////////////////////////////////
from .py_left_button_widget import PyLeftButton

# IMPORT ICON
# ///////////////////////////////////////////////////////////////
from .py_icon import PyIcon

# IMPORT LEFT COLUMN
# ///////////////////////////////////////////////////////////////
from gui.uis.columns.ui_left_column import Ui_LeftColumn


# This class is a subclass of QWidget that creates a left column of buttons for the Python tab.
class PyLeftColumn(QWidget):
    # SIGNALS
    clicked = Signal(object)
    released = Signal(object)

    def __init__(
            self,
            parent,
            app_parent,
            text_title,
            text_title_size,
            text_title_color,
            dark_one,
            bg_color,
            btn_color,
            btn_color_hover,
            btn_color_pressed,
            icon_path,
            icon_color,
            icon_color_hover,
            icon_color_pressed,
            context_color,
            icon_close_path,
            radius=8
    ):
        """
              This function is the constructor for the class LeftColumn

              :param parent: The parent widget of the window
              :param app_parent: The parent of the application
              :param text_title: The text that will be displayed on the title bar
              :param text_title_size: The size of the text in the title bar
              :param text_title_color: The color of the text in the title bar
              :param dark_one: This is a boolean value that determines whether the window is dark or light
              :param bg_color: The background color of the menu
              :param btn_color: The color of the button when it's not being hovered over or pressed
              :param btn_color_hover: The color of the button when the mouse is hovering over it
              :param btn_color_pressed: The color of the button when it's pressed
              :param icon_path: The path to the icon you want to use for the button
              :param icon_color: The color of the icon when the button is not being hovered over or pressed
              :param icon_color_hover: The color of the icon when the mouse is hovering over it
              :param icon_color_pressed: The color of the icon when the button is pressed
              :param context_color: The color of the context menu
              :param icon_close_path: The path to the icon you want to use for the close button
              :param radius: The radius of the rounded corners of the window, defaults to 8 (optional)
              """
        super().__init__()

        # PARAMETERS
        self._parent = parent
        self._app_parent = app_parent
        self._text_title = text_title
        self._text_title_size = text_title_size
        self._text_title_color = text_title_color
        self._icon_path = icon_path
        self._dark_one = dark_one
        self._bg_color = bg_color
        self._btn_color = btn_color
        self._btn_color_hover = btn_color_hover
        self._btn_color_pressed = btn_color_pressed
        self._icon_color = icon_color
        self._icon_color_hover = icon_color_hover
        self._icon_color_pressed = icon_color_pressed
        self._context_color = context_color
        self._icon_close_path = icon_close_path
        self._radius = radius

        # SETUP UI
        self.setup_ui()

        # ADD LEFT COLUMN TO BG FRAME
        self.menus = Ui_LeftColumn()
        self.menus.setupUi(self.content_frame)

        # CONNECT SIGNALS
        self.btn_close.clicked.connect(self.btn_clicked)
        self.btn_close.released.connect(self.btn_released)

    # TITLE LEFT COLUMN EMIT SIGNALS
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        """The function is called when the button is clicked"""
        self.clicked.emit(self.btn_close)

    def btn_released(self):
        """The function is called when the button is released"""
        self.released.emit(self.btn_close)

    # WIDGETS
    # ///////////////////////////////////////////////////////////////
    def setup_ui(self):
        """It sets the interface for left column"""
        # BASE LAYOUT
        self.base_layout = QVBoxLayout(self)
        self.base_layout.setContentsMargins(0, 0, 0, 0)
        self.base_layout.setSpacing(0)

        # TITLE FRAME
        # ///////////////////////////////////////////////////////////////
        self.title_frame = QFrame()
        self.title_frame.setMaximumHeight(47)
        self.title_frame.setMinimumHeight(47)

        # TITLE BASE LAYOUT
        self.title_base_layout = QVBoxLayout(self.title_frame)
        self.title_base_layout.setContentsMargins(5, 3, 5, 3)

        # TITLE BG
        self.title_bg_frame = QFrame()
        self.title_bg_frame.setObjectName("title_bg_frame")
        self.title_bg_frame.setStyleSheet(f'''
        #title_bg_frame {{
            background-color: {self._bg_color};
            border-radius: {self._radius}px;
        }}
        ''')

        # LAYOUT TITLE BG
        self.title_bg_layout = QHBoxLayout(self.title_bg_frame)
        self.title_bg_layout.setContentsMargins(5, 5, 5, 5)
        self.title_bg_layout.setSpacing(3)

        # ICON
        self.icon_frame = QFrame()
        self.icon_frame.setFixedSize(30, 30)
        self.icon_frame.setStyleSheet("background: none;")
        self.icon_layout = QVBoxLayout(self.icon_frame)
        self.icon_layout.setContentsMargins(0, 0, 0, 0)
        self.icon_layout.setSpacing(5)
        self.icon = PyIcon(self._icon_path, self._icon_color)
        self.icon_layout.addWidget(self.icon, Qt.AlignCenter, Qt.AlignCenter)

        # LABEL
        self.title_label = QLabel(self._text_title)
        self.title_label.setObjectName("title_label")
        self.title_label.setStyleSheet(f'''
        #title_label {{
            font-size: {self._text_title_size}pt;
            color: {self._text_title_color};
            padding-bottom: 2px;
            background: none;
        }}
        ''')

        # BTN FRAME
        self.btn_frame = QFrame()
        self.btn_frame.setFixedSize(30, 30)
        self.btn_frame.setStyleSheet("background: none;")
        # CLOSE BUTTON
        self.btn_close = PyLeftButton(
            self._parent,
            self._app_parent,
            tooltip_text="Hide",
            dark_one=self._dark_one,
            bg_color=self._btn_color,
            bg_color_hover=self._btn_color_hover,
            bg_color_pressed=self._btn_color_pressed,
            icon_color=self._icon_color,
            icon_color_hover=self._icon_color_hover,
            icon_color_pressed=self._icon_color_pressed,
            icon_color_active=self._icon_color_pressed,
            context_color=self._context_color,
            text_foreground=self._text_title_color,
            icon_path=self._icon_close_path,
            radius=6,
        )
        self.btn_close.setParent(self.btn_frame)
        self.btn_close.setObjectName("btn_close_left_column")

        # ADD TO TITLE LAYOUT
        self.title_bg_layout.addWidget(self.icon_frame)
        self.title_bg_layout.addWidget(self.title_label)
        self.title_bg_layout.addWidget(self.btn_frame)

        # ADD TITLE BG TO LAYOUT
        self.title_base_layout.addWidget(self.title_bg_frame)

        # CONTENT FRAME
        # ///////////////////////////////////////////////////////////////
        self.content_frame = QFrame()
        self.content_frame.setStyleSheet("background: none")

        # ADD TO LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.base_layout.addWidget(self.title_frame)
        self.base_layout.addWidget(self.content_frame)
