# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import QRect, QSize, Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QFrame, QSizeGrip, QWidget


# PY GRIPS
# ///////////////////////////////////////////////////////////////
class PyGrips(QWidget):
    """This class is a QWidget that contains Grips for application"""

    def __init__(self, parent, position, disable_color=False):
        """
        It creates a QSizeGrip object and attaches it to the parent widget

        :param parent: The parent widget
        :param position: This is the position of the grip. It can be top_left, top_right, bottom_left, bottom_right,
        top, bottom, left, or right
        :param disable_color: If set to True, the grip will be transparent, defaults to False (optional)
        """
        # SETUP UI
        # ///////////////////////////////////////////////////////////////
        super().__init__()
        self.mousePos = None
        self.parent = parent
        self.setParent(parent)
        self.wi = Widgets()
        self.common_background = "background: transparent;"

        # SHOW TOP LEFT GRIP
        # ///////////////////////////////////////////////////////////////
        if position == "top_left":
            self.wi.top_left(self)
            grip = QSizeGrip(self.wi.top_left_grip)
            grip.setFixedSize(self.wi.top_left_grip.size())
            self.setGeometry(5, 5, 15, 15)

            # ENABLE COLOR
            if disable_color:
                self.wi.top_left_grip.setStyleSheet(self.common_background)

        # SHOW TOP RIGHT GRIP
        # ///////////////////////////////////////////////////////////////
        if position == "top_right":
            self.wi.top_right(self)
            grip = QSizeGrip(self.wi.top_right_grip)
            grip.setFixedSize(self.wi.top_right_grip.size())
            self.setGeometry(self.parent.width() - 20, 5, 15, 15)

            # ENABLE COLOR
            if disable_color:
                self.wi.top_right_grip.setStyleSheet(self.common_background)

        # SHOW BOTTOM LEFT GRIP
        # ///////////////////////////////////////////////////////////////
        if position == "bottom_left":
            self.wi.bottom_left(self)
            grip = QSizeGrip(self.wi.bottom_left_grip)
            grip.setFixedSize(self.wi.bottom_left_grip.size())
            self.setGeometry(5, self.parent.height() - 20, 15, 15)

            # ENABLE COLOR
            if disable_color:
                self.wi.bottom_left_grip.setStyleSheet(self.common_background)

        # SHOW BOTTOM RIGHT GRIP
        # ///////////////////////////////////////////////////////////////
        if position == "bottom_right":
            self.wi.bottom_right(self)
            grip = QSizeGrip(self.wi.bottom_right_grip)
            grip.setFixedSize(self.wi.bottom_right_grip.size())
            self.setGeometry(self.parent.width() - 20,
                             self.parent.height() - 20, 15, 15)

            # ENABLE COLOR
            if disable_color:
                self.wi.bottom_right_grip.setStyleSheet(self.common_background)

        # SHOW TOP GRIP
        # ///////////////////////////////////////////////////////////////
        if position == "top":
            self.wi.top(self)
            self.setGeometry(0, 5, self.parent.width(), 10)
            self.setMaximumHeight(10)

            # RESIZE TOP
            def resize_top(event):
                delta = event.pos()
                height = max(self.parent.minimumHeight(),
                             self.parent.height() - delta.y())
                geo = self.parent.geometry()
                geo.setTop(geo.bottom() - height)
                self.parent.setGeometry(geo)
                event.accept()

            self.wi.top_grip.mouseMoveEvent = resize_top

            # ENABLE COLOR
            if disable_color:
                self.wi.top_grip.setStyleSheet(self.common_background)

        # SHOW BOTTOM GRIP
        # ///////////////////////////////////////////////////////////////
        elif position == "bottom":
            self.wi.bottom(self)
            self.setGeometry(0,
                             self.parent.height() - 10, self.parent.width(),
                             10)
            self.setMaximumHeight(10)

            # RESIZE BOTTOM
            def resize_bottom(event):
                delta = event.pos()
                height = max(self.parent.minimumHeight(),
                             self.parent.height() + delta.y())
                self.parent.resize(self.parent.width(), height)
                event.accept()

            self.wi.bottom_grip.mouseMoveEvent = resize_bottom

            # ENABLE COLOR
            if disable_color:
                self.wi.bottom_grip.setStyleSheet(self.common_background)

        # SHOW LEFT GRIP
        # ///////////////////////////////////////////////////////////////
        elif position == "left":
            self.wi.left(self)
            self.setGeometry(0, 10, 10, self.parent.height())
            self.setMaximumWidth(10)

            # RESIZE LEFT
            def resize_left(event):
                delta = event.pos()
                width = max(self.parent.minimumWidth(),
                            self.parent.width() - delta.x())
                geo = self.parent.geometry()
                geo.setLeft(geo.right() - width)
                self.parent.setGeometry(geo)
                event.accept()

            self.wi.left_grip.mouseMoveEvent = resize_left

            # ENABLE COLOR
            if disable_color:
                self.wi.left_grip.setStyleSheet(self.common_background)

        # RESIZE RIGHT
        # ///////////////////////////////////////////////////////////////
        elif position == "right":
            self.wi.right(self)
            self.setGeometry(self.parent.width() - 10, 10, 10,
                             self.parent.height())
            self.setMaximumWidth(10)

            def resize_right(event):
                delta = event.pos()
                width = max(self.parent.minimumWidth(),
                            self.parent.width() + delta.x())
                self.parent.resize(width, self.parent.height())
                event.accept()

            self.wi.right_grip.mouseMoveEvent = resize_right

            # ENABLE COLOR
            if disable_color:
                self.wi.right_grip.setStyleSheet(self.common_background)

    # MOUSE RELEASE
    # ///////////////////////////////////////////////////////////////
    def mouseReleaseEvent(self, event):  # skipcq: PYL-W0613
        """
        > The function `mouseReleaseEvent` is a member of the class `QtGui.QWidget` and is called when the mouse button
        is released

        :param event: the event that triggered the method
        """
        self.mousePos = None

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):  # skipcq: PYL-W0613
        """
        It checks if the widget has a top_grip, bottom_grip, left_grip, right_grip, top_right_grip, bottom_left_grip, or
        bottom_right_grip attribute, and if it does, it sets the geometry of that attribute to the appropriate size

        :param event: The event object that was passed to the event handler
        """
        if hasattr(self.wi, "top_grip"):
            self.wi.top_grip.setGeometry(0, 0, self.width(), 10)

        elif hasattr(self.wi, "bottom_grip"):
            self.wi.bottom_grip.setGeometry(0, 0, self.width(), 10)

        elif hasattr(self.wi, "left_grip"):
            self.wi.left_grip.setGeometry(0, 0, 10, self.height() - 20)

        elif hasattr(self.wi, "right_grip"):
            self.wi.right_grip.setGeometry(0, 0, 10, self.height() - 20)

        elif hasattr(self.wi, "top_right_grip"):
            self.wi.top_right_grip.setGeometry(self.width() - 15, 0, 15, 15)

        elif hasattr(self.wi, "bottom_left_grip"):
            self.wi.bottom_left_grip.setGeometry(0, self.height() - 15, 15, 15)

        elif hasattr(self.wi, "bottom_right_grip"):
            self.wi.bottom_right_grip.setGeometry(self.width() - 15,
                                                  self.height() - 15, 15, 15)


