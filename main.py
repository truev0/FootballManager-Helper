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

# IMPORT FUNCTIONS
# ///////////////////////////////////////////
from gui.core.functions import Functions

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
        self.set_signals()

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

    # LEFT MENU BTN IS CLICKED
    def btn_clicked(self):
        # GET BTN CLICKED
        btn = self.ui.setup_btns()

        # Remove selection if Clicked by "btn_close_left_column"
        if btn.objectName() != "btn_settings":
            self.ui.left_menu.deselect_all_tab()

        # Get title bar btn and reset active
        top_settings = self.ui.get_title_bar_btn("btn_top_settings")
        top_settings.set_active(False)

        # LEFT MENU
        # ///////////////////////////////////////////
        # Home Btn
        if btn.objectName() == "btn_home":
            # Select menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page 1
            self.ui.set_page(self.ui.load_pages.page_1)

        # Squad Btn
        if btn.objectName() == "btn_squad":
            # Select menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page 2
            self.ui.set_page(self.ui.load_pages.page_2)

        # Tactic Btn
        if btn.objectName() == "btn_tactic":
            # Select menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page x

        # Development Btn
        if btn.objectName() == "btn_development":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page x

        # Stats Btn
        if btn.objectName() == "btn_stats":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page x

        # Metrics Btn
        if btn.objectName() == "btn_metrics":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page x

        # Compare Btn
        if btn.objectName() == "btn_compare":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page x

        # Scouting Btn
        if btn.objectName() == "btn_scouting":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page x

        # Employees Btn
        if btn.objectName() == "btn_employees":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page x

        # Help Btn
        if btn.objectName() == "btn_help":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page x

        # Information Btn
        if btn.objectName() == "btn_info":
            # Check if left column is visible
            if not self.ui.left_column_is_visible():
                self.ui.left_menu.select_only_one_tab(btn.objectName())

                # Show / Hide
                self.ui.toggle_left_column()
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    self.ui.toggle_left_column()
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change left column menu
            if btn.objectName() != "btn_close_left_column":
                self.ui.set_left_column_menu(
                    menu=self.ui.left_column.menus.menu_2,
                    title="Info tab",
                    icon_path=Functions.set_svg_icon("icon_info.svg")
                )

        # Settings left
        if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
            # Check if left column is visible
            if not self.ui.left_column_is_visible():
                # Show / Hide
                self.ui.toggle_left_column()
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    self.ui.toggle_left_column()
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            if btn.objectName() != "btn_close_left_column":
                self.ui.set_left_column_menu(
                    menu=self.ui.left_column.menus.menu_1,
                    title="Settings left column",
                    icon_path=Functions.set_svg_icon("icon_settings.svg")
                )

        # TITLE BAR MENU
        # ///////////////////////////////////////////
        # Settings title bar
        if btn.objectName() == "btn_top_settings":
            # Toggle active
            if not self.ui.right_column_is_visible():
                btn.set_active(True)

                # Show / Hide
                self.ui.toggle_right_column()
            else:
                btn.set_active(False)

                # Show / Hide
                self.ui.toggle_right_column()

            # Get left menu btn
            top_settings = self.ui.get_left_menu_btn("btn_settings")
            top_settings.set_active_tab(False)

        # DEBUG

        print(f"Button {btn.objectName()}, clicked!")

    # LEFT MENU BTN IS RELEASED
    # Check function by object name / btn_id
    # ///////////////////////////////////////////
    def btn_released(self):
        # GET BTN CLICKED
        btn = self.ui.setup_btns()

        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    # SET ALL SIGNALS
    # ///////////////////////////////////////////
    def set_signals(self):
        # LEFT MENU SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # LEFT COLUMN SIGNALS
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

    # RESIZE EVENT
    # ///////////////////////////////////////////
    def resizeEvent(self, event):
        # RESIZE GRIPS AND CHANGE POSITION
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos

# SETTINGS WHEN TO START
# Set initial class and also additional parameter of the "QApplication" class
# ///////////////////////////////////////////


if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////
    app = QApplication(sys.argv)
    # app.setWindowIcon()
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////
    sys.exit(app.exec())
