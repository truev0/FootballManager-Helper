# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import QRect, QSize, Qt, Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QPushButton, QSizePolicy, QWidget

# IMPORT FUNCTIONS
# ///////////////////////////////////////////////////////////////
from gui.core.functions import set_svg_icon

# IMPORT BUTTONS
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_player_button.py_player_button_widget import PyPlayerButton

# PY VERTICAL PITCH


class PyVerticalPitch(QWidget):
    """This class is a widget that displays a vertical pitch"""

    # SIGNALS
    clicked = Signal(object)
    released = Signal(object)

    def __init__(
        self,
        parent=None,
        image_path="icon_player_identifier.svg",
        minimum_width=550,
        minimum_height=820,
    ):
        """
        The function `__init__` is a special function that is called when an object is created. It is used to initialize
        the object

        :param parent: The parent widget of the dialog
        :param image_path: The path to the image that will be displayed in the window, defaults to
        icon_player_identifier.svg (optional)
        :param minimum_width: The minimum width of the window, defaults to 550 (optional)
        :param minimum_height: The minimum height of the window, defaults to 820 (optional)
        """
        super().__init__()

        # PROPERTIES
        # ///////////////////////////////////////////////////////////////
        self.btn = None
        self._pitch_image = None
        self._image_player = image_path
        self._minimum_width = minimum_width
        self._minimum_height = minimum_height

        # SET PARENT
        self._parent = parent

        # SETUP WIDGETS
        self.setup_ui()

    # SETUP UI
    # ///////////////////////////////////////////////////////////////
    def setup_ui(self):
        """The function sets up the interface for the pitch"""
        self._pitch_image = QLabel(self._parent)
        self._pitch_image.setObjectName("pitch_image")
        self._pitch_image.setGeometry(
            QRect(0, 0, self._minimum_width, self._minimum_height))
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self._pitch_image.sizePolicy().hasHeightForWidth())
        self._pitch_image.setSizePolicy(size_policy)
        self._pitch_image.setMinimumSize(
            QSize(self._minimum_width, self._minimum_height))
        self._pitch_image.setPixmap(
            QPixmap("gui/images/png_images/vertical_pitch.png"))
        self._pitch_image.setScaledContents(True)
        self._pitch_image.setAlignment(Qt.AlignCenter)
        self._pitch_image.raise_()

    # PITCH EMIT SIGNALS
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        """The function btn_clicked is called when the button is clicked"""
        self.clicked.emit(self.btn)

    def btn_released(self):
        """The function btn_released is a function that emits a signal when a button is released"""
        self.released.emit(self.btn)

    # ADD BUTTON TO PITCH
    # Add btns and emit signals
    # ///////////////////////////////////////////////////////////////
    def add_btns(self, parameters):
        """
        It creates a button, sets its geometry, connects it to a function, and then adds it to a list

        :param parameters: [
        """
        if parameters is not None:
            for parameter in parameters:
                _btn_id = parameter["btn_id"]
                _is_active = parameter["is_active"]
                _pos_x = parameter["posX"]
                _pos_y = parameter["posY"]
                _size = parameter["size"]

                self.btn = PyPlayerButton(
                    self._parent,
                    icon_path=set_svg_icon(self._image_player),
                    btn_id=_btn_id,
                    is_active=_is_active,
                )
                self.btn.setGeometry(QRect(_pos_x, _pos_y, _size, _size))
                self.btn.clicked.connect(self.btn_clicked)
                self.btn.released.connect(self.btn_released)

    # SELECT ONLY ONE BTN
    # ///////////////////////////////////////////////////////////////
    def select_only_one(self, widget: str):
        """
        It takes a string as an argument, and then finds all the QPushButtons in the current window, and if the button's
        object name matches the string passed to the function, it sets that button to active, and all the other buttons
        to inactive

        :param widget: str
        :type widget: str
        """
        for btn in self.findChildren(QPushButton):
            if btn.objectName() == widget:
                btn.set_active(True)
            else:
                btn.set_active(False)

    # DESELECT ALL BTNs
    # ///////////////////////////////////////////////////////////////
    def deselect_all(self):
        """It finds all the QPushButtons in the current widget and sets their active state to False"""
        for btn in self.findChildren(QPushButton):
            btn.set_active(False)
