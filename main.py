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

# IMPORT UTILS
# ///////////////////////////////////////////
from gui.core.util import get_screen_size

# IMPORT FM INSIDE
# ///////////////////////////////////////////
import gui.core.fm_insider.FMinside as FMi

# IMPORT CUSTOM CLASSES
# ///////////////////////////////////////////
from gui.core.models.CustomNestedNamespace.py_CustomNestedNamespace import NestedNamespace
from gui.core.models.CustomNumpyTableModel.py_CustomNumpyTableModel import CustomizedNumpyModel
from gui.core.models.CustomNumpyListModel.py_CustomNumpyListModel import CustomizedNumpyListModel

# IMPORT TRANSLATIONS
# ///////////////////////////////////////////
from gui.core.dicts import en, es, util_lists

# IMPORT WIDGETS
# ///////////////////////////////////////////
from gui.widgets import *

# IMPORT KHAMISIKIBET WIDGET
# ///////////////////////////////////////////
from Custom_Widgets.Widgets import loadJsonStyle


# IMPORT INTERFACE
# ///////////////////////////////////////////
from gui.uis.windows.main_window.ui_interface_personal import Ui_MainWindow

# ADJUST QT FONT DPI FOR HIGH SCALE
# ///////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"

# MAIN WINDOW
# ///////////////////////////////////////////