# GRIP WIDGTES
# ///////////////////////////////////////////////////////////////
class Widgets:
    """Widgets are objects for grips"""

    def top_left(self, form):
        """
        It creates a frame in the top left corner of the window.

        :param form: The form that the grip is being added to
        """
        self.top_left_grip = QFrame(form)  # skipcq: PYL-W0201
        self.top_left_grip.setObjectName("top_left_grip")
        self.top_left_grip.setFixedSize(15, 15)
        self.top_left_grip.setStyleSheet(
            "background-color: #333; border: 2px solid #55FF00;")

    def top_right(self, form):
        """
        It creates a frame in the top right corner of the window.

        :param form: The form that the grip is being added to
        """
        self.top_right_grip = QFrame(form)  # skipcq: PYL-W0201
        self.top_right_grip.setObjectName("top_right_grip")
        self.top_right_grip.setFixedSize(15, 15)
        self.top_right_grip.setStyleSheet(
            "background-color: #333; border: 2px solid #55FF00;")

    def bottom_left(self, form):
        """
        It creates a frame in the bottom left corner of the window.

        :param form: The form that the grip is being added to
        """
        self.bottom_left_grip = QFrame(form)  # skipcq: PYL-W0201
        self.bottom_left_grip.setObjectName("bottom_left_grip")
        self.bottom_left_grip.setFixedSize(15, 15)
        self.bottom_left_grip.setStyleSheet(
            "background-color: #333; border: 2px solid #55FF00;")

    def bottom_right(self, form):
        """
        It creates a frame that is 15x15 pixels in size and sets the background color to #333 and the border to 2px
        solid #55FF00.

        :param form: The form that the grip is being added to
        """
        self.bottom_right_grip = QFrame(form)  # skipcq: PYL-W0201
        self.bottom_right_grip.setObjectName("bottom_right_grip")
        self.bottom_right_grip.setFixedSize(15, 15)
        self.bottom_right_grip.setStyleSheet(
            "background-color: #333; border: 2px solid #55FF00;")

    def top(self, form):
        """
        It creates a QFrame object, sets its geometry, style, and cursor, and then adds it to the form

        :param form: the form that the grip is being added to
        """
        self.top_grip = QFrame(form)  # skipcq: PYL-W0201
        self.top_grip.setObjectName("top_grip")
        self.top_grip.setGeometry(QRect(0, 0, 500, 10))
        self.top_grip.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.top_grip.setCursor(QCursor(Qt.SizeVerCursor))

    def bottom(self, form):
        """
        It creates a QFrame object, sets its geometry, style, and cursor, and then adds it to the form

        :param form: the form that the grip is being added to
        """
        self.bottom_grip = QFrame(form)  # skipcq: PYL-W0201
        self.bottom_grip.setObjectName("bottom_grip")
        self.bottom_grip.setGeometry(QRect(0, 0, 500, 10))
        self.bottom_grip.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.bottom_grip.setCursor(QCursor(Qt.SizeVerCursor))

    def left(self, form):
        """
        It creates a frame that is 10 pixels wide and 480 pixels high, and sets the cursor to a horizontal resize cursor

        :param form: the form that the grip is being added to
        """
        self.left_grip = QFrame(form)  # skipcq: PYL-W0201
        self.left_grip.setObjectName("left")
        self.left_grip.setGeometry(QRect(0, 10, 10, 480))
        self.left_grip.setMinimumSize(QSize(10, 0))
        self.left_grip.setCursor(QCursor(Qt.SizeHorCursor))
        self.left_grip.setStyleSheet("background-color: rgb(255, 121, 198);")

    def right(self, form):
        """
        It creates a QFrame object, sets its geometry, minimum size, cursor, and style sheet

        :param form: the parent widget
        """
        self.right_grip = QFrame(form)  # skipcq: PYL-W0201
        self.right_grip.setObjectName("right")
        self.right_grip.setGeometry(QRect(0, 0, 10, 500))
        self.right_grip.setMinimumSize(QSize(10, 0))
        self.right_grip.setCursor(QCursor(Qt.SizeHorCursor))
        self.right_grip.setStyleSheet("background-color: rgb(255, 0, 127);")
