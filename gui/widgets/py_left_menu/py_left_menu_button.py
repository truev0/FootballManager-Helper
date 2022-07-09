# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os

# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtWidgets import QPushButton, QLabel, QGraphicsDropShadowEffect

from PySide6.QtCore import Qt, QRect, QEvent, QPoint

from PySide6.QtGui import QPainter, QColor, QPixmap

# IMPORT FUNCTIONS
# ///////////////////////////////////////////////////////////////
from gui.core.functions import set_svg_icon


# CUSTOM LEFT MENU
# ///////////////////////////////////////////////////////////////
class PyLeftMenuButton(QPushButton):
    """
    This class is a subclass of QPushButton that has a custom paintEvent() method that draws a triangle on the left side
    of the button
    """

    def __init__(
            self,
            app_parent,
            text,
            btn_id=None,
            tooltip_text="",
            margin=4,
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
            icon_path="icon_add_user.svg",
            icon_active_menu="active_menu.svg",
            is_active=False,
            is_active_tab=False,
            is_toggle_active=False
    ):
        """
        The function is a class that inherits from QPushButton and sets the properties of the button

        :param app_parent: The parent widget
        :param text: The text that will be displayed on the button
        :param btn_id: The name of the button
        :param tooltip_text: The text that will be displayed when the mouse hovers over the button
        :param margin: The margin of the button, defaults to 4 (optional)
        :param dark_one: The background color of the button, defaults to #1b1e23 (optional)
        :param dark_three: The background color of the button when it's not active, defaults to #21252d (optional)
        :param dark_four: The background color of the button, defaults to #272c36 (optional)
        :param bg_one: The background color of the button, defaults to #2c313c (optional)
        :param icon_color: The color of the icon when the button is not active, defaults to #c3ccdf (optional)
        :param icon_color_hover: The color of the icon when the mouse is hovering over the button, defaults to #dce1ec
        (optional)
        :param icon_color_pressed: The color of the icon when the button is pressed, defaults to #edf0f5 (optional)
        :param icon_color_active: The color of the icon when the button is active, defaults to #f5f6f9 (optional)
        :param context_color: The color of the context menu, defaults to #568af2 (optional)
        :param text_foreground: The color of the text, defaults to #8a95aa (optional)
        :param text_active: The color of the text when the button is active, defaults to #dce1ec (optional)
        :param icon_path: The path to the icon you want to use, defaults to icon_add_user.svg (optional)
        :param icon_active_menu: This is the icon that will be displayed when the button is active, defaults to
        active_menu.svg (optional)
        :param is_active: If the button is active, it will have a different background color, defaults to False (optional)
        :param is_active_tab: This is used to set the active tab in the sidebar, defaults to False (optional)
        :param is_toggle_active: This is a boolean value that determines whether the button is active or not, defaults to
        False (optional)
        """
        super().__init__()
        self.setText(text)
        self.setCursor(Qt.PointingHandCursor)
        self.setMaximumHeight(50)
        self.setMinimumHeight(50)
        self.setObjectName(btn_id)

        # APP PATH
        self._icon_path = set_svg_icon(icon_path)
        self._icon_active_menu = set_svg_icon(icon_active_menu)

        # PROPERTIES
        self._margin = margin
        self._dark_one = dark_one
        self._dark_three = dark_three
        self._dark_four = dark_four
        self._bg_one = bg_one
        self._context_color = context_color
        self._icon_color = icon_color
        self._icon_color_hover = icon_color_hover
        self._icon_color_pressed = icon_color_pressed
        self._icon_color_active = icon_color_active
        self._set_icon_color = self._icon_color  # Set icon color
        self._set_bg_color = self._dark_one  # Set BG color
        self._set_text_foreground = text_foreground
        self._set_text_active = text_active
        self._parent = app_parent
        self._is_active = is_active
        self._is_active_tab = is_active_tab
        self._is_toggle_active = is_toggle_active

        # TOOLTIP
        self._tooltip_text = tooltip_text
        self.tooltip = _ToolTip(
            app_parent,
            tooltip_text,
            dark_one,
            context_color,
            text_foreground
        )
        self.tooltip.hide()

    # SETTER FOR TRANSLATE
    # ///////////////////////////////////////////////////////////////
    def change_tooltip(self, new_tooltip):
        """
        It changes the tooltip text of a widget

        :param new_tooltip: The new tooltip text
        """
        self._tooltip_text = new_tooltip
        self.tooltip = _ToolTip(
            self._parent,
            self._tooltip_text,
            self._dark_one,
            self._context_color,
            self._set_text_foreground
        )
        self.tooltip.hide()

    # PAINT EVENT
    # ///////////////////////////////////////////////////////////////
    def paintEvent(self, event):  # skipcq: PYL-W0613
        """
        The function is called when the widget is painted. It draws the background, the text, and the icon

        :param event: The event that was triggered
        """
        # PAINTER
        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setPen(Qt.NoPen)
        p.setFont(self.font())

        # RECTANGLES
        _rect = QRect(4, 5, self.width(), self.height() - 10)  # skipcq: PYL-W0612
        rect_inside = QRect(4, 5, self.width() - 8, self.height() - 10)
        rect_icon = QRect(0, 0, 50, self.height())
        rect_blue = QRect(4, 5, 20, self.height() - 10)
        rect_inside_active = QRect(7, 5, self.width(), self.height() - 10)
        rect_text = QRect(45, 0, self.width() - 50, self.height())

        if self._is_active:
            # DRAW BG BLUE
            p.setBrush(QColor(self._context_color))
            p.drawRoundedRect(rect_blue, 8, 8)

            # BG INSIDE
            p.setBrush(QColor(self._bg_one))
            p.drawRoundedRect(rect_inside_active, 8, 8)

            # DRAW ACTIVE
            icon_path = self._icon_active_menu
            app_path = os.path.abspath(os.getcwd())
            icon_path = os.path.normpath(os.path.join(app_path, icon_path))
            self._set_icon_color = self._icon_color_active
            self.icon_active(p, icon_path, self.width())

            # DRAW TEXT
            p.setPen(QColor(self._set_text_active))
            p.drawText(rect_text, Qt.AlignVCenter, self.text())

            # DRAW ICONS
            self.icon_paint(p, self._icon_path, rect_icon, self._set_icon_color)

        elif self._is_active_tab:
            # DRAW BG BLUE
            p.setBrush(QColor(self._dark_four))
            p.drawRoundedRect(rect_blue, 8, 8)

            # BG INSIDE
            p.setBrush(QColor(self._bg_one))
            p.drawRoundedRect(rect_inside_active, 8, 8)

            # DRAW ACTIVE
            icon_path = self._icon_active_menu
            app_path = os.path.abspath(os.getcwd())
            icon_path = os.path.normpath(os.path.join(app_path, icon_path))
            self._set_icon_color = self._icon_color_active
            self.icon_active(p, icon_path, self.width())

            # DRAW TEXT
            p.setPen(QColor(self._set_text_active))
            p.drawText(rect_text, Qt.AlignVCenter, self.text())

            # DRAW ICONS
            self.icon_paint(p, self._icon_path, rect_icon, self._set_icon_color)

        # NORMAL BG
        else:
            if self._is_toggle_active:
                # BG INSIDE
                p.setBrush(QColor(self._dark_three))
                p.drawRoundedRect(rect_inside, 8, 8)

                # DRAW TEXT
                p.setPen(QColor(self._set_text_foreground))
                p.drawText(rect_text, Qt.AlignVCenter, self.text())

                # DRAW ICONS
                if self._is_toggle_active:
                    self.icon_paint(p, self._icon_path, rect_icon, self._context_color)
                else:
                    self.icon_paint(p, self._icon_path, rect_icon, self._set_icon_color)
            else:
                # BG INSIDE
                p.setBrush(QColor(self._set_bg_color))
                p.drawRoundedRect(rect_inside, 8, 8)

                # DRAW TEXT
                p.setPen(QColor(self._set_text_foreground))
                p.drawText(rect_text, Qt.AlignVCenter, self.text())

                # DRAW ICONS
                self.icon_paint(p, self._icon_path, rect_icon, self._set_icon_color)

        p.end()

    # SET ACTIVE MENU
    # ///////////////////////////////////////////////////////////////
    def set_active(self, is_active):
        """
        If the button is active, set the icon color to the default color, and the background color to the default color. If
        the button is not active, set the icon color to the default color, and the background color to the dark color

        :param is_active: Boolean value to set the button to active or inactive
        """
        self._is_active = is_active
        if not is_active:
            self._set_icon_color = self._icon_color
            self._set_bg_color = self._dark_one

        self.repaint()

    # SET ACTIVE TAB MENU
    # ///////////////////////////////////////////////////////////////
    def set_active_tab(self, is_active):
        """
        If the tab is not active, set the icon color to the icon color and the background color to the dark one

        :param is_active: Boolean value that determines whether the tab is active or not
        """
        self._is_active_tab = is_active
        if not is_active:
            self._set_icon_color = self._icon_color
            self._set_bg_color = self._dark_one

        self.repaint()

    # RETURN IF IS ACTIVE MENU
    # ///////////////////////////////////////////////////////////////
    def is_active(self):
        """
        It returns the value of the variable _is_active.
        :return: The value of the variable _is_active
        """
        return self._is_active

    # RETURN IF IS ACTIVE TAB MENU
    # ///////////////////////////////////////////////////////////////
    def is_active_tab(self):
        """
        It returns the value of the variable _is_active_tab.
        :return: The value of the _is_active_tab attribute.
        """
        return self._is_active_tab

    # SET ACTIVE TOGGLE
    # ///////////////////////////////////////////////////////////////
    def set_active_toggle(self, is_active):
        """
        This function sets the toggle button to active or inactive

        :param is_active: This is a boolean value that determines whether the toggle is active or not
        """
        self._is_toggle_active = is_active

    # SET ICON
    # ///////////////////////////////////////////////////////////////
    def set_icon(self, icon_path):
        """
        It sets the icon path and then repaints the widget

        :param icon_path: The path to the icon you want to use
        """
        self._icon_path = icon_path
        self.repaint()

    # DRAW ICON WITH COLORS
    # ///////////////////////////////////////////////////////////////
    @staticmethod
    def icon_paint(qp, image, rect, color):
        """
        It takes a QPainter, a QPixmap, a QRect, and a QColor, and it draws the QPixmap in the center of the QRect, with the
        QColor as the color of the QPixmap

        :param qp: the QPainter object
        :param image: The image to be painted
        :param rect: The rectangle to draw the icon in
        :param color: The color to paint the icon with
        """
        icon = QPixmap(image)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()

    # DRAW ACTIVE ICON / RIGHT SIDE
    # ///////////////////////////////////////////////////////////////
    def icon_active(self, qp, image, width):
        """
        It takes a QPainter object, a QPixmap object, and an integer as arguments. It then creates a new QPainter object,
        sets the composition mode to SourceIn, fills the QPixmap object with the background color, draws the QPixmap object,
        and ends the painter

        :param qp: the QPainter object
        :param image: The image to be drawn
        :param width: the width of the widget
        """
        icon = QPixmap(image)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), self._bg_one)
        qp.drawPixmap(width - 5, 0, icon)
        painter.end()

    # CHANGE STYLES
    # Functions with custom styles
    # ///////////////////////////////////////////////////////////////
    def change_style(self, event):
        """
        If the mouse enters the button, change the background color to a darker shade of the original color. If the mouse
        leaves the button, change the background color back to the original color. If the mouse is pressed, change the
        background color to an even darker shade of the original color. If the mouse is released, change the background
        color back to the darker shade of the original color

        :param event: The event that is being processed
        """
        if event == QEvent.Enter:
            if not self._is_active:
                self._set_icon_color = self._icon_color_hover
                self._set_bg_color = self._dark_three
            self.repaint()
        elif event == QEvent.Leave:
            if not self._is_active:
                self._set_icon_color = self._icon_color
                self._set_bg_color = self._dark_one
            self.repaint()
        elif event == QEvent.MouseButtonPress:
            if not self._is_active:
                self._set_icon_color = self._context_color
                self._set_bg_color = self._dark_four
            self.repaint()
        elif event == QEvent.MouseButtonRelease:
            if not self._is_active:
                self._set_icon_color = self._icon_color_hover
                self._set_bg_color = self._dark_three
            self.repaint()

    # MOUSE OVER
    # Event triggered when the mouse is over the BTN
    # ///////////////////////////////////////////////////////////////
    def enterEvent(self, event):  # skipcq: PYL-W0613
        """
        Show tooltip when the mouse leave button

        :param event: The event that triggered the enterEvent
        """
        self.change_style(QEvent.Enter)
        if self.width() == 50 and self._tooltip_text:
            self.move_tooltip()
            self.tooltip.show()

    # MOUSE LEAVE
    # Event fired when the mouse leaves the BTN
    # ///////////////////////////////////////////////////////////////
    def leaveEvent(self, event):  # skipcq: PYL-W0613
        """
        Hide tooltip when the mouse leave button

        :param event: The event that triggered the leave event
        """
        self.change_style(QEvent.Leave)
        self.tooltip.hide()

    # MOUSE PRESS
    # Event triggered when the left button is pressed
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        """
        If the left mouse button is pressed, change the style of the button, hide the tooltip, and emit a signal

        :param event: The event that was triggered
        :return: The clicked signal is being emitted.
        """
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonPress)
            self.tooltip.hide()
            return self.clicked.emit()
        return None

    # MOUSE RELEASED
    # Event triggered after the mouse button is released
    # ///////////////////////////////////////////////////////////////
    def mouseReleaseEvent(self, event):
        """
        If the left mouse button is released, change the style of the button and emit the released signal

        :param event: The event object that was passed to the event handler
        :return: The signal is being returned.
        """
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonRelease)
            return self.released.emit()
        return None

    # MOVE TOOLTIP
    # ///////////////////////////////////////////////////////////////
    def move_tooltip(self):
        """The function moves the tooltip to the right of the widget, and centers it vertically"""
        # GET MAIN WINDOW PARENT
        gp = self.mapToGlobal(QPoint(0, 0))

        # SET WIDGET TO GET POSITION
        # Return absolute position of widget inside app
        pos = self._parent.mapFromGlobal(gp)

        # FORMAT POSITION
        # Adjust tooltip position with offset
        pos_x = pos.x() + self.width() + 5
        pos_y = pos.y() + (self.width() - self.tooltip.height()) // 2

        # SET POSITION TO WIDGET
        # Move tooltip position
        self.tooltip.move(pos_x, pos_y)


