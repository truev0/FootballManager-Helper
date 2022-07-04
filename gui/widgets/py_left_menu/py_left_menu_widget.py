# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, \
    QFrame

from PySide6.QtCore import QPropertyAnimation, Signal, QEasingCurve, Qt

# IMPORT BUTTON AND DIV
# ///////////////////////////////////////////////////////////////
from .py_left_menu_button import PyLeftMenuButton
from .py_div import PyDiv

# IMPORT FUNCTIONS
# ///////////////////////////////////////////////////////////////
from gui.core.functions import set_svg_icon


# PY LEFT MENU
# ///////////////////////////////////////////////////////////////
# This class is a widget that contains a QVBoxLayout that contains a QPushButton and a QListWidget
class PyLeftMenu(QWidget):
    # SIGNALS
    clicked = Signal(object)
    released = Signal(object)

    def __init__(
            self,
            parent=None,
            app_parent=None,
            dark_one="#1b1e23",
            dark_three="#21252d",
            dark_four="#272c36",
            bg_one="#2c313c",
            icon_color="#c3ccdf",
            icon_color_hover="#dce1ec",
            icon_color_pressed="#edf0f5",
            icon_color_active="#f5f6f9",
            context_color="#568af2",
            text_foreground="#8a95aa",
            text_active="#dce1ec",
            duration_time=500,
            radius=8,
            minimum_width=50,
            maximum_width=240,
            icon_path="icon_menu.svg",
            icon_path_close="icon_menu_close.svg",
            toggle_text="Hide Menu",
            toggle_tooltip="Show menu"
    ):
        """
        This function sets up the widget and its properties

        :param parent: The parent widget
        :param app_parent: The parent of the widget
        :param dark_one: The background color of the menu, defaults to #1b1e23 (optional)
        :param dark_three: The color of the menu's background, defaults to #21252d (optional)
        :param dark_four: The background color of the menu, defaults to #272c36 (optional)
        :param bg_one: The background color of the menu, defaults to #2c313c (optional)
        :param icon_color: The color of the icon when the menu is hidden, defaults to #c3ccdf (optional)
        :param icon_color_hover: The color of the icon when the mouse is hovering over it, defaults to #dce1ec (optional)
        :param icon_color_pressed: The color of the icon when the button is pressed, defaults to #edf0f5 (optional)
        :param icon_color_active: The color of the icon when the button is active, defaults to #f5f6f9 (optional)
        :param context_color: The color of the context menu, defaults to #568af2 (optional)
        :param text_foreground: The color of the text in the menu, defaults to #8a95aa (optional)
        :param text_active: The color of the text when the button is active, defaults to #dce1ec (optional)
        :param duration_time: The time it takes for the animation to complete, defaults to 500 (optional)
        :param radius: The radius of the rounded corners, defaults to 8 (optional)
        :param minimum_width: The minimum width of the menu, defaults to 50 (optional)
        :param maximum_width: The maximum width of the menu, defaults to 240 (optional)
        :param icon_path: The path to the icon that will be used for the toggle button, defaults to icon_menu.svg (optional)
        :param icon_path_close: The icon that will be displayed when the menu is open, defaults to icon_menu_close.svg
        (optional)
        :param toggle_text: The text that will be displayed on the toggle button, defaults to Hide Menu (optional)
        :param toggle_tooltip: The tooltip text that appears when you hover over the toggle button, defaults to Show menu
        (optional)
        """
        super().__init__()

        # PROPERTIES
        # ///////////////////////////////////////////////////////////////
        self._dark_one = dark_one
        self._dark_three = dark_three
        self._dark_four = dark_four
        self._bg_one = bg_one
        self._icon_color = icon_color
        self._icon_color_hover = icon_color_hover
        self._icon_color_pressed = icon_color_pressed
        self._icon_color_active = icon_color_active
        self._context_color = context_color
        self._text_foreground = text_foreground
        self._text_active = text_active
        self._duration_time = duration_time
        self._radius = radius
        self._minimum_width = minimum_width
        self._maximum_width = maximum_width
        self._icon_path = set_svg_icon(icon_path)
        self._icon_path_close = set_svg_icon(icon_path_close)

        # SET PARENT
        self._parent = parent
        self._app_parent = app_parent

        # SETUP WIDGETS
        self.setup_ui()

        # SET BG COLOR
        self.bg.setStyleSheet(f"background: {dark_one}; border-radius: {radius};")

        # TOGGLE BUTTON AND DIV MENUS
        # ///////////////////////////////////////////////////////////////
        self.toggle_button = PyLeftMenuButton(
            app_parent,
            text=toggle_text,
            tooltip_text=toggle_tooltip,
            dark_one=self._dark_one,
            dark_three=self._dark_three,
            dark_four=self._dark_four,
            bg_one=self._bg_one,
            icon_color=self._icon_color,
            icon_color_hover=self._icon_color_active,
            icon_color_pressed=self._icon_color_pressed,
            icon_color_active=self._icon_color_active,
            context_color=self._context_color,
            text_foreground=self._text_foreground,
            text_active=self._text_active,
            icon_path=icon_path
        )
        self.toggle_button.clicked.connect(self.toggle_animation)
        self.div_top = PyDiv(dark_four)

        # ADD TO TOP LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.top_layout.addWidget(self.toggle_button)
        self.top_layout.addWidget(self.div_top)

        # ADD TO BOTTOM LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.div_bottom = PyDiv(dark_four)
        self.div_bottom.hide()
        self.bottom_layout.addWidget(self.div_bottom)

    # ADD BUTTONS TO LEFT MENU
    # Add btns and emit signals
    # ///////////////////////////////////////////////////////////////
    def add_menus(self, parameters):
        """
        It adds a menu button to the left menu bar

        :param parameters: [
        """
        if parameters is not None:
            for parameter in parameters:
                _btn_icon = parameter['btn_icon']
                _btn_id = parameter['btn_id']
                _btn_text = parameter['btn_text']
                _btn_tooltip = parameter['btn_tooltip']
                _show_top = parameter['show_top']
                _is_active = parameter['is_active']

                self.menu = PyLeftMenuButton(
                    self._app_parent,
                    text=_btn_text,
                    btn_id=_btn_id,
                    tooltip_text=_btn_tooltip,
                    dark_one=self._dark_one,
                    dark_three=self._dark_three,
                    dark_four=self._dark_four,
                    bg_one=self._bg_one,
                    icon_color=self._icon_color,
                    icon_color_hover=self._icon_color_active,
                    icon_color_pressed=self._icon_color_pressed,
                    icon_color_active=self._icon_color_active,
                    context_color=self._context_color,
                    text_foreground=self._text_foreground,
                    text_active=self._text_active,
                    icon_path=_btn_icon,
                    is_active=_is_active
                )
                self.menu.clicked.connect(self.btn_clicked)
                self.menu.released.connect(self.btn_released)

                # ADD TO LAYOUT
                if _show_top:
                    self.top_layout.addWidget(self.menu)
                else:
                    self.div_bottom.show()
                    self.bottom_layout.addWidget(self.menu)

    # LEFT MENU EMIT SIGNALS
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        """
        The function is called when the button is clicked. It emits a signal that is connected to a slot. The slot is a
        function that is called when the signal is emitted
        """
        self.clicked.emit(self.menu)

    def btn_released(self):
        """The function emits a signal that is connected to a slot that opens a menu"""
        self.released.emit(self.menu)

    # EXPAND / RETRACT LEF MENU
    # ///////////////////////////////////////////////////////////////
    def toggle_animation(self):
        """
        It creates an animation object, stops it, sets the start and end values, sets the easing curve, sets the duration,
        and starts the animation
        """
        # CREATE ANIMATION
        self.animation = QPropertyAnimation(self._parent, b"minimumWidth")
        self.animation.stop()
        if self.width() == self._minimum_width:
            self.animation.setStartValue(self.width())
            self.animation.setEndValue(self._maximum_width)
            self.toggle_button.set_active_toggle(True)
            self.toggle_button.set_icon(self._icon_path_close)
        else:
            self.animation.setStartValue(self.width())
            self.animation.setEndValue(self._minimum_width)
            self.toggle_button.set_active_toggle(False)
            self.toggle_button.set_icon(self._icon_path)
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setDuration(self._duration_time)
        self.animation.start()

    # SELECT ONLY ONE BTN
    # ///////////////////////////////////////////////////////////////
    def select_only_one(self, widget: str):
        """
        It takes a string as an argument, and then finds all the QPushButtons in the current window, and if the button's
        object name matches the string passed to the function, it sets that button to active, and all the other buttons to
        inactive

        :param widget: str
        :type widget: str
        """
        for btn in self.findChildren(QPushButton):
            if btn.objectName() == widget:
                btn.set_active(True)
            else:
                btn.set_active(False)

    # SELECT ONLY ONE TAB BTN
    # ///////////////////////////////////////////////////////////////
    def select_only_one_tab(self, widget: str):
        """
        It loops through all the buttons in the window, and if the button's name matches the name of the button that was
        clicked, it sets the button's active_tab property to True, otherwise it sets it to False

        :param widget: str - the name of the widget that you want to be active
        :type widget: str
        """
        for btn in self.findChildren(QPushButton):
            if btn.objectName() == widget:
                btn.set_active_tab(True)
            else:
                btn.set_active_tab(False)

    # DESELECT ALL BTNs
    # ///////////////////////////////////////////////////////////////
    def deselect_all(self):
        """It finds all the QPushButtons in the current widget and sets their active state to False"""
        for btn in self.findChildren(QPushButton):
            btn.set_active(False)

    # DESELECT ALL TAB BTNs
    # ///////////////////////////////////////////////////////////////
    def deselect_all_tab(self):
        """It finds all the QPushButtons in the current widget and sets their active_tab property to False"""
        for btn in self.findChildren(QPushButton):
            btn.set_active_tab(False)

    # SETUP APP
    # ///////////////////////////////////////////////////////////////
    def setup_ui(self):
        """It sets up the UI of the left menu"""
        # ADD MENU LAYOUT
        self.left_menu_layout = QVBoxLayout(self)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)

        # ADD BG
        self.bg = QFrame()

        # TOP FRAME
        self.top_frame = QFrame()

        # BOTTOM FRAME
        self.bottom_frame = QFrame()

        # ADD LAYOUTS
        self._layout = QVBoxLayout(self.bg)
        self._layout.setContentsMargins(0, 0, 0, 0)

        # TOP LAYOUT
        self.top_layout = QVBoxLayout(self.top_frame)
        self.top_layout.setContentsMargins(0, 0, 0, 0)
        self.top_layout.setSpacing(1)

        # BOTTOM LAYOUT
        self.bottom_layout = QVBoxLayout(self.bottom_frame)
        self.bottom_layout.setContentsMargins(0, 0, 0, 8)
        self.bottom_layout.setSpacing(1)

        # ADD TOP AND BOTTOM FRAME
        self._layout.addWidget(self.top_frame, 0, Qt.AlignTop)
        self._layout.addWidget(self.bottom_frame, 0, Qt.AlignBottom)

        # ADD BG TO LAYOUT
        self.left_menu_layout.addWidget(self.bg)
