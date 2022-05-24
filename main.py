# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////
import sys
import os

# IMPORT PYSIDE CORE
# ///////////////////////////////////////////
from pyside_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT MAIN FUNCTIONS
# ///////////////////////////////////////////
from gui.uis.windows.main_window.functions_main_window import MainFunctions

# IMPORT WIDGETS
# ///////////////////////////////////////////
from gui.widgets import *

# IMPORT INTERFACE
# ///////////////////////////////////////////
from gui.uis.windows.main_window.ui_interface_personal import Ui_MainWindow

# ADJUST QT FONT DPI FOR HIGH SCALE
# ///////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"

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

        # LOAD SETTINGS
        # ///////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////
        self.hide_grips = True  # Show/Hide resize grips
        self.custom_settings()
        self.ui.setup_gui()

        self.show()

    # CUSTOM PARAMETERS FOR WINDOW
    # ///////////////////////////////////////////
    def custom_settings(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])

        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)


if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////
    app = QApplication(sys.argv)
    # app.setWindowIcon()
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////
    sys.exit(app.exec())