class _ToolTip(QLabel):
    """This class is a QLabel that displays a tooltip when the mouse hovers over it"""

    # TOOLTIP / LABEL StyleSheet
    style_tooltip = """
    QLabel {{
        background-color: {_dark_one};
        color: {_text_foreground};
        padding-left: 10px;
        padding-right: 10px;
        border-radius: 17px;
        border: 0px solid transparent;
        border-left: 3px solid {_context_color};
        font: 800 9pt "Segoe UI";
    }}
    """

    def __init__(
            self,
            parent,
            tooltip,
            dark_one,
            context_color,
            text_foreground
    ):
        """
        It creates a QLabel with a drop shadow and a custom style sheet

        :param parent: The parent widget of the tooltip
        :param tooltip: The text to be displayed in the tooltip
        :param dark_one: the background color of the parent widget
        :param context_color: The color of the tooltip's background
        :param text_foreground: The color of the text in the tooltip
        """
        QLabel.__init__(self)

        # LABEL SETUP
        style = self.style_tooltip.format(
            _dark_one=dark_one,
            _context_color=context_color,
            _text_foreground=text_foreground
        )
        self.setObjectName(u"label_tooltip")
        self.setStyleSheet(style)
        self.setMinimumHeight(34)
        self.setParent(parent)
        self.setText(tooltip)
        self.adjustSize()

        # SET DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.setGraphicsEffect(self.shadow)
