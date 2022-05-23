# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////
import sys
import os

# IMPORT PYSIDE CORE
# ///////////////////////////////////////////
from pyside_core import *

# MAIN WINDOW
# ///////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.show()


if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////
    application = QApplication(sys.argv)
    application.setWindowIcon()
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////
    sys.exit(application.exec())