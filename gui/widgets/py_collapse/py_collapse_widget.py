# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////
from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame, QHBoxLayout, QLabel
from PySide6.QtCore import Signal, QPoint, QPointF
from PySide6.QtGui import QPainter, QColor


class FrameLayout(QWidget):
    """It creates a frame layout."""

    def __init__(self, parent=None, title=None):
        QWidget.__init__(self, parent=parent)

        self._is_collasped = True
        self.title_frame = None
        self._content, self._content_layout = (None, None)

        self._main_v_layout = QVBoxLayout(self)
        self._main_v_layout.addWidget(self.initTitleFrame(title, self._is_collasped))
        self._main_v_layout.addWidget(self.initContent(self._is_collasped))

        self.initCollapsable()

    def initTitleFrame(self, title, collapsed):
        """
        It creates a title frame with a title and a collapsed state

        :param title: The title of the frame
        :param collapsed: If True, the frame will be collapsed when it is created
        :return: The title_frame is being returned.
        """
        self.title_frame = self.TitleFrame(title=title, collapsed=collapsed)
        return self.title_frame

    def initContent(self, collapsed):
        """
        It creates a QWidget, sets its style sheet, creates a QVBoxLayout, sets the layout of the QWidget to the
        QVBoxLayout, sets the visibility of the QWidget to the opposite of the collapsed parameter, and returns the QWidget.

        :param collapsed: Boolean value that determines whether the widget is collapsed or not
        :return: The content of the widget.
        """
        self._content = QWidget()
        self._content.setStyleSheet("border-radius: 8px; background-color: #343b48;")
        self._content_layout = QVBoxLayout()

        self._content.setLayout(self._content_layout)
        self._content.setVisible(not collapsed)

        return self._content

    def addWidget(self, widget):
        """
        It adds a widget to the layout of the current widget

        :param widget: The widget to add to the layout
        """
        self._content_layout.addWidget(widget)

    def initCollapsable(self):
        """When the title frame is clicked, the toggleCollapsed function is called"""
        self.title_frame.clicked.connect(self.toggleCollapsed)

    def toggleCollapsed(self):
        """It sets the visibility of the content frame to the opposite of the current visibility"""
        self._content.setVisible(self._is_collasped)
        self._is_collasped = not self._is_collasped
        self.title_frame.arrow.setArrow(int(self._is_collasped))

    class TitleFrame(QFrame):
        """It's a frame with a title"""

        clicked = Signal(str)

        def __init__(self, parent=None, title="", collapsed=False):
            QFrame.__init__(self, parent=parent)

            self.setMinimumHeight(40)
            self.setMaximumHeight(50)
            self.move(QPoint(24, 0))
            self.setStyleSheet("border-radius: 8px;background-color: #1b1e23;")

            self._hlayout = QHBoxLayout(self)
            self._hlayout.setContentsMargins(0, 0, 0, 0)
            self._hlayout.setSpacing(0)

            self.arrow = None
            self._title = None

            self._hlayout.addWidget(self.initArrow(collapsed))
            self._hlayout.addWidget(self.initTitle(title))

        def initArrow(self, collapsed):
            """
            It creates a FrameLayout.Arrow object, sets its collapsed property to the value of the collapsed parameter, and
            sets its style sheet to "border:0px"

            :param collapsed: Boolean value that determines whether the arrow is pointing up or down
            :return: The arrow is being returned.
            """
            self.arrow = FrameLayout.Arrow(collapsed=collapsed)
            self.arrow.setStyleSheet("border:0px")

            return self.arrow

        def initTitle(self, title=None):
            """
            It creates a label with the text "title" and sets the minimum height to 24, moves the label to the point (24,0),
            and sets the style sheet to "border:0px; color: #dce1ec"

            :param title: The title of the widget
            :return: The title of the widget.
            """
            self._title = QLabel(title)
            self._title.setMinimumHeight(24)
            self._title.move(QPoint(24, 0))
            self._title.setStyleSheet("border:0px; color: #dce1ec")

            return self._title

        def mousePressEvent(self, event):
            """
            The function emits a signal when the mouse is pressed on the title frame

            :param event: The event that was triggered
            :return: The super class of the TitleFrame class.
            """
            self.clicked.emit("clicked")

            return super(FrameLayout.TitleFrame, self).mousePressEvent(event)

        def change_title(self, new_title):
            """
            It takes a string as an argument, and sets the text of the title label to that string

            :param new_title: The new title to be displayed
            """
            self._title.setText(new_title)

    class Arrow(QFrame):
        """It's a subclass of QFrame that draws an arrow"""

        def __init__(self, parent=None, collapsed=False):
            QFrame.__init__(self, parent=parent)

            self.setMaximumSize(24, 24)

            # horizontal == 0
            self._arrow_horizontal = (QPointF(7.0, 8.0), QPointF(17.0, 8.0), QPointF(12.0, 13.0))
            # vertical == 1
            self._arrow_vertical = (QPointF(8.0, 7.0), QPointF(13.0, 12.0), QPointF(8.0, 17.0))
            # arrow
            self.m_arrow = None
            self.setArrow(int(collapsed))

        def setArrow(self, arrow_dir):
            """
            If the arrow_dir is True, then the arrow is vertical, otherwise it is horizontal

            :param arrow_dir: True for vertical, False for horizontal
            """
            if arrow_dir:
                self.m_arrow = self._arrow_vertical
            else:
                self.m_arrow = self._arrow_horizontal

        def paintEvent(self, event):  # skipcq: PYL-W0613
            """
            > Draws a polygon on the widget

            :param event: The paint event
            """
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(QColor(192, 192, 192))
            painter.setPen(QColor(64, 64, 64))
            painter.drawPolygon(self.m_arrow)
            painter.end()
