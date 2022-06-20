from pyside_core import *


def get_screen_size():
    return QGuiApplication.primaryScreen().geometry()
