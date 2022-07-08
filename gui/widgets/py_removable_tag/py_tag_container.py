# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout

# IMPORT TAGS
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_removable_tag.py_removable_widget import PyRemovableTag

# PY TAG CONTAINER
# ///////////////////////////////////////////////////////////////


class PyTagContainer(QWidget):
    # SIGNALS
    clicked = Signal(object)
    released = Signal(object)

    def __init__(self, parent=None):
        super().__init__()
        self._parent = parent
        self.main_lay = QVBoxLayout(self)
        self.main_lay.setContentsMargins(0, 0, 0, 0)
        self.main_lay.setSpacing(0)
        self.main_lay.setAlignment(Qt.AlignTop)
        self.setLayout(self.main_lay)

    # EMIT SIGNALS
    def btn_clicked(self):
        self.clicked.emit(self.tag)

    def btn_released(self):
        self.released.emit(self.tag)

    # ADD TAGS
    def add_tag(self, names):
        for name in names:
            _text = name

            self.tag = PyRemovableTag(
                text=_text
            )
            self.tag.close_button.clicked.connect(self.btn_clicked)
            self.tag.close_button.released.connect(self.btn_released)
            self.main_lay.addWidget(self.tag)
