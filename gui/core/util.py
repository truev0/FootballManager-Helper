# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtGui import QGuiApplication


def get_screen_size():
    """
    It returns the size of the screen
    :return: The size of the screen.
    """
    # TODO verify for both screens
    return QGuiApplication.primaryScreen().geometry()
