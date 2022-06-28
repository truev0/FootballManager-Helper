# IMPORT PYSIDE CORE
# ///////////////////////////////////////////////////////////////
# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY TOGGLE BUTTON
# ///////////////////////////////////////////////////////////////
from gui.widgets import PyComboBox, PyLineEdit, PyToggle
from pyside_core import *


# PY BUTTON GROUP
# ////////////////////////////////////////////////////////////////
class PyButtonGroup(QWidget):

    def __init__(self):
        super().__init__()
        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        self._count = None
        self._lines = None

        self.layout = QGridLayout(self)
        self.setLayout(self.layout)
        self.setStyleSheet(
            "QLabel { border: 2px solid #1b1e23; border-radius:10px;}")

        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(False)

    def add_buttons(self, names, opt):
        operators = [">", "<", "<=", ">="]
        i = 0
        if opt == 0:
            first_label_pos = [(y, x) for y in range(12)
                               for x in range(0, 8, 2)]
            second_label_pos = [(y, x) for y in range(9)
                                for x in range(0, 8, 2)]
            first_layout_pos = [(y, x) for y in range(12)
                                for x in range(1, 8, 2)]
            second_layout_pos = [(y, x) for y in range(9)
                                 for x in range(1, 8, 2)]
            if len(names) > 40:
                for pos_l, name, pos_b in zip(first_label_pos, names,
                                              first_layout_pos):
                    if name == "":
                        continue
                    custom_widget = PyToggle(name)
                    label = QLabel(name)
                    label.setAlignment(Qt.AlignCenter)
                    self.button_group.addButton(custom_widget, i)
                    self.layout.addWidget(label, *pos_l)
                    self.layout.addWidget(custom_widget, *pos_b)
                    i += 1
                    self._count = i
            else:
                for pos_l, name, pos_b in zip(second_label_pos, names,
                                              second_layout_pos):
                    if name == "":
                        continue
                    custom_widget = PyToggle(name)
                    label = QLabel(name)
                    label.setAlignment(Qt.AlignCenter)
                    self.button_group.addButton(custom_widget, i)
                    self.layout.addWidget(label, *pos_l)
                    self.layout.addWidget(custom_widget, *pos_b)
                    i += 1
                    self._count = i
        elif opt == 1:
            first_label_pos = [(y, x) for y in range(48)
                               for x in range(0, 3, 3)]
            second_label_pos = [(y, x) for y in range(36)
                                for x in range(0, 3, 3)]
            first_layout_pos = [(y, x) for y in range(48)
                                for x in range(2, 3, 3)]
            second_layout_pos = [(y, x) for y in range(36)
                                 for x in range(2, 3, 3)]
            first_combo_pos = [(y, x) for y in range(48)
                               for x in range(1, 3, 3)]
            second_combo_pos = [(y, x) for y in range(36)
                                for x in range(1, 3, 3)]
            if len(names) > 40:
                for pos_l, name, pos_line, pos_c in zip(
                        first_label_pos, names, first_layout_pos,
                        first_combo_pos):
                    custom_widget = PyLineEdit(place_holder_text=name)
                    validator = QDoubleValidator(0.00, 99999999.99, 2)
                    validator.setNotation(QDoubleValidator.StandardNotation)
                    custom_widget.setValidator(validator)
                    custom_widget.setMinimumHeight(40)
                    custom_widget2 = PyComboBox(
                        dark_one=self.themes["app_color"]["dark_one"],
                        text_foreground=self.themes["app_color"]
                        ["text_foreground"],
                        combo_border=self.themes["app_color"]["context_hover"],
                    )
                    custom_widget2.setMinimumWidth(60)
                    custom_widget2.setMaximumWidth(80)
                    for o in operators:
                        custom_widget2.addItem(o)
                    label = QLabel(name)
                    label.setMinimumWidth(50)
                    label.setAlignment(Qt.AlignCenter)
                    self.layout.addWidget(label, *pos_l)
                    self.layout.addWidget(custom_widget, *pos_line)
                    self.layout.addWidget(custom_widget2, *pos_c)
            else:
                for pos_l, name, pos_line, pos_c in zip(
                        second_label_pos, names, second_layout_pos,
                        second_combo_pos):
                    custom_widget = PyLineEdit(place_holder_text=name)
                    custom_widget.setMinimumHeight(40)
                    custom_widget2 = PyComboBox(
                        dark_one=self.themes["app_color"]["dark_one"],
                        text_foreground=self.themes["app_color"]
                        ["text_foreground"],
                        combo_border=self.themes["app_color"]["context_hover"],
                    )
                    custom_widget2.setMinimumWidth(60)
                    custom_widget2.setMaximumWidth(80)
                    for o in operators:
                        custom_widget2.addItem(o)
                    label = QLabel(name)
                    label.setMinimumWidth(65)
                    label.setMaximumWidth(70)
                    label.setAlignment(Qt.AlignCenter)
                    self.layout.addWidget(label, *pos_l)
                    self.layout.addWidget(custom_widget, *pos_line)
                    self.layout.addWidget(custom_widget2, *pos_c)
        elif opt == 2:
            first_label_pos = [(y, x) for y in range(3)
                               for x in range(0, 3, 3)]
            first_layout_pos = [(y, x) for y in range(3)
                                for x in range(2, 3, 3)]
            first_combo_pos = [(y, x) for y in range(3)
                               for x in range(1, 3, 3)]
            for pos_l, name, pos_line, pos_c in zip(first_label_pos, names,
                                                    first_layout_pos,
                                                    first_combo_pos):
                custom_widget = PyLineEdit(place_holder_text=name)
                custom_widget.setMinimumHeight(40)
                custom_widget2 = PyComboBox(
                    dark_one=self.themes["app_color"]["dark_one"],
                    text_foreground=self.themes["app_color"]
                    ["text_foreground"],
                    combo_border=self.themes["app_color"]["context_hover"],
                )
                custom_widget2.setMinimumWidth(60)
                custom_widget2.setMaximumWidth(80)
                for o in operators:
                    custom_widget2.addItem(o)
                label = QLabel(name)
                label.setMinimumWidth(50)
                label.setAlignment(Qt.AlignCenter)
                self.layout.addWidget(label, *pos_l)
                self.layout.addWidget(custom_widget, *pos_line)
                self.layout.addWidget(custom_widget2, *pos_c)

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
