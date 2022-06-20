# IMPORT PYSIDE CORE
# ///////////////////////////////////////////////////////////////
from pyside_core import *

# IMPORT PY TOGGLE BUTTON
# ///////////////////////////////////////////////////////////////
from gui.widgets import PyToggle


# PY BUTTON GROUP
# ////////////////////////////////////////////////////////////////
class PyButtonGroup(QWidget):
    def __init__(
            self
    ):
        super().__init__()
        self._count = None

        self.layout = QGridLayout(self)
        self.setLayout(self.layout)
        self.setStyleSheet("border: 2px solid;"
                           "border-radius: 10px;")

        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(False)

    def add_buttons(self, names):
        first_label_pos = [(y, x) for y in range(15) for x in range(0, 8, 2)]
        second_label_pos = [(y, x) for y in range(12) for x in range(0, 8, 2)]
        first_layout_pos = [(y, x) for y in range(15) for x in range(1, 8, 2)]
        second_layout_pos = [(y, x) for y in range(12) for x in range(1, 8, 2)]
        i = 0
        if len(names) < 40:
            for pos_l, name, pos_b in zip(first_label_pos, names, first_layout_pos):
                if name == '':
                    continue
                checkbox = PyToggle(name)
                label = QLabel(name)
                label.setAlignment(Qt.AlignCenter)
                self.button_group.addButton(checkbox, i)
                self.layout.addWidget(label, *pos_l)
                self.layout.addWidget(checkbox, *pos_b)
                i += 1
            self._count = i
        else:
            for pos_l, name, pos_b in zip(second_label_pos, names, second_layout_pos):
                if name == '':
                    continue
                checkbox = PyToggle(name)
                label = QLabel(name)
                label.setAlignment(Qt.AlignCenter)
                self.button_group.addButton(checkbox, i)
                self.layout.addWidget(label, *pos_l)
                self.layout.addWidget(checkbox, *pos_b)
                i += 1
            self._count = i

    def remove_all_buttons(self):
        for i in range(self._count):
            self.button_group.removeButton(self.button_group.button(i))

    def get_count(self):
        return self._count
