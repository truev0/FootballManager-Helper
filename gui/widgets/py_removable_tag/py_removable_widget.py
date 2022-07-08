# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import Signal, Qt, Property

from PySide6.QtWidgets import QLabel, QPushButton, QHBoxLayout, \
    QSizePolicy


# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
# It's a QPushButton that can be connected to a Python function

class PyRemovableTag(QPushButton):
    """Tag for players in tactic view"""
    sig_closed = Signal()
    sig_clicked = Signal()

    def __init__(
            self,
            instanceof=None,
            text="",
            parent=None
    ):
        super(PyRemovableTag, self).__init__(text=text, parent=parent)
        self.setCursor(Qt.PointingHandCursor)
        self._instanceof = instanceof
        self.setText(text)
        self.clicked.connect(self.delete_from_all)
        self.setVisible(True)

        self._clickable = False
        self._border = True

        self._color = None

    def delete_from_all(self):
        tmp_lista = self._instanceof.get_lista()
        tmp_lista.remove(self.text())
        self._instanceof.set_updated_lista(tmp_lista)
        self.close()
