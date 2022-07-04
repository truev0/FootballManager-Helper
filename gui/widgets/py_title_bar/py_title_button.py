# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtWidgets import QPushButton, QLabel, QGraphicsDropShadowEffect

from PySide6.QtCore import Qt, QEvent, QRect, QPoint

from PySide6.QtGui import QColor, QPainter, QBrush, QPixmap


# PY TITLE BUTTON
# ///////////////////////////////////////////////////////////////
# It's a QPushButton that has a title and a description
class PyTitleButton(QPushButton):
    def __init__(
            self,
            parent,
            app_parent=None,
            tooltip_text="",
            btn_id=None,
            width=30,
            height=30,
            radius=8,
            bg_color="#343b48",
            bg_color_hover="#3c4454",
            bg_color_pressed="#2c313c",
            icon_color="#c3ccdf",
            icon_color_hover="#dce1ec",
            icon_color_pressed="#edf0f5",
            icon_color_active="#f5f6f9",
            icon_path="no_icon.svg",
            dark_one="#1b1e23",
            context_color="#568af2",
            text_foreground="#8a95aa",
            is_active=False
    ):
        """
        It's a function that creates a button with a tooltip

        :param parent: The parent widget of the button
        :param app_parent: The parent of the application
        :param tooltip_text: The text that will be displayed in the tooltip
        :param btn_id: The name of the button
        :param width: The width of the button, defaults to 30 (optional)
        :param height: The height of the button, defaults to 30 (optional)
        :param radius: The radius of the button's corners, defaults to 8 (optional)
        :param bg_color: The background color of the button, defaults to #343b48 (optional)
        :param bg_color_hover: The background color of the button when the mouse is hovering over it, defaults to #3c4454
        (optional)
        :param bg_color_pressed: The background color of the button when it's pressed, defaults to #2c313c (optional)
        :param icon_color: The color of the icon when the button is not hovered over or pressed, defaults to #c3ccdf
        (optional)
        :param icon_color_hover: The color of the icon when the mouse is hovering over the button, defaults to #dce1ec
        (optional)
        :param icon_color_pressed: The color of the icon when the button is pressed, defaults to #edf0f5 (optional)
        :param icon_color_active: The color of the icon when the button is active, defaults to #f5f6f9 (optional)
        :param icon_path: The path to the icon you want to use, defaults to no_icon.svg (optional)
        :param dark_one: The background color of the tooltip, defaults to #1b1e23 (optional)
        :param context_color: The color of the tooltip's background, defaults to #568af2 (optional)
        :param text_foreground: The color of the text in the tooltip, defaults to #8a95aa (optional)
        :param is_active: If the button is active or not, defaults to False (optional)
        """
        super().__init__()

        # SET DEFAULT PARAMETERS
        self.setFixedSize(width, height)
        self.setCursor(Qt.PointingHandCursor)
        self.setObjectName(btn_id)

        # PROPERTIES
        self._bg_color = bg_color
        self._bg_color_hover = bg_color_hover
        self._bg_color_pressed = bg_color_pressed
        self._icon_color = icon_color
        self._icon_color_hover = icon_color_hover
        self._icon_color_pressed = icon_color_pressed
        self._icon_color_active = icon_color_active
        self._context_color = context_color
        self._top_margin = self.height() + 6
        self._is_active = is_active
        # Set Parameters
        self._dark_one = dark_one
        self._text_foreground = text_foreground
        self._set_bg_color = bg_color
        self._set_icon_path = icon_path
        self._set_icon_color = icon_color
        self._set_border_radius = radius
        # Parent
        self._parent = parent
        self._app_parent = app_parent

        # TOOLTIP
        self._tooltip_text = tooltip_text
        self._tooltip = _ToolTip(
            app_parent,
            tooltip_text,
            dark_one,
            context_color,
            text_foreground
        )
        self._tooltip.hide()

    # DELETE TOOLTIP
    # ///////////////////////////////////////////////////////////////
    def delete_tooltip(self):
        """It deletes the tooltip object from the class"""
        del self._tooltip

    # SETTER FOR TRANSLATE
    # ///////////////////////////////////////////////////////////////
    def change_tooltip(self, new_tooltip):
        """
        It changes the tooltip text of a widget

        :param new_tooltip: The new tooltip text
        """
        self._tooltip_text = new_tooltip
        self._tooltip = _ToolTip(
            self._app_parent,
            self._tooltip_text,
            self._dark_one,
            self._context_color,
            self._text_foreground
        )
        self._tooltip.hide()

    # SET ACTIVE MENU
    # ///////////////////////////////////////////////////////////////
    def set_active(self, is_active):
        """
        It sets the active state of the button and repaints it

        :param is_active: A boolean value that indicates whether the button is active or not
        """
        self._is_active = is_active
        self.repaint()

    # RETURN IF IS ACTIVE MENU
    # ///////////////////////////////////////////////////////////////
    def is_active(self):
        """
        It returns the value of the variable _is_active.
        :return: The value of the variable _is_active
        """
        return self._is_active

    # PAINT EVENT
    # painting the button and the icon
    # ///////////////////////////////////////////////////////////////
    def paintEvent(self, event):  # skipcq: PYL-W0613
        """
        > The function paints a rounded rectangle with a background color and an icon

        :param event: The event that triggered the paintEvent
        """
        # PAINTER
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.RenderHint.Antialiasing)

        if self._is_active:
            # BRUSH
            brush = QBrush(QColor(self._context_color))
        else:
            # BRUSH
            brush = QBrush(QColor(self._set_bg_color))

        # CREATE RECTANGLE
        rect = QRect(0, 0, self.width(), self.height())
        paint.setPen(Qt.NoPen)
        paint.setBrush(brush)
        paint.drawRoundedRect(
            rect,
            self._set_border_radius,
            self._set_border_radius
        )

        # DRAW ICONS
        self.icon_paint(paint, self._set_icon_path, rect)

        # END PAINTER
        paint.end()

    # CHANGE STYLES
    # Functions with custom styles
    # ///////////////////////////////////////////////////////////////
    def change_style(self, event):
        """
        If the mouse enters the button, change the background color to the hover color and the icon color to the hover
        color. If the mouse leaves the button, change the background color to the normal color and the icon color to the
        normal color. If the mouse presses the button, change the background color to the pressed color and the icon color
        to the pressed color. If the mouse releases the button, change the background color to the hover color and the icon
        color to the hover color

        :param event: The event that triggered the change
        """
        if event == QEvent.Enter:
            self._set_bg_color = self._bg_color_hover
            self._set_icon_color = self._icon_color_hover
            self.repaint()
        elif event == QEvent.Leave:
            self._set_bg_color = self._bg_color
            self._set_icon_color = self._icon_color
            self.repaint()
        elif event == QEvent.MouseButtonPress:
            self._set_bg_color = self._bg_color_pressed
            self._set_icon_color = self._icon_color_pressed
            self.repaint()
        elif event == QEvent.MouseButtonRelease:
            self._set_bg_color = self._bg_color_hover
            self._set_icon_color = self._icon_color_hover
            self.repaint()

    # MOUSE OVER
    # Event triggered when the mouse is over the BTN
    # ///////////////////////////////////////////////////////////////
    def enterEvent(self, event):  # skipcq: PYL-W0613
        """
        > When the mouse enter the button, change the style of the button and show the tooltip

        :param event: The event that triggered this method
        """
        self.change_style(QEvent.Enter)
        self.move_tooltip()
        self._tooltip.show()

    # MOUSE LEAVE
    # Event fired when the mouse leaves the BTN
    # ///////////////////////////////////////////////////////////////
    def leaveEvent(self, event):  # skipcq: PYL-W0613
        """
        > When the mouse leaves the button, change the style of the button and hide the tooltip

        :param event: The event that triggered the leave event
        """
        self.change_style(QEvent.Leave)
        self.move_tooltip()
        self._tooltip.hide()

    # MOUSE PRESS
    # Event triggered when the left button is pressed
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        """
        If the left mouse button is pressed, change the style of the button, set focus to the button, and emit the clicked
        signal.

        :param event: The event object that was passed to the event handler
        :return: The clicked signal is being emitted.
        """
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonPress)
            # SET FOCUS
            self.setFocus()
            # EMIT SIGNAL
            return self.clicked.emit()
        return None

    # MOUSE RELEASED
    # Event triggered after the mouse button is released
    # ///////////////////////////////////////////////////////////////
    def mouseReleaseEvent(self, event):
        """
        If the left mouse button is released, change the style of the button and emit a signal

        :param event: The event object that was passed to the event handler
        :return: The signal is being returned.
        """
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonRelease)
            # EMIT SIGNAL
            return self.released.emit()
        return None

    # DRAW ICON WITH COLORS
    # ///////////////////////////////////////////////////////////////
    def icon_paint(self, qp, image, rect):
        """
        It takes an image, paints it with a color, and then draws it on the screen

        :param qp: QPainter object
        :param image: The image to be painted
        :param rect: The rectangle that the icon is being drawn in
        """
        icon = QPixmap(image)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        if self._is_active:
            painter.fillRect(icon.rect(), self._icon_color_active)
        else:
            painter.fillRect(icon.rect(), self._set_icon_color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()

    # SET ICON
    # ///////////////////////////////////////////////////////////////
    def set_icon(self, icon_path):
        """
        It sets the icon path to the icon_path argument, and then repaints the window

        :param icon_path: The path to the icon you want to use
        """
        self._set_icon_path = icon_path
        self.repaint()

    # MOVE TOOLTIP
    # ///////////////////////////////////////////////////////////////
    def move_tooltip(self):
        """It moves the tooltip to the right of the widget, and down by the height of the top margin"""
        # GET MAIN WINDOW PARENT
        gp = self.mapToGlobal(QPoint(0, 0))

        # SET WIDGET TO GET POSTION
        # Return absolute position of widget inside app
        pos = self._parent.mapFromGlobal(gp)

        # FORMAT POSITION
        # Adjust tooltip position with offset
        pos_x = (pos.x() - self._tooltip.width()) + self.width() + 5
        pos_y = pos.y() + self._top_margin

        # SET POSITION TO WIDGET
        # Move tooltip position
        self._tooltip.move(pos_x, pos_y)


# TOOLTIP
# ///////////////////////////////////////////////////////////////
# This class is a QLabel that displays a tooltip when the mouse hovers over it
class _ToolTip(QLabel):
    # TOOLTIP / LABEL StyleSheet
    style_tooltip = """
    QLabel {{
        background-color: {_dark_one};
        color: {_text_foreground};
        padding-left: 10px;
        padding-right: 10px;
        border-radius: 17px;
        border: 0px solid transparent;
        border-right: 3px solid {_context_color};
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
