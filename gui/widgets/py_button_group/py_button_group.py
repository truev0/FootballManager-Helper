# IMPORT PYSIDE CORE
# ///////////////////////////////////////////////////////////////
from pyside_core import *

# IMPORT PY TOGGLE BUTTON
# ///////////////////////////////////////////////////////////////
from gui.widgets import PyToggle, PyLineEdit


# PY BUTTON GROUP
# ////////////////////////////////////////////////////////////////
class PyButtonGroup(QWidget):
    def __init__(
            self
    ):
        super().__init__()
        self._count = None
        self._lines = None

        self.layout = QGridLayout(self)
        self.setLayout(self.layout)
        self.setStyleSheet("border: 2px solid;"
                           "border-radius: 10px;")

        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(False)

    def add_buttons(self, names, opt):
        custom_widget = None
        first_label_pos = None
        second_label_pos = None
        first_layout_pos = None
        second_layout_pos = None
        label = None
        if opt == 0:
            first_label_pos = [(y, x) for y in range(12) for x in range(0, 8, 2)]
            second_label_pos = [(y, x) for y in range(9) for x in range(0, 8, 2)]
            first_layout_pos = [(y, x) for y in range(12) for x in range(1, 8, 2)]
            second_layout_pos = [(y, x) for y in range(9) for x in range(1, 8, 2)]
        elif opt == 1:
            first_label_pos = [(y, x) for y in range(48) for x in range(0, 2, 2)]
            second_label_pos = [(y, x) for y in range(36) for x in range(0, 2, 2)]
            first_layout_pos = [(y, x) for y in range(48) for x in range(1, 2, 2)]
            second_layout_pos = [(y, x) for y in range(36) for x in range(1, 2, 2)]
        i = 0
        if len(names) > 40:
            for pos_l, name, pos_b in zip(first_label_pos, names, first_layout_pos):
                if name == '':
                    continue
                if opt == 0:
                    custom_widget = PyToggle(name)
                    self.button_group.addButton(custom_widget, i)
                    label = QLabel(name)
                    i += 1
                    self._count = i
                elif opt == 1:
                    custom_widget = PyLineEdit(place_holder_text=name)
                    custom_widget.setMinimumHeight(40)
                    label = QLabel(name)
                    label.setMinimumWidth(50)

                label.setAlignment(Qt.AlignCenter)
                self.layout.addWidget(label, *pos_l)
                self.layout.addWidget(custom_widget, *pos_b)
        else:
            for pos_l, name, pos_b in zip(second_label_pos, names, second_layout_pos):
                if name == '':
                    continue
                if opt == 0:
                    custom_widget = PyToggle(name)
                    self.button_group.addButton(custom_widget, i)
                    label = QLabel(name)
                    i += 1
                    self._count = i
                elif opt == 1:
                    custom_widget = PyLineEdit(place_holder_text=name)
                    label = QLabel(name)
                    label.setMinimumWidth(50)

                label.setAlignment(Qt.AlignCenter)
                self.layout.addWidget(label, *pos_l)
                self.layout.addWidget(custom_widget, *pos_b)

    def remove_all_buttons(self):
        for i in range(self._count):
            self.button_group.removeButton(self.button_group.button(i))

    def reset_all_lines(self):
        for child in self.findChildren(QLineEdit):
            child.clear()

    def get_count(self):
        return self._count

    def get_lines(self):
        return self._lines
