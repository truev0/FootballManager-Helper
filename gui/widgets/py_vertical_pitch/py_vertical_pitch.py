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
from gui.widgets.py_player_button import PyPlayerButton

# PY VERTICAL PITCH


class PyVerticalPitch(QWidget):
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
        super().__init__()

        # PROPERTIES
        # ///////////////////////////////////////////////////////////////
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
        self.clicked.emit(self.btn)

    def btn_released(self):
        self.released.emit(self.btn)

    # ADD BUTTON TO PITCH
    # Add btns and emit signals
    # ///////////////////////////////////////////////////////////////
    def add_btns(self, parameters):
        if parameters is not None:
            for parameter in parameters:
                _btn_id = parameter["btn_id"]
                _is_active = parameter["is_active"]
                _posX = parameter["posX"]
                _posY = parameter["posY"]
                _size = parameter["size"]

                self.btn = PyPlayerButton(
                    self._parent,
                    icon_path=set_svg_icon(self._image_player),
                    btn_id=_btn_id,
                    is_active=_is_active,
                )
                self.btn.setGeometry(QRect(_posX, _posY, _size, _size))
                self.btn.clicked.connect(self.btn_clicked)
                self.btn.released.connect(self.btn_released)

    # SELECT ONLY ONE BTN
    # ///////////////////////////////////////////////////////////////
    def select_only_one(self, widget: str):
        for btn in self.findChildren(QPushButton):
            if btn.objectName() == widget:
                btn.set_active(True)
            else:
                btn.set_active(False)

    # DESELECT ALL BTNs
    # ///////////////////////////////////////////////////////////////
    def deselect_all(self):
        for btn in self.findChildren(QPushButton):
            btn.set_active(False)
