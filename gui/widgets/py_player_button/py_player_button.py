# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from pyside_core import *

# IMPORT PY ICON BUTTON
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_icon_button import PyIconButton

# IMPORT FUNCTIONS
# ///////////////////////////////////////////////////////////////
from gui.core.functions import *

# PY PLAYER BUTTON
# ///////////////////////////////////////////////////////////////


class PyPlayerButton(QPushButton):
    def __init__(
            self,
            icon_path=None,
            parent=None,
            app_parent=None,
            btn_id=None,
            bg_color="#4f973c",
            bg_color_hover="#dce1ec",
            bg_color_pressed="#f5f6f9",
            icon_color="#c3ccdf",
            icon_color_hover="#343b48",
            icon_color_pressed="272c36",
            icon_color_active="#1b1e23",
            tooltip_text="                               ",
            dark_one="#1b1e23",
            text_foreground="#8a95aa",
            is_active=False,
    ):
        super().__init__()

        # SET PARAMETERS
        self.setFixedSize(48, 48)
        if parent != None:
            self.setParent(parent)
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
        self._parent = parent
        self._app_parent = app_parent

        # Custom attributes
        self._lista = []

        # # CUSTOM PLAYER WINDOW
        # self._container_player = _CustomListPlayer(
        #     tooltip_text,
        #     dark_one,
        #     text_foreground,
        # )
        # self._container_player.hide()

        # TODO continuar con el cuadro custom

        # TOOLTIP
        self._tooltip_text = tooltip_text
        self._tooltip = _ToolTip(
            parent,
            tooltip_text,
            dark_one,
            text_foreground
        )
        self._tooltip.hide()


    # DRAG ENTER EVENT VERIFIER
    # ///////////////////////////////////////////////////////////////
    def dragEnterEvent(self, event):
        if 'application/x-qabstractitemmodeldatalist' in event.mimeData().formats():
            event.accept()
        else:
            event.ignore()


    # DROP EVENT
    # ///////////////////////////////////////////////////////////////
    def dropEvent(self, event):
        mimeData = event.mimeData()
        if mimeData.hasText():
            self._lista.append(mimeData.text())
        elif 'application/x-qabstractitemmodeldatalist' in mimeData.formats():
            names = []
            stream = QDataStream(mimeData.data('application/x-qabstractitemmodeldatalist'))
            while not stream.atEnd():
                # All fields must be read, even if we don't use them
                row = stream.readInt32()
                col = stream.readInt32()
                for _ in range(stream.readInt32()):
                    role = stream.readInt32()
                    value = stream.readQVariant()
                    if role == Qt.DisplayRole:
                        names.append(value)
            self._lista.extend(names)
        self.updater_height = self._tooltip.height() + 12
        self.update_width = 150
        self._tooltip.resize(self.update_width, self.updater_height)
        self._tooltip.setText("\n".join(self._lista))
        print(self._lista)

    # SET ACTIVE MENU
    # ///////////////////////////////////////////////////////////////
    def set_active(self, is_active):
        self._is_active = is_active
        self.repaint()

    # RETURN IF IS ACTIVE
    # ///////////////////////////////////////////////////////////////
    def is_active(self, is_active):
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
    def enterEvent(self, event):
        self.change_style(QEvent.Enter)
        self.move_tooltip()
        # print(self._tooltip.height(), self._tooltip.width())
        print(self.players_container.height(), self.players_container.width())
        # self._tooltip.show()

    # MOUSE LEAVE
    # Event fired when the mouse leaves the BTN
    # ///////////////////////////////////////////////////////////////
    def leaveEvent(self, event):
        self.change_style(QEvent.Leave)
        self.move_tooltip()
        # self._tooltip.hide()

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
            self.players_container.slideMenu()
            # EMIT SIGNAL
            return self.clicked.emit()
        elif event.button() == Qt.RightButton:
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
        elif event.button() == Qt.RightButton:
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
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)

            self.__mouseMovePos = globalPos
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
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()

    # SET ICON
    # ///////////////////////////////////////////////////////////////
    def set_icon(self, icon_path):
        self._set_icon_path = icon_path
        self.repaint()


    # MOVE TOOLTIP
    # ///////////////////////////////////////////////////////////////
    def move_tooltip(self):
        # GET MAIN WINDOW
        gp = self.mapToGlobal(QPoint(0, 0))
        # SET DIGET TO GET POSITION
        # Return absolute position of the widget relative to the app
        pos = self._parent.mapFromGlobal(gp)

        # FORMAT POSITION
        # Adjust the position of the tooltip
        pos_x = (pos.x() - (self._tooltip.width() // 2)) + (self.width() // 2)
        pos_y = pos.y() - self._top_margin

        # SET POSITION TO WIDGET
        # Move tooltip position
        self._tooltip.move(pos_x, pos_y)

class _CustomListPlayer(QWidget):
    def __init__(
            self,
            parent,
            tooltip,
            dark_one,
            text_foreground
    ):
        QWidget.__init__(self)
        self.setParent(parent)
        self.setObjectName(u"CustomListPlayer")
        self.setMinimumHeight(40)
        self.setMinimumWidth(150)
        self.main_container_layout = QVBoxLayout(self)
        self.main_container_layout.setObjectName(u"main_container_layout")

        self.subContainer = QWidget(self)
        self.subContainer.setObjectName(u"subContainer")
        self.subContainer_layout = QVBoxLayout(self.subContainer)
        self.subContainer_layout.setObjectName(u"subContainer_layout")

        self.top_label = QLabel(self.subContainer)
        self.top_label.setObjectName(u"top_label")
        font = QFont()
        font.setBold(True)
        self.top_label.setFont(font)

        self.subContainer_layout.addWidget(self.top_label)

        self.frame_player = QFrame(self.subContainer)
        self.frame_player.setObjectName(u"frame_player")
        self.frame_player.setFrameShape(QFrame.StyledPanel)
        self.frame_player.setFrameShadow(QFrame.Raised)
        self.frame_player_layout = QHBoxLayout(self.frame_player)
        self.frame_player_layout.setObjectName(u"frame_player_layout")
        self.label_list_player = QLabel(self.frame_player)
        self.label_list_player.setObjectName(u"label_list_player")
        self.label_list_player.setAlignment(Qt.AlignCenter)
        self.label_list_player.setText(tooltip)
        self.frame_player_layout.addWidget(self.label_list_player)

        self.closeContainerBtn = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_close.svg"),
            parent=self.frame_player,
            tooltip_text="close",
            width=24,
            height=24,
            radius=8,
            bg_color="#FF00000"
        )

        self.frame_player_layout.addWidget(self.closeContainerBtn)
        self.subContainer_layout.addWidget(self.frame_player)
        self.main_container_layout.addWidget(self.subContainer)



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

    def __init__(
            self,
            parent,
            tooltip,
            dark_one,
            text_foreground
    ):
        QLabel.__init__(self)

        # LABEL SETUP
        style = self.style_tooltip.format(
            _dark_one=dark_one,
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
