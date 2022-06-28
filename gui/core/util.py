# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtGui import QGuiApplication


def get_screen_size():
    return QGuiApplication.primaryScreen().geometry()