class MainWindow(QMainWindow):
    closing = Signal()

    def __init__(self):
        super(MainWindow, self).__init__()

        # SETUP MAIN WINDOW
        # Load widgets from "gui\uis\main_window\ui_interface_personal.py"
        # ///////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # CLASS VARIABLES
        # ///////////////////////////////////////////
        self.dragPos = None
        self.df_original = None
        self.df_squad = None
        self.df_tactic = None
        self.df_for_table = None
        self.bottom_right_grip = None
        self.bottom_left_grip = None
        self.top_right_grip = None
        self.top_left_grip = None
        self.bottom_grip = None
        self.top_grip = None
        self.right_grip = None
        self.left_grip = None
        self.haveSquadInfo = False
        self.haveScoutingInfo = False
        self.haveOldSquadInfo = False
        self.ui_text = {}
        self.ui_text.update({'en': NestedNamespace(en.english)})
        self.ui_text.update({'es': NestedNamespace(es.espanol)})
        self.ui_headers = {}
        self.ui_headers.update({'en': NestedNamespace(en.column_headers)})
        self.ui_headers.update({'es': NestedNamespace(es.column_headers)})

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
        loadJsonStyle(self, self.ui)

        # CUSTOM MAIN ANIMATIONS
        # ///////////////////////////////////////////
        self.windowObject = self
        self.windowObject.move(20, 20)

        # CREATING VAR FOR SHOWING ANIMATION
        # ///////////////////////////////////////////
        self.showAnimation = QPropertyAnimation(self, b"pos")
        self.showAnimation.setDuration(700)

        # CREATING VAR FOR HIDING ANIMATION
        # ///////////////////////////////////////////
        self.hideAnimation = QPropertyAnimation(self, b"pos")
        self.hideAnimation.setDuration(400)

        # SAVING OLD POSITION
        self.oldPos = self.get_center()
        self._is_started = False

    # ///////////////////////////////////////////
    # START IMPLEMENTED FUNCTIONS
    # ///////////////////////////////////////////

    # RE-IMPLEMENT SHOW EVENT
    # ///////////////////////////////////////////
    def showEvent(self, event: QShowEvent) -> None:
        self.showAnimation.setStartValue(
            QPoint(self.x(), get_screen_size().height())
        )
        self.showAnimation.setEndValue(self.oldPos)
        self.showAnimation.setEasingCurve(QEasingCurve.OutCubic)
        self.showAnimation.start()

        QMainWindow.showEvent(self, event)

    # RE-IMPLEMENT CLOSE EVENT
    # ///////////////////////////////////////////
    def closeEvent(self, event: QCloseEvent) -> None:
        if not self._is_started:
            self.oldPos = self.pos()
            self.hideAnimation.setStartValue(self.oldPos)
            self.hideAnimation.setEndValue(
                QPoint(
                    self.x(), get_screen_size().height()
                )
            )
            self.hideAnimation.setEasingCurve(QEasingCurve.InCubic)
            self.hideAnimation.start()
            self._is_started = True
            event.ignore()
        else:
            event.accept()

        self.hideAnimation.finished.connect(self.close)

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

    # ///////////////////////////////////////////
    # END IMPLEMENTED FUNCTIONS
    # ///////////////////////////////////////////

    # ///////////////////////////////////////////
    # START CUSTOM FUNCTIONS FOR UI
    # ///////////////////////////////////////////

    # CENTRE WINDOW
    # ///////////////////////////////////////////
    def center_window(self):
        frame_geo = self.frameGeometry()
        screen = self.window().windowHandle().screen()
        center_loc = screen.geometry().center()
        frame_geo.moveCenter(center_loc)
        self.move(frame_geo.topLeft())

    # GET CENTER OF THE SCREEN
    # ///////////////////////////////////////////
    def get_center(self):
        geometry = self.frameGeometry()
        geometry.moveCenter(get_screen_size().center())
        return geometry.topLeft()

    # CREATE MINIMIZE EVENT
    # ///////////////////////////////////////////
    def minimize_event(self):
        self.oldPos = self.pos()
        self.hideAnimation.setStartValue(self.oldPos)
        self.hideAnimation.setEndValue(
            QPoint(
                self.x(), get_screen_size().height()
            )
        )
        self.hideAnimation.setEasingCurve(QEasingCurve.InCubic)
        self.hideAnimation.setDuration(400)
        self.hideAnimation.start()
        self.hideAnimation.finished.connect(lambda: self.showMinimized())

    # CREATE MAXIMIZE EVENT
    # ///////////////////////////////////////////
    def maximize_event(self):
        self.oldPos = self.pos()
        self.hideAnimation.setStartValue(self.oldPos)
        # self.hideAnimation.setEndValue(
        #     QPoint(
        #         self.x(), get_screen_size().height()
        #     )
        # )
        self.hideAnimation.setEndValue(
            QRect(
                self.x(),
                self.y(),
                get_screen_size().width(),
                get_screen_size().height()
            )
        )
        self.hideAnimation.setDuration(200)
        self.hideAnimation.setEasingCurve(QEasingCurve.InCubic)
        self.hideAnimation.start()
        self.center_window()
        self.hideAnimation.finished.connect(lambda: self.ui.title_bar.maximize_restore())

    # RESIZE NOTIFICATION POPUP
    # ///////////////////////////////////////////
    def adjust_notification_container(self, btn):
        # RESET CONTAINER HEIGHT
        self.ui.popup_notification_container.expandedHeight = self.default_size_notification_container
        if btn.get_len_lista() > 5:
            diff = btn.get_len_lista() - 5
            # SET + HEIGHT IF HAVE A LOT OF PLAYERS
            self.ui.popup_notification_container.expandedHeight = self.default_size_notification_container + (12 * diff)
        # FORMAT TEXT TO BE DISPLAYED
        tmp = btn.text_formater()
        # DISPLAY PLAYERS
        self.ui.list_label.setText(tmp)
        # EXEC NOTIFICATION CONTAINER
        self.ui.popup_notification_container.toggleMenu(btn)

    # ///////////////////////////////////////////
    # END CUSTOM FUNCTIONS FOR UI
    # ///////////////////////////////////////////

    # ///////////////////////////////////////////
    # START CUSTOM FUNCTIONS FOR SETTINGS
    # ///////////////////////////////////////////

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

    # ///////////////////////////////////////////
    # END CUSTOM FUNCTIONS FOR SETTINGS
    # ///////////////////////////////////////////

    # ///////////////////////////////////////////
    # START PRINCIPAL FUNCTIONS FOR CLICKS AND SIGNALS
    # ///////////////////////////////////////////

    # BUTTONS WITH SIGNALS CLICKED
    # ///////////////////////////////////////////
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
            self.ui.set_page(self.ui.load_pages.page_5)

        # Metrics Btn
        if btn.objectName() == "btn_metrics":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page 6
            self.ui.set_page(self.ui.load_pages.page_6)

        # Compare Btn
        if btn.objectName() == "btn_compare":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page 7
            self.ui.set_page(self.ui.load_pages.page_7)

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
            '''
            No implementado por que es buton auxiliar
            '''
            pass

        # VERTICAL PITCH
        # ///////////////////////////////////////////
        # Button 1
        # SET DEFAULT SIZE
        self.default_size_notification_container = self.ui.popup_notification_container.getDefaultHeight()
        if btn.objectName() == "btn_pos_1":
            self.adjust_notification_container(btn)

        # Button 2
        if btn.objectName() == "btn_pos_2":
            self.adjust_notification_container(btn)

        # Button 3
        if btn.objectName() == "btn_pos_3":
            self.adjust_notification_container(btn)

        # Button 4
        if btn.objectName() == "btn_pos_4":
            self.adjust_notification_container(btn)

        # Button 5
        if btn.objectName() == "btn_pos_5":
            self.adjust_notification_container(btn)

        # Button 6
        if btn.objectName() == "btn_pos_6":
            self.adjust_notification_container(btn)

        # Button 7
        if btn.objectName() == "btn_pos_7":
            self.adjust_notification_container(btn)

        # Button 8
        if btn.objectName() == "btn_pos_8":
            self.adjust_notification_container(btn)

        # Button 9
        if btn.objectName() == "btn_pos_9":
            self.adjust_notification_container(btn)

        # Button 10
        if btn.objectName() == "btn_pos_10":
            self.adjust_notification_container(btn)

        # Button 11
        if btn.objectName() == "btn_pos_11":
            self.adjust_notification_container(btn)

        # DEBUG
        # print(f"Button {btn.objectName()}, clicked!")

    # BUTTONS WITH SIGNALS RELEASED
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

        # VERTICAL PITCH SIGNALS
        self.ui.pitch_widget.clicked.connect(self.btn_clicked)
        self.ui.pitch_widget.released.connect(self.btn_released)

    # ///////////////////////////////////////////
    # END PRINCIPAL FUNCTIONS FOR CLICKS AND SIGNALS
    # ///////////////////////////////////////////

    # ///////////////////////////////////////////
    # START CUSTOM FUNCTIONS FOR EVENTS
    # ///////////////////////////////////////////

    # CONNECT EVENTS
    # ///////////////////////////////////////////
    def connect_events(self):
        # CLICK EVENTS
        # ///////////////////////////////////////////
        self.ui.load_squad_btn.clicked.connect(lambda: self.load_all_data(self.ui.load_squad_btn))
        self.ui.load_scouting_btn.clicked.connect(lambda: self.load_all_data(self.ui.load_scouting_btn))
        # ADD OLD SQUAD BUTTON
        self.ui.english_language_btn.clicked.connect(lambda: self.translate_lang('en'))
        self.ui.spanish_language_btn.clicked.connect(lambda: self.translate_lang('es'))
        self.ui.btn_close_notification.clicked.connect(lambda: self.ui.popup_notification_container.collapseMenu())
        self.ui.btn_send.clicked.connect(lambda: self.process_data_compare_players())

        # SLIDE BETWEEN PAGES
        # ///////////////////////////////////////////
        # Change to pages in right column
        self.ui.right_btn_1.clicked.connect(
            lambda: self.ui.set_right_column_menu(
                self.ui.right_column.menu_2
            )
        )

        self.ui.right_btn_2.clicked.connect(
            lambda: self.ui.set_right_column_menu(
                self.ui.right_column.menu_1
            )
        )

        # Change to checkbox list of stats in compare page
        self.ui.btn_compare_stats.clicked.connect(
            lambda: self.ui.set_compare_column_menu(
                self.ui.load_pages.menu2_compare,
                self.ui.btn_compare_stats
            )
        )
        # Change to checkbox list of metrics in compare page
        self.ui.btn_compare_attrs.clicked.connect(
            lambda: self.ui.set_compare_column_menu(
                self.ui.load_pages.menu1_compare,
                self.ui.btn_compare_attrs
            )
        )
        # CHANGE EVENTS
        # ///////////////////////////////////////////

    # ///////////////////////////////////////////
    # END CUSTOM FUNCTIONS FOR EVENTS
    # ///////////////////////////////////////////

    # ///////////////////////////////////////////
    # START CUSTOM FUNCTIONS FOR FUNCTIONALITY
    # ///////////////////////////////////////////

    # LOAD FILE
    # ///////////////////////////////////////////
    def load_all_data(self, button_object):
        # FILE DIALOG
        dlg_file = QFileDialog.getOpenFileName(
            self,
            caption="Select a file",
            filter="HTML Files (*.html)"
        )

        # READ FILE
        if dlg_file:
            if 'squad' in button_object.text():
                # SETTING ORIGINAL DATAFRAME
                self.df_original = FMi.setting_up_pandas(dlg_file[0], 'squad_btn')
                self.process_squad_info()

                self.tables_helper()

                self.load_data_for_graphs()

                self.create_and_load_checkboxes()
                tmp_list = self.df_original[self.ui_headers[self.language].h.h1].values.tolist()
                self.add_squad_names(tmp_list)
                self.haveSquadInfo = True
            elif 'scouting' in button_object.text():
                '''
                No implementado aun
                '''
                pass
            elif 'old' in button_object.text():
                '''
                No implementado aun por que no se que hacer aqui
                '''
                pass

    # PROCESS ACTUAL SQUAD INFO
    # ///////////////////////////////////////////
    def process_squad_info(self):
        self.df_original = FMi.convert_values(self.df_original, self.language)
        self.df_original = FMi.create_metrics_for_gk(self.df_original, self.language)

        # SETTING MODIFIED DATAFRAME
        self.df_squad = FMi.data_for_rankings(self.df_original, self.language)
        self.df_squad = FMi.create_scores_for_position(self.df_squad, self.language)
        self.df_squad = FMi.round_data(self.df_squad)
        self.df_squad = FMi.ranking_values(self.df_squad)

        # SETTING DATAFRAME FOR SQUAD TABLE
        self.df_for_table = FMi.create_df_for_squad(self.df_squad, self.language)
        # SETTING DATAFRAME FOR SQUAD TABLE
        self.df_tactic = self.df_for_table.iloc[:, :1]
        self.df_tactic = self.df_tactic.join(self.df_for_table.iloc[:, 2:3])

    # SQUAD HELPER FUNCTION
    # ///////////////////////////////////////////
    def tables_helper(self):
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

    # SET / LOAD DATA FOR STATS AND METRICS GRAPHS
    # ///////////////////////////////////////////
    def load_data_for_graphs(self):
        # SETTING DATAFRAME FOR STATS / METRICS WIDGET
        self.df_helper = self.df_original.iloc[:, :2]
        if self.language == 'en':
            self.df_helper = self.df_helper.join(self.df_original['Salary'])
            self.df_helper['Salary'] = self.df_helper['Salary'].fillna(0)
        elif self.language == 'es':
            self.df_helper = self.df_helper.join(self.df_original['Sueldo'])
            self.df_helper['Sueldo'] = self.df_helper['Sueldo'].fillna(0)
        self.df_helper = self.df_helper.join(self.df_original.iloc[:, 11:44])

        # STATS & METRICS DATA
        if self.ui.graph_statistics.chart.count_actual_list() > 1:
            self.ui.graph_statistics.type_selector.clear()
            self.ui.graph_statistics.combo_selector.clear()

        if self.language == 'en':
            self.ui.graph_statistics.type_selector.addItem(self.ui_text[self.language].menu.o5, util_lists.list_en[0])
            self.ui.graph_statistics.type_selector.addItem(self.ui_text[self.language].menu.o6, util_lists.list_en[1])
            self.ui.graph_statistics.chart.add_to_list(util_lists.list_en[0])
            self.ui.graph_statistics.chart.add_to_list(util_lists.list_en[1])
        elif self.language == 'es':
            self.ui.graph_statistics.type_selector.addItem(self.ui_text[self.language].menu.o5, util_lists.list_es[0])
            self.ui.graph_statistics.type_selector.addItem(self.ui_text[self.language].menu.o6, util_lists.list_es[1])
            self.ui.graph_statistics.chart.add_to_list(util_lists.list_es[0])
            self.ui.graph_statistics.chart.add_to_list(util_lists.list_es[1])
        self.ui.graph_statistics.chart.set_data(self.df_helper)

    # TRANSLATE UI
    # ///////////////////////////////////////////
    def translate_lang(self, lang):
        self.language = lang

        # Translating side menu buttons
        self.ui.left_menu.findChild(QPushButton, 'btn_home').setText(self.ui_text[lang].menu.o0)
        self.ui.left_menu.findChild(QPushButton, 'btn_squad').setText(self.ui_text[lang].menu.o1)
        self.ui.left_menu.findChild(QPushButton, 'btn_tactic').setText(self.ui_text[lang].menu.o2)
        self.ui.left_menu.findChild(QPushButton, 'btn_development').setText(self.ui_text[lang].menu.o3)
        self.ui.left_menu.findChild(QPushButton, 'btn_stats').setText(self.ui_text[lang].menu.oaux1)
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
        self.ui.left_menu.findChild(QPushButton, 'btn_stats').change_tooltip(self.ui_text[lang].menu.taux1)
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

        # Translating right inside menu
        self.ui.right_btn_1.setText(self.ui_text[lang].right_content.b1)
        self.ui.right_btn_2.setText(self.ui_text[lang].right_content.b2)

    # CREATE AND LOAD CHECHBOXES TO COMPARE
    # ///////////////////////////////////////////
    def create_and_load_checkboxes(self):
        if self.ui.group_chk_stats_widget.get_count() is not None\
                and self.ui.group_chk_attrs_widget.get_count() is not None:
            self.ui.group_chk_attrs_widget.remove_all_buttons()
            self.ui.group_chk_stats_widget.remove_all_buttons()
        if self.language == 'en':
            self.ui.group_chk_attrs_widget.add_buttons(util_lists.list_en[2])
            self.ui.group_chk_stats_widget.add_buttons(util_lists.list_en[0])
        elif self.language == 'es':
            self.ui.group_chk_attrs_widget.add_buttons(util_lists.list_es[2])
            self.ui.group_chk_stats_widget.add_buttons(util_lists.list_es[0])

        # TEST SECTION
        self.ui.first_squad_player_combo.currentIndexChanged.connect(
            self.update_inner_combo
        )
        self.update_inner_combo(self.ui.first_squad_player_combo.currentIndex())

        self.ui.second_squad_player_combo.currentIndexChanged.connect(
            self.second_update_inner_combo
        )
        self.second_update_inner_combo(self.ui.second_squad_player_combo.currentIndex())

    def update_inner_combo(self, index):
        first_dependent_list = self.ui.first_squad_player_combo.itemData(index)
        if first_dependent_list:
            self.ui.first_player_combo.addItems(first_dependent_list)

    def second_update_inner_combo(self, index):
        second_dependent_list = self.ui.second_squad_player_combo.itemData(index)
        if second_dependent_list:
            self.ui.second_player_combo.addItems(second_dependent_list)

    # THREE FUNCTIONS FOR ACTUAL SQUAD, SCOUT, OLD SQUAD
    # //////////////////////////////////////////////////
    def add_squad_names(self, tmp_l):

        if self.ui.first_squad_player_combo.count() == 3:
            self.ui.first_squad_player_combo.clear()
            self.ui.first_player_combo.clear()
            self.ui.second_squad_player_combo.clear()
            self.ui.second_player_combo.clear()
        self.ui.first_squad_player_combo.addItem(self.ui_text[self.language].menu.g0, tmp_l)
        self.ui.second_squad_player_combo.addItem(self.ui_text[self.language].menu.g0, tmp_l)
        self.ui.spyder_graph_widget.spyder_chart.set_data(self.df_squad)

    def add_scouting_names(self):
        # TODO traer la lista
        if self.ui.first_squad_player_combo.count() == 3:
            self.ui.first_squad_player_combo.clear()
            self.ui.first_player_combo.clear()
            self.ui.second_squad_player_combo.clear()
            self.ui.second_player_combo.clear()
        self.ui.first_squad_player_combo.addItem(self.ui_text[self.language].menu.g1, [])
        self.ui.second_squad_player_combo.addItem(self.ui_text[self.language].menu.g1, [])

    def add_old_squad_names(self):
        # TODO traer la lista
        if self.ui.first_squad_player_combo.count() == 3:
            self.ui.first_squad_player_combo.clear()
            self.ui.first_player_combo.clear()
            self.ui.second_squad_player_combo.clear()
            self.ui.second_player_combo.clear()
        self.ui.first_squad_player_combo.addItem(self.ui_text[self.language].menu.g2, [])
        self.ui.second_squad_player_combo.addItem(self.ui_text[self.language].menu.g2, [])

    # SEND DATA FOR COMPARE GRAPHIC
    # ///////////////////////////////////////////////////
    def send_data_compare_graphic(self):
        checked_buttons = []
        actual_players = []
        if not self.ui.btn_compare_attrs.isEnabled():
            for i in range(self.ui.group_chk_attrs_widget.get_count()):
                if self.ui.group_chk_attrs_widget.button_group.button(i).isChecked():
                    checked_buttons.append(self.ui.group_chk_attrs_widget.button_group.button(i).get_name())
        elif not self.ui.btn_compare_stats.isEnabled():
            for i in range(self.ui.group_chk_stats_widget.get_count()):
                if self.ui.group_chk_stats_widget.button_group.button(i).isChecked():
                    checked_buttons.append(self.ui.group_chk_stats_widget.button_group.button(i).get_name())
        actual_players.append(
                self.ui.first_player_combo.currentText()
        )
        actual_players.append(
                self.ui.second_player_combo.currentText()
        )
        return actual_players, checked_buttons

    def process_data_compare_players(self):
        players_info, options_info = self.send_data_compare_graphic()
        self.ui.spyder_graph_widget.spyder_chart.set_chart(players_info, options_info)

    # ///////////////////////////////////////////
    # END CUSTOM FUNCTIONS FOR FUNCTIONALITY
    # ///////////////////////////////////////////


# MAIN FUNCTION TO START
# Set initial class and also additional parameter of the "QApplication" class
# ///////////////////////////////////////////
def main():
    # APPLICATION
    # ///////////////////////////////////////////
    app = QApplication(sys.argv)
    # app.setWindowIcon()
    window = MainWindow()
    window.show()

    # EXEC EXIT APP
    # ///////////////////////////////////////////
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
