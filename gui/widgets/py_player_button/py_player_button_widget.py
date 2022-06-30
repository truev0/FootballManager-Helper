# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import QDataStream, QEvent, QRect, Qt
from PySide6.QtGui import QBrush, QColor, QPainter, QPixmap
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QLabel, QPushButton

# IMPORT FUNCTIONS
# ///////////////////////////////////////////////////////////////

# PY PLAYER BUTTON
# ///////////////////////////////////////////////////////////////


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
        self._lista = []

    # GET LEN LISTA
    # ///////////////////////////////////////////////////////////////
    def get_len_lista(self):
        return len(self._lista)

    # FORMAT TEXT
    # ///////////////////////////////////////////////////////////////
    def text_formatter(self):
        self._text = "\n".join([str(x) for x in self._lista])
        tmp = self._text
        return tmp

    # DRAG ENTER EVENT VERIFIER
    # ///////////////////////////////////////////////////////////////
    def dragEnterEvent(self, event):
        if "application/x-qabstractitemmodeldatalist" in event.mimeData(
        ).formats():
            event.accept()
        else:
            event.ignore()

    # DROP EVENT
    # ///////////////////////////////////////////////////////////////
    def dropEvent(self, event):
        mime_data = event.mimeData()
        if mime_data.hasText():
            self._lista.append(mime_data.text())
        elif "application/x-qabstractitemmodeldatalist" in mime_data.formats():
            names = []
            stream = QDataStream(
                mime_data.data("application/x-qabstractitemmodeldatalist"))
            while not stream.atEnd():
                # All fields must be read, even if we don't use them
                row = stream.readInt32()  # skipcq: PYL-W0612
                col = stream.readInt32()  # skipcq: PYL-W0612
                for _ in range(stream.readInt32()):
                    role = stream.readInt32()
                    value = stream.readQVariant()
                    if role == Qt.DisplayRole and value not in names:
                        names.append(value)
            self._lista.extend(names)

    # SET ACTIVE MENU
    # ///////////////////////////////////////////////////////////////
    def set_active(self, is_active):
        self._is_active = is_active
        self.repaint()

    # RETURN IF IS ACTIVE
    # ///////////////////////////////////////////////////////////////
    def is_active(self):
        return self._is_active

    # PAINT EVENT
    # ///////////////////////////////////////////////////////////////
    def paintEvent(self, event):
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
        self.change_style(QEvent.Enter)

    # MOUSE LEAVE
    # Event fired when the mouse leaves the BTN
    # ///////////////////////////////////////////////////////////////
    def leaveEvent(self, event):  # skipcq: PYL-W0613
        self.change_style(QEvent.Leave)

    # MOUSE PRESS
    # Event triggered when the left button is pressed
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
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

    # MOUSE RELEASED
    # Event triggered after the mouse button is released
    # ///////////////////////////////////////////////////////////////
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonRelease)
            # EMIT SIGNAL
            return self.released.emit()
        if event.button() == Qt.RightButton:
            if self.__mousePressPos is not None:
                moved = event.globalPos() - self.__mousePressPos
                if moved.manhattanLength() > 3:
                    event.ignore()
                    return
            super(PyPlayerButton, self).mouseReleaseEvent(event)

    # MOUSE MOVE EVENT
    # ///////////////////////////////////////////////////////////////
    def mouseMoveEvent(self, event):
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
        self._set_icon_path = icon_path
        self.repaint()


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
