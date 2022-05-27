# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////
import sys
import os
import json
import time

# IMPORT PYSIDE CORE
# ///////////////////////////////////////////
from pyside_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT FUNCTIONS
# ///////////////////////////////////////////
from gui.core.functions import Functions

# IMPORT FM INSIDE
# ///////////////////////////////////////////
import gui.core.fm_insider.FMinside as FMi

# IMPORT CUSTOM CLASSES
# ///////////////////////////////////////////
from gui.core.custom_classes.CustomNestedNamespace.py_CustomNestedNamespace import NestedNamespace
from gui.core.custom_classes.CustomNumpyTableModel.py_CustomNumpyTableModel import CustomizedNumpyModel
from gui.core.custom_classes.CustomNumpyListModel.py_CustomNumpyListModel import CustomizedNumpyListModel

# IMPORT TRANSLATIONS
# ///////////////////////////////////////////
from gui.core.translations import en, es

# IMPORT WIDGETS
# ///////////////////////////////////////////
from gui.widgets import *
from gui.widgets.py_title_bar.py_title_button import PyTitleButton

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

        # CLASS VARIABLES
        # ///////////////////////////////////////////
        self.dragPos = None
        self.df_squad = None
        self.bottom_right_grip = None
        self.bottom_left_grip = None
        self.top_right_grip = None
        self.top_left_grip = None
        self.bottom_grip = None
        self.top_grip = None
        self.right_grip = None
        self.left_grip = None
        self.ui_text = {}
        self.ui_text.update({'en': NestedNamespace(en.english)})
        self.ui_text.update({'es': NestedNamespace(es.espanol)})


        # LOAD SETTINGS
        # ///////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items
        self.language = 'en'

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////
        self.hide_grips = True  # Show/Hide resize grips
        self.custom_settings()
        self.ui.setup_gui()
        self.set_signals()
        self.connect_events()

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

            # Load page 3
            self.ui.set_page(self.ui.load_pages.page_3)

        # Development Btn
        if btn.objectName() == "btn_development":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page 4
            # self.ui.set_page(self.ui.load_pages.page_4)

        # Stats Btn
        if btn.objectName() == "btn_stats":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page 5
            # self.ui.set_page(self.ui.load_pages.page_5)

        # Metrics Btn
        if btn.objectName() == "btn_metrics":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page 6
            # self.ui.set_page(self.ui.load_pages.page_6)

        # Compare Btn
        if btn.objectName() == "btn_compare":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page 7
            # self.ui.set_page(self.ui.load_pages.page_7)

        # Scouting Btn
        if btn.objectName() == "btn_scouting":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page 8
            # self.ui.set_page(self.ui.load_pages.page_8)

        # Employees Btn
        if btn.objectName() == "btn_employees":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page 9
            # self.ui.set_page(self.ui.load_pages.page_9)

        # Help Btn
        if btn.objectName() == "btn_help":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page 10
            # self.ui.set_page(self.ui.load_pages.page_10)

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

        if btn.objectName() == "btn_refresh":
            # self.squad_helper()
            pass

        # DEBUG

        # print(f"Button {btn.objectName()}, clicked!")

    # LEFT MENU BTN IS RELEASED
    # Check function by object name / btn_id
    # ///////////////////////////////////////////
    def btn_released(self):
        # GET BTN CLICKED
        btn = self.ui.setup_btns()

        # DEBUG
        # print(f"Button {btn.objectName()}, released!")

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
        global_pos = p.toPoint()
        self.dragPos = global_pos

    # CONNECT EVENT CLICKS
    # ///////////////////////////////////////////
    def connect_events(self):
        self.ui.load_squad_btn.clicked.connect(lambda: self.load_file())
        self.ui.english_language_btn.clicked.connect(lambda: self.translate_lang('en'))
        self.ui.spanish_language_btn.clicked.connect(lambda: self.translate_lang('es'))

    # LOAD FILE
    # ///////////////////////////////////////////
    def load_file(self):
        # FILE DIALOG
        dlg_file = QFileDialog.getOpenFileName(
            self,
            caption="Select a file",
            filter="HTML Files (*.html)"
        )

        # READ FILE
        if dlg_file:
            self.df_squad = FMi.setting_up_pandas(dlg_file[0], 'squad_btn')
            self.df_squad = FMi.convert_values(self.df_squad, self.language)
            self.df_squad = FMi.create_metrics_for_gk(self.df_squad, self.language)
            self.df_squad = FMi.data_for_rankings(self.df_squad, self.language)
            self.df_squad = FMi.create_scores_for_position(self.df_squad, self.language)
            self.df_squad = FMi.round_data(self.df_squad)
            self.df_squad = FMi.ranking_values(self.df_squad)

        self.df_for_table = FMi.create_df_for_squad(self.df_squad, self.language)
        self.df_tactic = self.df_for_table.iloc[:, :1]
        self.tables_helper()

    # SQUAD HELPER FUNCTION
    # ///////////////////////////////////////////
    def tables_helper(self):
        inicio = time.time()
        model = CustomizedNumpyModel(self.df_for_table)
        column_indexes = [1, 3, 4, 5, 6, 7, 8, 10, 12]
        self.ui.table_squad.setSelectionBehavior(QTableView.SelectItems)
        self.ui.table_squad.setModel(model)
        self.ui.table_squad.show()
        headers = self.ui.table_squad.horizontalHeader()
        for c in column_indexes:
            headers.setSectionResizeMode(c, QHeaderView.ResizeToContents)

        model2 = CustomizedNumpyListModel(self.df_tactic)
        self.ui.table_tactic.setModel(model2)
        self.ui.table_tactic.show()
        self.ui.table_tactic.horizontalHeader().setStretchLastSection(True)

        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio}")


    # TRANSLATE UI
    # ///////////////////////////////////////////
    def translate_lang(self, lang):
        print("Translation")
        self.language = lang

        # Translating side menu buttons
        self.ui.left_menu.findChild(QPushButton, 'btn_home').setText(self.ui_text[lang].menu.o0)
        self.ui.left_menu.findChild(QPushButton, 'btn_squad').setText(self.ui_text[lang].menu.o1)
        self.ui.left_menu.findChild(QPushButton, 'btn_tactic').setText(self.ui_text[lang].menu.o2)
        self.ui.left_menu.findChild(QPushButton, 'btn_development').setText(self.ui_text[lang].menu.o3)
        self.ui.left_menu.findChild(QPushButton, 'btn_stats').setText(self.ui_text[lang].menu.o5)
        self.ui.left_menu.findChild(QPushButton, 'btn_metrics').setText(self.ui_text[lang].menu.o6)
        self.ui.left_menu.findChild(QPushButton, 'btn_compare').setText(self.ui_text[lang].menu.o7)
        self.ui.left_menu.findChild(QPushButton, 'btn_scouting').setText(self.ui_text[lang].menu.o8)
        self.ui.left_menu.findChild(QPushButton, 'btn_employees').setText(self.ui_text[lang].menu.o9)
        self.ui.left_menu.findChild(QPushButton, 'btn_settings').setText(self.ui_text[lang].menu.o10)
        self.ui.left_menu.findChild(QPushButton, 'btn_info').setText(self.ui_text[lang].menu.o11)
        self.ui.left_menu.findChild(QPushButton, 'btn_help').setText(self.ui_text[lang].menu.o12)
        self.ui.left_menu.toggle_button.setText(self.ui_text[lang].menu.o4)

        # Translating side menu tooltips
        self.ui.left_menu.findChild(QPushButton, 'btn_home').change_tooltip(self.ui_text[lang].menu.t0)
        self.ui.left_menu.findChild(QPushButton, 'btn_squad').change_tooltip(self.ui_text[lang].menu.t1)
        self.ui.left_menu.findChild(QPushButton, 'btn_tactic').change_tooltip(self.ui_text[lang].menu.t2)
        self.ui.left_menu.findChild(QPushButton, 'btn_development').change_tooltip(self.ui_text[lang].menu.t3)
        self.ui.left_menu.findChild(QPushButton, 'btn_stats').change_tooltip(self.ui_text[lang].menu.t5)
        self.ui.left_menu.findChild(QPushButton, 'btn_metrics').change_tooltip(self.ui_text[lang].menu.t6)
        self.ui.left_menu.findChild(QPushButton, 'btn_compare').change_tooltip(self.ui_text[lang].menu.t7)
        self.ui.left_menu.findChild(QPushButton, 'btn_scouting').change_tooltip(self.ui_text[lang].menu.t8)
        self.ui.left_menu.findChild(QPushButton, 'btn_employees').change_tooltip(self.ui_text[lang].menu.t9)
        self.ui.left_menu.findChild(QPushButton, 'btn_settings').change_tooltip(self.ui_text[lang].menu.t10)
        self.ui.left_menu.findChild(QPushButton, 'btn_info').change_tooltip(self.ui_text[lang].menu.t11)
        self.ui.left_menu.findChild(QPushButton, 'btn_help').change_tooltip(self.ui_text[lang].menu.t12)
        self.ui.left_menu.toggle_button.change_tooltip(self.ui_text[lang].menu.t4)

        # Translating tooltip title buttons
        self.ui.title_bar.findChild(QPushButton,
                                    'btn_refresh').change_tooltip(self.ui_text[lang].title_buttons_tooltips.b1)
        self.ui.title_bar.findChild(QPushButton,
                                    'btn_top_settings').change_tooltip(self.ui_text[lang].title_buttons_tooltips.b2)
        self.ui.title_bar.minimize_button.change_tooltip(self.ui_text[lang].title_buttons_tooltips.b3)
        self.ui.title_bar.maximize_restore_button.change_tooltip(self.ui_text[lang].title_buttons_tooltips.b4)
        self.ui.title_bar.close_button.change_tooltip(self.ui_text[lang].title_buttons_tooltips.b5)


        # Translating left inside menu
        self.ui.load_squad_btn.setText(self.ui_text[lang].left_content.b1)
        self.ui.load_scouting_btn.setText(self.ui_text[lang].left_content.b2)

        # Translatin right inside menu
        self.ui.right_btn_1.setText(self.ui_text[lang].right_content.b1)
        self.ui.right_btn_2.setText(self.ui_text[lang].right_content.b2)



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
