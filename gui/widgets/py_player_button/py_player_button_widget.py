# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import QDataStream, QEvent, QRect, Qt
from PySide6.QtGui import QBrush, QColor, QPainter, QPixmap
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QLabel, QPushButton

# IMPORT FUNCTIONS
# ///////////////////////////////////////////////////////////////

# PY PLAYER BUTTON
# ///////////////////////////////////////////////////////////////


# This class is a subclass of QPushButton that has a custom signal called clicked_with_player
class PyPlayerButton(QPushButton):

    def __init__(
        self,
        app_parent,
        icon_path=None,
        btn_id=None,
        bg_color="#4f973c",
        bg_color_hover="#dce1ec",
        bg_color_pressed="#f5f6f9",
        icon_color="#c3ccdf",
        icon_color_hover="#343b48",
        icon_color_pressed="272c36",
        icon_color_active="#1b1e23",
        is_active=False,
    ):
        """
        The function takes in a bunch of parameters, sets some properties, and then sets some parameters

        :param app_parent: The parent of the button
        :param icon_path: The path to the icon you want to use
        :param btn_id: The name of the button
        :param bg_color: The background color of the button, defaults to #4f973c (optional)
        :param bg_color_hover: The background color of the button when the mouse is over it, defaults to #dce1ec (optional)
        :param bg_color_pressed: The background color of the button when it is pressed, defaults to #f5f6f9 (optional)
        :param icon_color: The color of the icon when the button is not active, defaults to #c3ccdf (optional)
        :param icon_color_hover: The color of the icon when the mouse is over the button, defaults to #343b48 (optional)
        :param icon_color_pressed: The color of the icon when the button is pressed, defaults to 272c36 (optional)
        :param icon_color_active: The color of the icon when the button is active, defaults to #1b1e23 (optional)
        :param is_active: If True, the button will be active, defaults to False (optional)
        """
        super().__init__()

        # SET PARAMETERS
        self.__mousePressPos = None
        self.__mouseMovePos = None
        self.setFixedSize(48, 48)
        if app_parent is not None:
            self.setParent(app_parent)
        self.setCursor(Qt.PointingHandCursor)
        self.setObjectName(btn_id)
        self.setAcceptDrops(True)

        # PROPERTIES
        self._bg_color = bg_color
        self._bg_color_hover = bg_color_hover
        self._bg_color_pressed = bg_color_pressed

        self._icon_color = icon_color
        self._icon_color_hover = icon_color_hover
        self._icon_color_pressed = icon_color_pressed
        self._icon_color_active = icon_color_active
        self._top_margin = 40
        self._is_active = is_active
        # Set Parameters
        self._set_bg_color = bg_color
        self._set_icon_path = icon_path
        self._set_icon_color = icon_color
        self._set_border_radius = 8
        # Parent
        self._parent = app_parent

        # Custom attributes
        self._lista = []
        self._text = ""

    # SET EMPTY LIST
    # ///////////////////////////////////////////////////////////////
    def set_empty_list(self):
        """It sets the list to an empty list"""
        self._lista = []

    # GET LEN LISTA
    # ///////////////////////////////////////////////////////////////
    def get_len_lista(self):
        """
        It returns the length of the list
        :return: The length of the list.
        """
        return len(self._lista)

    # GET LISTA
    # ///////////////////////////////////////////////////////////////
    def get_lista(self):
        """
        It returns the list
        :return: The list
        """
        return self._lista

    # FORMAT TEXT
    # ///////////////////////////////////////////////////////////////
    def text_formatter(self):
        """
        It takes a list of strings, joins them together with a newline character, and returns the result
        :return: The text formatter is returning the text that is being created in the list.
        """
        self._text = "\n".join([str(x) for x in self._lista])
        tmp = self._text
        return tmp

    # DRAG ENTER EVENT VERIFIER
    # ///////////////////////////////////////////////////////////////
    def dragEnterEvent(self, event):  # skipcq: PYL-R0201
        """
        If the data being dragged is a list of items, accept the drag event

        :param event: The event object
        """
        if "application/x-qabstractitemmodeldatalist" in event.mimeData(
        ).formats():
            event.accept()
        else:
            event.ignore()

    # DROP EVENT
    # ///////////////////////////////////////////////////////////////
    def dropEvent(self, event):
        """
        It reads the data from the drag and drop event and appends it to the list

        :param event: The event object that contains the information about the drop
        """
        mime_data = event.mimeData()
        if mime_data.hasText():
            if mime_data.text() not in self._lista:
                self._lista.append(mime_data.text())
        elif "application/x-qabstractitemmodeldatalist" in mime_data.formats():
            stream = QDataStream(
                mime_data.data("application/x-qabstractitemmodeldatalist"))
            while not stream.atEnd():
                # All fields must be read, even if we don't use them
                _row = stream.readInt32()  # skipcq: PYL-W0612
                _col = stream.readInt32()  # skipcq: PYL-W0612
                for _ in range(stream.readInt32()):
                    role = stream.readInt32()
                    value = stream.readQVariant()
                    if role == Qt.DisplayRole and value not in self._lista:
                        self._lista.append(value)

    # SET ACTIVE MENU
    # ///////////////////////////////////////////////////////////////
    def set_active(self, is_active):
        """
        It sets the active state of the button and repaints it

        :param is_active: A boolean value that indicates whether the button is active or not
        """
        self._is_active = is_active
        self.repaint()

    # RETURN IF IS ACTIVE
    # ///////////////////////////////////////////////////////////////
    def is_active(self):
        """
        It returns the value of the variable _is_active.
        :return: The value of the variable _is_active
        """
        return self._is_active

    # PAINT EVENT
    # ///////////////////////////////////////////////////////////////
    def paintEvent(self, _event):
        """
        The function is called when the widget is updated. It creates a painter object, sets the render hint to
        antialiasing, sets the brush color to the background color, creates a rectangle, sets the pen to no pen, sets the
        brush to the brush color, draws a rounded rectangle, and ends the painter

        :param _event: The event that triggered the paintEvent
        """
        # PAINTER
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.RenderHint.Antialiasing)

        if self._is_active:
            # BRUSH
            brush = QBrush(QColor(self._bg_color_pressed))
        else:
            # BRUSH
            brush = QBrush(QColor(self._set_bg_color))

        # CREATE RECTANGLE
        rect = QRect(0, 0, self.width(), self.height())
        paint.setPen(Qt.NoPen)
        paint.setBrush(brush)
        paint.drawRoundedRect(rect, self._set_border_radius,
                              self._set_border_radius)

        # DRAW ICONS
        self.icon_paint(paint, self._set_icon_path, rect)

        # END PAINTER
        paint.end()

    # CHANGE STYLES
    # Function with custom styles
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
        > This function changes the style of the widget when the mouse enter the widget

        :param event: The event that occurred
        """
        self.change_style(QEvent.Enter)

    # MOUSE LEAVE
    # Event fired when the mouse leaves the BTN
    # ///////////////////////////////////////////////////////////////
    def leaveEvent(self, event):  # skipcq: PYL-W0613
        """
        > This function changes the style of the widget when the mouse leaves the widget

        :param event: The event that occurred
        """
        self.change_style(QEvent.Leave)

    # MOUSE PRESS
    # Event triggered when the left button is pressed
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        """
        If the left mouse button is pressed, the button's style is changed and a signal is emitted. If the right mouse
        button is pressed, the mouse position is saved and the event is passed to the parent class

        :param event: The event that was triggered
        :return: The clicked signal is being emitted.
        """
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonPress)
            # SET FOCUS
            self.setFocus()
            # EMIT SIGNAL
            return self.clicked.emit()
        if event.button() == Qt.RightButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()
            super(PyPlayerButton, self).mousePressEvent(event)
        return None

    # MOUSE RELEASED
    # Event triggered after the mouse button is released
    # ///////////////////////////////////////////////////////////////
    def mouseReleaseEvent(self, event):
        """
        If the left mouse button is released, emit a signal.

        :param event: The event object that was passed to the function
        :return: The return value is the signal that is emitted when the button is released.
        """
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonRelease)
            # EMIT SIGNAL
            return self.released.emit()
        if event.button() == Qt.RightButton:
            if self.__mousePressPos is not None:
                moved = event.globalPos() - self.__mousePressPos
                if moved.manhattanLength() > 3:
                    event.ignore()
                    return None
            super(PyPlayerButton, self).mouseReleaseEvent(event)
        return None

    # MOUSE MOVE EVENT
    # ///////////////////////////////////////////////////////////////
    def mouseMoveEvent(self, event):
        """
        If the mouse is being dragged with the right button, move the button to the new position

        :param event: The event object that was passed to the event handler
        """
        if event.buttons() == Qt.RightButton:
            curr_pos = self.mapToGlobal(self.pos())
            global_pos = event.globalPos()
            diff = global_pos - self.__mouseMovePos
            new_pos = self.mapFromGlobal(curr_pos + diff)
            if 31 < new_pos.y() < 744 and 30 < new_pos.x() < 476:
                self.move(new_pos)
                self.__mouseMovePos = global_pos

        super(PyPlayerButton, self).mouseMoveEvent(event)

    # DRAW ICON WITH COLORS
    # ///////////////////////////////////////////////////////////////
    def icon_paint(self, qp, image, rect):
        """
        It takes a QPixmap, paints it with a color, and then draws it on the screen

        :param qp: QPainter object
        :param image: The image to be painted
        :param rect: The rectangle that the icon is drawn in
        """
        icon = QPixmap(image)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        if self._is_active:
            painter.fillRect(icon.rect(), self._icon_color_active)
        else:
            painter.fillRect(icon.rect(), self._set_icon_color)
        qp.drawPixmap((rect.width() - icon.width()) / 2,
                      (rect.height() - icon.height()) / 2, icon)
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


# This class is a QLabel that displays a tooltip when the mouse hovers over it
class _ToolTip(QLabel):
    # TOOLTIP / LABEL StyleSheet
    # ///////////////////////////////////////////////////////////////
    style_tooltip = """
        QLabel {{
        background-color: {_dark_one};
        color: {_text_foreground};
        padding-left: 10px;
        padding-right: 10px;
        border-radius: 17px;
        border: 0px solid transparent;
        font: 800 9pt "Segoe UI";
    }}
    """

    def __init__(self, parent, tooltip, dark_one, text_foreground):
        """
        I'm creating a QLabel, setting its style, setting its parent, setting its text, and then setting a drop shadow

        :param parent: The parent widget of the tooltip
        :param tooltip: The text to be displayed in the tooltip
        :param dark_one: the background color of the parent widget
        :param text_foreground: The color of the text in the tooltip
        """
        QLabel.__init__(self)

        # LABEL SETUP
        style = self.style_tooltip.format(_dark_one=dark_one,
                                          _text_foreground=text_foreground)
        self.setObjectName("label_tooltip")
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
