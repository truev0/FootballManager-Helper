# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import Property, QEasingCurve, QPoint, QPropertyAnimation, QRect, Qt
from PySide6.QtGui import QColor, QFont, QPainter
from PySide6.QtWidgets import QCheckBox


# It's a checkbox that can be toggled on and off
class PyToggle(QCheckBox):

    def __init__(
        self,
        name,
        width=50,
        bg_color="#777",
        circle_color="#DDD",
        active_color="#00BCFF",
        animation_curve=QEasingCurve.OutBounce,
    ):
        """
        The function takes in a bunch of arguments, and then sets up the animation

        :param name: The name of the checkbox
        :param width: The width of the checkbox, defaults to 50 (optional)
        :param bg_color: The background color of the checkbox, defaults to #777 (optional)
        :param circle_color: The color of the circle when the checkbox is not checked, defaults to #DDD (optional)
        :param active_color: The color of the circle when the checkbox is checked, defaults to #00BCFF (optional)
        :param animation_curve: The animation curve for the animation
        """
        QCheckBox.__init__(self)
        self.name = name
        self.setFixedSize(width, 28)
        self.setCursor(Qt.PointingHandCursor)

        # COLORS
        self._bg_color = bg_color
        self._circle_color = circle_color
        self._active_color = active_color

        self._position = 3
        self.animation = QPropertyAnimation(self, b"position")
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(500)
        self.stateChanged.connect(self.setup_animation)

    @Property(float)
    def position(self):
        """
        It returns the position.
        :return: The position.
        """
        return self._position

    @position.setter
    def position(self, pos):
        """
        The function position() takes in a position (pos) and sets the position of the object to that position

        :param pos: The position of the widget
        """
        self._position = pos
        self.update()

    # START STOP ANIMATION
    def setup_animation(self, value):
        """
        If the value is true, the animation will end at the width of the widget minus 26 pixels. If the value is false, the
        animation will end at 4 pixels

        :param value: The value of the checkbox
        """
        self.animation.stop()
        if value:
            self.animation.setEndValue(self.width() - 26)
        else:
            self.animation.setEndValue(4)
        self.animation.start()

    def hitButton(self, pos: QPoint):
        """
        If the point is within the rectangle, return True, otherwise return False

        :param pos: QPoint
        :type pos: QPoint
        :return: The contentsRect() is being returned.
        """
        return self.contentsRect().contains(pos)

    def paintEvent(self, e):  # skipcq: PYL-W0613
        """
        > The function draws a rounded rectangle and an ellipse on the widget

        :param e: The event object
        """
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setFont(QFont("Segoe UI", 9))

        # SET PEN
        p.setPen(Qt.NoPen)

        # DRAW RECT
        rect = QRect(0, 0, self.width(), self.height())

        if not self.isChecked():
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect(0, 0, rect.width(), 28, 14, 14)
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._position, 3, 22, 22)
        else:
            p.setBrush(QColor(self._active_color))
            p.drawRoundedRect(0, 0, rect.width(), 28, 14, 14)
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._position, 3, 22, 22)

        p.end()

    def get_name(self):
        """
        The function get_name() returns the value of the attribute name of the object self
        :return: The name of the person.
        """
        return self.name
