# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import Signal, Qt, Property

from PySide6.QtWidgets import QLabel, QPushButton, QHBoxLayout, \
    QSizePolicy


# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
# It's a QPushButton that can be connected to a Python function
class PyRemovableTag(QLabel):
    """Tag for players in tactic view"""
    sig_closed = Signal()
    sig_clicked = Signal()

    def __init__(
            self,
            text="",
            parent=None
    ):
        super(PyRemovableTag, self).__init__(text=text, parent=parent)
        self._deleted = False
        self._index = None
        self._is_pressed = False
        self.close_button = QPushButton(text="X", parent=self)
        self.close_button.clicked.connect(self.sig_closed)
        self.close_button.clicked.connect(self.close)
        self.close_button.setVisible(False)

        self._main_lay = QHBoxLayout()
        self._main_lay.setContentsMargins(0, 0, 0, 0)
        self._main_lay.addStretch()
        self._main_lay.addWidget(self.close_button)

        self.setLayout(self._main_lay)

        self._clickable = False
        self._border = True
        self._border_style = """
        PyRemovableTag {{
        padding: 4px;
        color: #FF00FF;
        border-radius: 4px;
        border: 1px solid #FFFFFF;
        background-color: #dce1ec;
        }}
        PyRemovableTag:hover {{
        color: #00FF00;
        }}
        """

        self._no_border_style = """
        PyRemovableTag {{
        padding: 4px;
        border-radius: 4px;
        color: #FF00FF;
        border: 0 solid #FFFFFF;
        background-color: #dce1ec;
        }}
        PyRemovableTag:hover {{
        background-color: #00FF00;
        }}
        """

        self.setSizePolicy(
            QSizePolicy.Minimum,
            QSizePolicy.Minimum
        )

        self._color = None
        self.set_color("#ffffff")

    def minimumSizeHint(self, *args, **kwargs):
        orig = super(PyRemovableTag, self).minimumSizeHint(*args, **kwargs)
        orig.setWidth(
            orig.width() + 0.5
        )
        return orig

    def get_color(self):
        return self._color

    def set_color(self, value):
        self._color = value
        self._update_style()

    def _update_style(self):
        # scale_x, _ = get_scale_factor()
        if self._border:
            self.setStyleSheet(
                self._border_style
            )
        else:
            self.setStyleSheet(
                self._no_border_style
            )

    color = Property(str, get_color, set_color)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._is_pressed = True
        return super(PyRemovableTag, self).mousePressEvent(event)

    def leaveEvent(self, event):
        self._is_pressed = False
        return super(PyRemovableTag, self).leaveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self._is_pressed:
            if self._clickable:
                self.sig_clicked.emit()
        self._is_pressed = False
        return super(PyRemovableTag, self).mouseReleaseEvent(event)

    def closeable(self):
        self.close_button.setVisible(True)
        return self

    def clickable(self):
        self.setCursor(Qt.PointingHandCursor)
        self._clickable = True
        return self

    def no_border(self):
        self._border = False
        self._update_style()
        return self

    def coloring(self, color):
        self.set_color(color)
        return self

    def set_self_index(self, index):
        self._index = index

    def get_self_index(self):
        return self._index

    def get_deleted(self):
        return self._deleted

    def closeEvent(self, event):
        self._deleted = True
