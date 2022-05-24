# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////
import sys
import os

# IMPORT PYSIDE CORE
# ///////////////////////////////////////////
from pyside_core import *

# IMPORT INTERFACE
# ///////////////////////////////////////////
from gui.uis.windows.main_window.ui_interface_personal import Ui_MainWindow

# MAIN WINDOW
# ///////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOW
        # Load widgets from "gui\uis\main_window\ui_interface_personal.py"
        # ///////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.show()


if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////
    app = QApplication(sys.argv)
    # app.setWindowIcon()
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////
    sys.exit(app.exec())
