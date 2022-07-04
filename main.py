# ///////////////////////////////////////////////////////////////
#
# BY: VICTOR CAICEDO
# PROJECT MADE WITH: PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import os

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# IMPORT KHAMISIKIBET WIDGET
# ///////////////////////////////////////////
from Custom_Widgets.Widgets import loadJsonStyle

# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////
# from gui.core.pyside_modules import *
from PySide6.QtCore import QEasingCurve, QPoint, QPropertyAnimation, QRect, Qt, Signal
from PySide6.QtGui import QCloseEvent, QShowEvent
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFileDialog,
    QHeaderView,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QTableView,
    QLabel,
    QSpacerItem,
    QSizePolicy
)

# PROCESSING, CHARTS AND CLUSTERING MODULES
# ///////////////////////////////////////////
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# IMPORT FM INSIDE
# ///////////////////////////////////////////
import gui.core.fm_insider.FMinside as FMi

# IMPORT TRANSLATIONS
# ///////////////////////////////////////////
from gui.core.dicts import en, es, util_lists

# IMPORT FUNCTIONS
# ///////////////////////////////////////////
# from gui.core.functions import Functions
from gui.core.functions import set_svg_icon

# IMPORT SETTINGS
# ///////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT CUSTOM CLASSES
# ///////////////////////////////////////////
from gui.core.models.CustomNestedNamespace.py_CustomNestedNamespace import (
    NestedNamespace,
)
from gui.core.models.CustomNumpyListModel.py_CustomNumpyListModel import (
    CustomizedNumpyListModel,
)
from gui.core.models.CustomNumpyScoutTableModel.py_CustomNumpyScoutTableModel import (
    CustomizedNumpyScoutModel,
)
from gui.core.models.CustomNumpyTableModel.py_CustomNumpyTableModel import (
    CustomizedNumpyModel,
)

# IMPORT UTILS
# ///////////////////////////////////////////
from gui.core.util import get_screen_size

# IMPORT INTERFACE
# ///////////////////////////////////////////
from gui.uis.windows.main_window.ui_interface import Ui_MainWindow

# IMPORT CUSTOM WIDGETS
# ///////////////////////////////////////////
from gui.widgets import PyGrips, FrameLayout

plt.style.use("seaborn-whitegrid")

# ADJUST QT FONT DPI FOR HIGH SCALE
# ///////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"

# MAIN WINDOW
# ///////////////////////////////////////////


# The class MainWindow inherits from the class QMainWindow
class MainWindow(QMainWindow):
    closing = Signal()

    def __init__(self):
        """
        The function is called when the program starts. It sets up the main window, loads settings,
        sets up the GUI, sets signals, connects events, loads the style, creates animations, and saves the old position
        """
        super(MainWindow, self).__init__()

        # SETUP MAIN WINDOW
        # Load widgets from "gui\uis\main_window\ui_interface.py"
        # ///////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # CLASS VARIABLES
        # ///////////////////////////////////////////
        self.dragPos = None
        # Main dataframes
        self.df_original = None
        self.df_squad = None
        self.df_tactic = None
        self.df_for_table = None
        self.df_scouting = None
        self.df_scout_for_table = None
        self.filtered_df = None
        self.df_old_squad = None
        self.df_helper = None
        # Others vars needed in init
        self.first_collapsable = None
        self.text_first_collapsable = None
        self.second_collapsable = None
        self.second_collapsable_1 = None
        self.second_collapsable_2 = None
        self.second_collapsable_3 = None
        self.second_collapsable_4 = None
        self.text_sc1 = None
        self.text_sc2 = None
        self.text_sc3 = None
        self.text_sc4 = None
        self.third_collapsable = None
        self.text_third_collapsable = None
        self.fourth_collapsable = None
        self.text_fourth_collapsable = None
        self.fifth_collapsable = None
        self.text_fifth_collapsable = None
        self.sixth_collapsable = None
        self.text_sixth_collapsable = None
        self.seventh_collapsable = None
        self.text_seventh_collapsable = None
        self.eighth_collapsable = None
        self.text_eighth_collapsable = None
        self.ninth_collapsable = None
        self.text_ninth_collapsable = None
        self.vertical_collapsable = None

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
        self.scoutingCounter = 0
        self.haveOldSquadInfo = False
        self.ui_text = {}
        self.ui_text.update({"en": NestedNamespace(en.english)})
        self.ui_text.update({"es": NestedNamespace(es.espanol)})
        self.ui_headers = {}
        self.ui_headers.update({"en": NestedNamespace(en.column_headers)})
        self.ui_headers.update({"es": NestedNamespace(es.column_headers)})
        self.default_size_notification_container = None

        # LOAD SETTINGS
        # ///////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items
        self.language = "en"

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////
        self.hide_grips = True  # Show/Hide resize grips
        self.custom_settings()
        self.ui.setup_gui()
        self.set_signals()
        self.connect_events()
        self.load_qa_questions()
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
        """
        The function is called when the window is shown. It sets the start value of the animation to the current
        position of the window, and the end value to the position of the window before it was hidden

        :param event: QShowEvent
        :type event: QShowEvent
        """
        self.showAnimation.setStartValue(
            QPoint(self.x(),
                   get_screen_size().height()))
        self.showAnimation.setEndValue(self.oldPos)
        self.showAnimation.setEasingCurve(QEasingCurve.OutCubic)
        self.showAnimation.start()

        QMainWindow.showEvent(self, event)

    # RE-IMPLEMENT CLOSE EVENT
    # ///////////////////////////////////////////
    def closeEvent(self, event: QCloseEvent) -> None:
        """
        The function is called when the user clicks the close button on the window. If the window is not started,
        the window is hidden and the animation is started. If the window is started, the window is closed

        :param event: QCloseEvent
        :type event: QCloseEvent
        """
        if not self._is_started:
            self.oldPos = self.pos()
            self.hideAnimation.setStartValue(self.oldPos)
            self.hideAnimation.setEndValue(
                QPoint(self.x(),
                       get_screen_size().height()))
            self.hideAnimation.setEasingCurve(QEasingCurve.InCubic)
            self.hideAnimation.start()
            self._is_started = True
            event.ignore()
        else:
            event.accept()

        self.hideAnimation.finished.connect(self.close)

    # RESIZE EVENT
    # ///////////////////////////////////////////
    def resizeEvent(self, _event):
        """
        It resizes the grips and changes their position

        :param _event: The event that triggered the resize
        """
        # RESIZE GRIPS AND CHANGE POSITION
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10,
                                        self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5,
                                         self.height() - 15,
                                         self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20,
                                               self.height() - 20, 15, 15)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////
    def mousePressEvent(self, event):
        """
        The function sets the global position of the mouse to the variable dragPos

        :param event: The event that was triggered
        """
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
        """The function takes a window object and centers it on the screen"""
        frame_geo = self.frameGeometry()
        screen = self.window().windowHandle().screen()
        center_loc = screen.geometry().center()
        frame_geo.moveCenter(center_loc)
        self.move(frame_geo.topLeft())

    # GET CENTER OF THE SCREEN
    # ///////////////////////////////////////////
    def get_center(self):
        """
        It returns the top left corner of the window, which is the same as the center of the window, but only if the
        window is centered on the screen
        :return: The top left corner of the window.
        """
        geometry = self.frameGeometry()
        geometry.moveCenter(get_screen_size().center())
        return geometry.topLeft()

    # CREATE MINIMIZE EVENT
    # ///////////////////////////////////////////
    def minimize_event(self):
        """It moves the window to the bottom of the screen, then minimizes it"""
        self.oldPos = self.pos()
        self.hideAnimation.setStartValue(self.oldPos)
        self.hideAnimation.setEndValue(
            QPoint(self.x(),
                   get_screen_size().height()))
        self.hideAnimation.setEasingCurve(QEasingCurve.InCubic)
        self.hideAnimation.setDuration(400)
        self.hideAnimation.start()
        self.hideAnimation.finished.connect(self.showMinimized)

    # CREATE MAXIMIZE EVENT
    # ///////////////////////////////////////////
    def maximize_event(self):
        """
        It hides the window, moves it to the top left corner of the screen, resizes it to the size of the screen,
        and then centers it
        """
        self.oldPos = self.pos()
        self.hideAnimation.setStartValue(self.oldPos)
        self.hideAnimation.setEndValue(
            QRect(
                self.x(),
                self.y(),
                get_screen_size().width(),
                get_screen_size().height(),
            ))
        self.hideAnimation.setDuration(200)
        self.hideAnimation.setEasingCurve(QEasingCurve.InCubic)
        self.hideAnimation.start()
        self.center_window()
        self.hideAnimation.finished.connect(self.ui.title_bar.maximize_restore)

    # RESIZE NOTIFICATION POPUP
    # ///////////////////////////////////////////
    def adjust_notification_container(self, btn):
        """
        It takes a button as an argument, resets the height of the container, checks if the button has more than 5
        players, if it does, it adds 12 pixels to the height of the container for each player over 5, formats the text
        to be displayed, displays the text, and then toggles the menu

        :param btn: the button that was clicked
        """
        # RESET CONTAINER HEIGHT
        self.ui.popup_notification_container.expandedHeight = (
            self.default_size_notification_container)
        if btn.get_len_lista() > 5:
            diff = btn.get_len_lista() - 5
            # SET + HEIGHT IF HAVE A LOT OF PLAYERS
            self.ui.popup_notification_container.expandedHeight = (
                self.default_size_notification_container + (12 * diff))
        # FORMAT TEXT TO BE DISPLAYED
        tmp = btn.text_formatter()
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
        """It sets the title of the window, removes the title bar, and adds grips to the window"""
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
            self.bottom_left_grip = PyGrips(self, "bottom_left",
                                            self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right",
                                             self.hide_grips)

    # ///////////////////////////////////////////
    # END CUSTOM FUNCTIONS FOR SETTINGS
    # ///////////////////////////////////////////

    # ///////////////////////////////////////////
    # START PRINCIPAL FUNCTIONS FOR CLICKS AND SIGNALS
    # ///////////////////////////////////////////

    # BUTTONS WITH SIGNALS CLICKED
    # ///////////////////////////////////////////
    def btn_clicked(self):
        """It's a function that handles all the button clicks in the application"""
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

        # Stats Btn
        if btn.objectName() == "btn_stats":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page 5
            self.ui.set_page(self.ui.load_pages.page_5)

        # Compare Btn
        if btn.objectName() == "btn_compare":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page 7
            self.ui.set_page(self.ui.load_pages.page_7)

        # Scouting Btn
        if btn.objectName() == "btn_scouting":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page 8
            self.ui.set_page(self.ui.load_pages.page_8)

        # Help Btn
        if btn.objectName() == "btn_help":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page 9
            self.ui.set_page(self.ui.load_pages.page_9)

        # Clustering Btn
        if btn.objectName() == "btn_clustering":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page 10
            self.ui.set_page(self.ui.load_pages.page_10)

        # Languages Btn
        if btn.objectName() == "btn_languages":
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
                    title="Language tab",
                    icon_path=set_svg_icon("icon_info.svg"),
                )

        # Settings left
        if (btn.objectName() == "btn_settings"
                or btn.objectName() == "btn_close_left_column"):
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
                    icon_path=set_svg_icon("icon_settings.svg"),
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
            for line, combo in zip(
                    self.ui.right_column.scroll_area_1.findChildren(QLineEdit),
                    self.ui.right_column.scroll_area_1.findChildren(QComboBox),
            ):
                line.setText("0")
                combo.setCurrentIndex(0)
            for line, combo in zip(
                    self.ui.right_column.scroll_area_2.findChildren(QLineEdit),
                    self.ui.right_column.scroll_area_2.findChildren(QComboBox),
            ):
                line.setText("0")
                combo.setCurrentIndex(0)

        # VERTICAL PITCH
        # ///////////////////////////////////////////
        # Button 1
        # SET DEFAULT SIZE
        self.default_size_notification_container = (
            self.ui.popup_notification_container.getDefaultHeight())
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

    # BUTTONS WITH SIGNALS RELEASED
    # ///////////////////////////////////////////
    def btn_released(self):
        """The function is called when a button is released"""
        # GET BTN CLICKED
        # btn = self.ui.setup_btns()

    # SET ALL SIGNALS
    # ///////////////////////////////////////////
    def set_signals(self):
        """It connects the clicked and released signals of the buttons to the btn_clicked and btn_released functions"""
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
        """The function connects the buttons to the functions that will be executed when the buttons are clicked"""
        # CLICK EVENTS
        # ///////////////////////////////////////////
        self.ui.load_squad_btn.clicked.connect(
            lambda: self.load_all_data(self.ui.load_squad_btn))
        self.ui.load_scouting_btn.clicked.connect(
            lambda: self.load_all_data(self.ui.load_scouting_btn))
        self.ui.load_old_btn.clicked.connect(
            lambda: self.load_all_data(self.ui.load_old_btn))
        self.ui.english_language_btn.clicked.connect(
            lambda: self.translate_lang("en"))
        self.ui.spanish_language_btn.clicked.connect(
            lambda: self.translate_lang("es"))
        self.ui.right_btn_3.clicked.connect(self.collect_scout_data)
        self.ui.btn_close_notification.clicked.connect(
            self.ui.popup_notification_container.collapseMenu)
        self.ui.btn_send.clicked.connect(self.process_data_compare_players)
        self.ui.clustering_btn_send.clicked.connect(self.clustering_management)

        # SLIDE BETWEEN PAGES
        # ///////////////////////////////////////////
        # Change to pages in right column
        self.ui.right_btn_1.clicked.connect(
            lambda: self.ui.set_right_column_menu(self.ui.right_column.menu_2))

        self.ui.right_btn_2.clicked.connect(
            lambda: self.ui.set_right_column_menu(self.ui.right_column.menu_1))

        # Change to checkbox list of stats in compare page
        self.ui.btn_compare_stats.clicked.connect(
            lambda: self.ui.set_compare_column_menu(
                self.ui.load_pages.menu2_compare, self.ui.btn_compare_stats))
        # Change to checkbox list of metrics in compare page
        self.ui.btn_compare_attrs.clicked.connect(
            lambda: self.ui.set_compare_column_menu(
                self.ui.load_pages.menu1_compare, self.ui.btn_compare_attrs))
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
    def load_qa_questions(self):

        new_font = "color: #dce1ec; text-align: justify; text-justify: inter-word; font-size: 16px; font-weight: bold;"
        # Start First collapsable tab
        self.first_collapsable = FrameLayout(
            title=self.ui_text[self.language].pages.p9.first_collapse[0]
        )
        self.text_first_collapsable = QLabel(
            self.ui_text[self.language].pages.p9.first_collapse[1]
        )
        self.text_first_collapsable.setStyleSheet(new_font)
        self.text_first_collapsable.setWordWrap(True)
        self.first_collapsable.addWidget(self.text_first_collapsable)

        # End First collapsable tab

        # Start Second collapsable tab
        self.second_collapsable = FrameLayout(
            title=self.ui_text[self.language].pages.p9.second_collapse[0]
        )
        self.second_collapsable_1 = FrameLayout(
            title=self.ui_text[self.language].pages.p9_aux.step_one[0]
        )
        self.text_sc1 = QLabel(
            self.ui_text[self.language].pages.p9_aux.step_one[1]
        )
        self.text_sc1.setStyleSheet(new_font)
        self.text_sc1.setWordWrap(True)
        self.second_collapsable_1.addWidget(self.text_sc1)

        self.second_collapsable.addWidget(self.second_collapsable_1)

        self.second_collapsable_2 = FrameLayout(
            title=self.ui_text[self.language].pages.p9_aux.step_two[0]
        )
        self.text_sc2 = QLabel(
            self.ui_text[self.language].pages.p9_aux.step_two[1]
        )
        self.text_sc2.setStyleSheet(new_font)
        self.text_sc2.setWordWrap(True)
        self.second_collapsable_2.addWidget(self.text_sc2)

        self.second_collapsable.addWidget(self.second_collapsable_2)

        self.second_collapsable_3 = FrameLayout(
            title=self.ui_text[self.language].pages.p9_aux.step_three[0]
        )
        self.text_sc3 = QLabel(
            self.ui_text[self.language].pages.p9_aux.step_three[1]
        )
        self.text_sc3.setStyleSheet(new_font)
        self.text_sc3.setWordWrap(True)
        self.second_collapsable_3.addWidget(self.text_sc3)

        self.second_collapsable.addWidget(self.second_collapsable_3)

        self.second_collapsable_4 = FrameLayout(
            title=self.ui_text[self.language].pages.p9_aux.step_four[0]
        )
        self.text_sc4 = QLabel(
            self.ui_text[self.language].pages.p9_aux.step_four[1]
        )
        self.text_sc4.setStyleSheet(new_font)
        self.text_sc4.setWordWrap(True)
        self.second_collapsable_4.addWidget(self.text_sc4)

        self.second_collapsable.addWidget(self.second_collapsable_4)

        # End Second collapsable tab

        # Start Third collapsable tab

        self.third_collapsable = FrameLayout(
            title=self.ui_text[self.language].pages.p9.third_collapse[0]
        )
        self.text_third_collapsable = QLabel(
            self.ui_text[self.language].pages.p9.third_collapse[1]
        )
        self.text_third_collapsable.setStyleSheet(new_font)
        self.text_third_collapsable.setWordWrap(True)
        self.third_collapsable.addWidget(self.text_third_collapsable)

        # End Third collapsable tab

        # Start Fourth collapsable tab

        self.fourth_collapsable = FrameLayout(
            title=self.ui_text[self.language].pages.p9.fourth_collapse[0]
        )
        self.text_fourth_collapsable = QLabel(
            self.ui_text[self.language].pages.p9.fourth_collapse[1]
        )
        self.text_fourth_collapsable.setStyleSheet(new_font)
        self.text_fourth_collapsable.setWordWrap(True)
        self.fourth_collapsable.addWidget(self.text_fourth_collapsable)

        # End Fourth collapsable tab

        # Start Fifth collapsable tab

        self.fifth_collapsable = FrameLayout(
            title=self.ui_text[self.language].pages.p9.fifth_collapse[0]
        )
        self.text_fifth_collapsable = QLabel(
            self.ui_text[self.language].pages.p9.fifth_collapse[1]
        )
        self.text_fifth_collapsable.setStyleSheet(new_font)
        self.text_fifth_collapsable.setWordWrap(True)
        self.fifth_collapsable.addWidget(self.text_fifth_collapsable)

        # End Fifth collapsable tab

        # Start Sixth collapsable tab

        self.sixth_collapsable = FrameLayout(
            title=self.ui_text[self.language].pages.p9.sixth_collapse[0]
        )
        self.text_sixth_collapsable = QLabel(
            self.ui_text[self.language].pages.p9.sixth_collapse[1]
        )
        self.text_sixth_collapsable.setStyleSheet(new_font)
        self.text_sixth_collapsable.setWordWrap(True)
        self.sixth_collapsable.addWidget(self.text_sixth_collapsable)

        # End Sixth collapsable tab

        # Start Seventh collapsable tab

        self.seventh_collapsable = FrameLayout(
            title=self.ui_text[self.language].pages.p9.seventh_collapse[0]
        )
        self.text_seventh_collapsable = QLabel(
            self.ui_text[self.language].pages.p9.seventh_collapse[1]
        )
        self.text_seventh_collapsable.setStyleSheet(new_font)
        self.text_seventh_collapsable.setWordWrap(True)
        self.seventh_collapsable.addWidget(self.text_seventh_collapsable)

        # End Seventh collapsable tab

        # Start Eighth collapsable tab

        self.eighth_collapsable = FrameLayout(
            title=self.ui_text[self.language].pages.p9.eighth_collapse[0]
        )
        self.text_eighth_collapsable = QLabel(
            self.ui_text[self.language].pages.p9.eighth_collapse[1]
        )
        self.text_eighth_collapsable.setStyleSheet(new_font)
        self.text_eighth_collapsable.setWordWrap(True)
        self.eighth_collapsable.addWidget(self.text_eighth_collapsable)

        # End Eighth collapsable tab

        # Start Ninth collapsable tab

        self.ninth_collapsable = FrameLayout(
            title=self.ui_text[self.language].pages.p9.ninth_collapse[0]
        )
        self.text_ninth_collapsable = QLabel(
            self.ui_text[self.language].pages.p9.ninth_collapse[1]
        )
        self.text_ninth_collapsable.setStyleSheet(new_font)
        self.text_ninth_collapsable.setWordWrap(True)
        self.ninth_collapsable.addWidget(self.text_ninth_collapsable)

        # End Ninth collapsable tab

        # Add to main page layout
        self.ui.load_pages.vertical_layout_9.addWidget(self.first_collapsable)
        self.ui.load_pages.vertical_layout_9.addWidget(self.second_collapsable)
        self.ui.load_pages.vertical_layout_9.addWidget(self.third_collapsable)
        self.ui.load_pages.vertical_layout_9.addWidget(self.fourth_collapsable)
        self.ui.load_pages.vertical_layout_9.addWidget(self.fifth_collapsable)
        self.ui.load_pages.vertical_layout_9.addWidget(self.sixth_collapsable)
        self.ui.load_pages.vertical_layout_9.addWidget(self.seventh_collapsable)
        self.ui.load_pages.vertical_layout_9.addWidget(self.eighth_collapsable)
        self.ui.load_pages.vertical_layout_9.addWidget(self.ninth_collapsable)
        self.vertical_collapsable = QSpacerItem(10, 50, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.ui.load_pages.vertical_layout_9.addItem(self.vertical_collapsable)

    def load_all_data(self, button_object):
        """
        It reads a file, processes the data, and then creates a table and a graph

        :param button_object: The button that was clicked
        """
        # FILE DIALOG
        dlg_file = QFileDialog.getOpenFileName(self,
                                               caption="Select a file",
                                               filter="HTML Files (*.html)")

        # READ FILE
        if dlg_file[0] != "":
            if "squad" in button_object.get_name():
                # SETTING ORIGINAL DATAFRAME
                self.df_original = FMi.setting_up_pandas(
                    dlg_file[0])
                if self.df_original is not None:
                    self.process_squad_info()

                    self.tables_helper_squad()

                    self.load_data_for_graphs()

                    self.create_and_load_checkboxes()
                    tmp_list = self.df_original[self.ui_headers[
                        self.language].h.h1].values.tolist()
                    self.ui.clustering_player_combo.addItems(tmp_list)
                    self.add_squad_names(tmp_list)
                    self.haveSquadInfo = True
            elif "scouting" in button_object.get_name():
                if self.df_scouting is None:
                    self.df_scouting = FMi.setting_up_pandas(
                        dlg_file[0])
                else:
                    self.df_scouting = pd.concat([
                        self.df_scouting,
                        FMi.setting_up_pandas(dlg_file[0]),
                    ])
                if self.df_scouting is not None:
                    self.process_scouting_info()
                    if self.df_scouting is not None:
                        self.tables_helper_scouting(self.df_scout_for_table)
                        tmp_list = self.df_scouting[self.ui_headers[
                            self.language].h.h1].values.tolist()
                        self.create_edits_for_scouting()
                        self.create_lines_for_clustering()
                        self.add_scouting_names(tmp_list)
            elif "old" in button_object.text():
                # SETTING ORIGINAL DATAFRAME
                self.df_old_squad = FMi.setting_up_pandas(
                    dlg_file[0])
                if self.df_old_squad is not None:
                    self.process_old_squad_info()
                    tmp_list = self.df_old_squad[self.ui_headers[
                        self.language].h.h1].values.tolist()
                    self.add_old_squad_names(tmp_list)
                    self.haveSquadInfo = True

    # PROCESS ACTUAL SQUAD INFO
    # ///////////////////////////////////////////
    def process_squad_info(self):
        """
        It takes a dataframe, converts the values to the language of the user, creates metrics for goalkeepers, creates
        a dataframe for the rankings, rounds the data, creates a dataframe for the squad table, and creates a dataframe
        for the tactic table
        """
        self.df_original = FMi.convert_values(self.df_original, self.language)
        self.df_original = FMi.create_metrics_for_gk(self.df_original,
                                                     self.language)

        # SETTING MODIFIED DATAFRAME
        self.df_squad = FMi.data_for_rankings(self.df_original, self.language)
        self.df_squad = FMi.round_data(self.df_squad)
        self.df_squad = FMi.ranking_values(self.df_squad)

        # SETTING DATAFRAME FOR SQUAD TABLE
        self.df_for_table = FMi.create_df_for_squad(self.df_squad,
                                                    self.language)
        # SETTING DATAFRAME FOR SQUAD TABLE
        self.df_tactic = self.df_for_table.iloc[:, :1]
        self.df_tactic = self.df_tactic.join(self.df_for_table.iloc[:, 2:3])

    # PROCESS SCOUTING SQUAD INFO
    # ///////////////////////////////////////////
    def process_scouting_info(self):
        """
        It takes a dataframe, converts the values to the language of the user, converts the values to the scouting
        values, creates metrics for goalkeepers, creates a dataframe for the scouting team, fills the NaN values with
        0, and increments the scouting counter
        """
        if self.scoutingCounter < 4:
            self.df_scouting = FMi.convert_values(self.df_scouting,
                                                  self.language)
            self.df_scouting = FMi.convert_values_scout(self.df_scouting)
            self.df_scouting = FMi.create_metrics_for_gk(
                self.df_scouting, self.language)

            # SETTING MODIFIED DATAFRAME
            self.df_scouting = FMi.data_for_rankings(self.df_scouting,
                                                     self.language)
            self.df_scouting = FMi.round_data(self.df_scouting)
            self.df_scouting = FMi.ranking_values(self.df_scouting)

            self.df_scout_for_table = FMi.create_df_for_scouting_team(
                self.df_scouting, self.language)
            self.df_scout_for_table.fillna(0, inplace=True)
            self.scoutingCounter += 1
        else:
            self.df_scouting = None
            self.scoutingCounter = 0

    # PROCESS OLD SQUAD INFO
    # ///////////////////////////////////////////
    def process_old_squad_info(self):
        self.df_old_squad = FMi.convert_values(self.df_old_squad, self.language)
        self.df_old_squad = FMi.convert_values_scout(self.df_old_squad)
        self.df_old_squad = FMi.create_metrics_for_gk(self.df_old_squad, self.language)

        # SETTING MODIFIED DATAFRAME
        self.df_old_squad = FMi.data_for_rankings(self.df_old_squad, self.language)
        self.df_old_squad = FMi.round_data(self.df_old_squad)
        self.df_old_squad = FMi.ranking_values(self.df_old_squad)
        self.df_old_squad.fillna(0, inplace=True)

        self.haveOldSquadInfo = True

    # SQUAD HELPER FUNCTION
    # ///////////////////////////////////////////
    def tables_helper_squad(self):
        """It takes a dataframe, converts it to a numpy array, and then uses a custom model to display it in a table"""
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

    # SCOUTING HELPER FUNCTION
    # ///////////////////////////////////////////
    def tables_helper_scouting(self, df_to_set=None):
        """
        It takes a dataframe, converts it to a numpy array, and then sets the tableview to display the dataframe

        :param df_to_set: The dataframe to be set as the model
        """
        tmp_model = CustomizedNumpyScoutModel(df_to_set)
        column_indexes = [1, 3, 4, 5, 6, 7, 8, 10, 12]
        self.ui.table_scouting.setSelectionBehavior(QTableView.SelectItems)
        self.ui.table_scouting.setModel(tmp_model)
        self.ui.table_scouting.show()
        headers = self.ui.table_scouting.horizontalHeader()
        for c in column_indexes:
            headers.setSectionResizeMode(c, QHeaderView.ResizeToContents)

    # SET / LOAD DATA FOR STATS AND METRICS GRAPHS
    # ///////////////////////////////////////////
    def load_data_for_graphs(self):
        """It loads data from pandas dataframe, and then it loads that dataframe into a Chart object."""
        # SETTING DATAFRAME FOR STATS / METRICS WIDGET
        self.df_helper = self.df_original.iloc[:, :2]
        if self.language == "en":
            self.df_helper = self.df_helper.join(self.df_original["Salary"])
            self.df_helper["Salary"] = self.df_helper["Salary"].fillna(0)
        elif self.language == "es":
            self.df_helper = self.df_helper.join(self.df_original["Sueldo"])
            self.df_helper["Sueldo"] = self.df_helper["Sueldo"].fillna(0)
        self.df_helper = self.df_helper.join(self.df_original.iloc[:, 11:44])

        # STATS & METRICS DATA
        if self.ui.graph_statistics.chart.count_actual_list() > 1:
            self.ui.graph_statistics.type_selector.clear()
            self.ui.graph_statistics.combo_selector.clear()

        if self.language == "en":
            self.ui.graph_statistics.type_selector.addItem(
                self.ui_text[self.language].menu.o5, util_lists.list_en[0])
            self.ui.graph_statistics.type_selector.addItem(
                self.ui_text[self.language].menu.o6, util_lists.list_en[1])
            self.ui.graph_statistics.chart.add_to_list(util_lists.list_en[0])
            self.ui.graph_statistics.chart.add_to_list(util_lists.list_en[1])
        elif self.language == "es":
            self.ui.graph_statistics.type_selector.addItem(
                self.ui_text[self.language].menu.o5, util_lists.list_es[0])
            self.ui.graph_statistics.type_selector.addItem(
                self.ui_text[self.language].menu.o6, util_lists.list_es[1])
            self.ui.graph_statistics.chart.add_to_list(util_lists.list_es[0])
            self.ui.graph_statistics.chart.add_to_list(util_lists.list_es[1])
        self.ui.graph_statistics.chart.set_data(self.df_helper)

    # TRANSLATE UI
    # ///////////////////////////////////////////
    def translate_lang(self, lang):
        """
        It translates the UI

        :param lang: the language to translate to
        """
        self.language = lang

        # Translating side menu buttons
        self.ui.left_menu.findChild(QPushButton, "btn_home").setText(
            self.ui_text[lang].menu.o0)
        self.ui.left_menu.findChild(QPushButton, "btn_squad").setText(
            self.ui_text[lang].menu.o1)
        self.ui.left_menu.findChild(QPushButton, "btn_tactic").setText(
            self.ui_text[lang].menu.o2)
        self.ui.left_menu.findChild(QPushButton, "btn_stats").setText(
            self.ui_text[lang].menu.oaux1)
        self.ui.left_menu.findChild(QPushButton, "btn_compare").setText(
            self.ui_text[lang].menu.o7)
        self.ui.left_menu.findChild(QPushButton, "btn_scouting").setText(
            self.ui_text[lang].menu.o8)
        self.ui.left_menu.findChild(QPushButton, "btn_settings").setText(
            self.ui_text[lang].menu.o10)
        self.ui.left_menu.findChild(QPushButton, "btn_languages").setText(
            self.ui_text[lang].menu.o11)
        self.ui.left_menu.findChild(QPushButton, "btn_help").setText(
            self.ui_text[lang].menu.o12)
        self.ui.left_menu.toggle_button.setText(self.ui_text[lang].menu.o4)

        # Translating side menu tooltips
        self.ui.left_menu.findChild(QPushButton, "btn_home").change_tooltip(
            self.ui_text[lang].menu.t0)
        self.ui.left_menu.findChild(QPushButton, "btn_squad").change_tooltip(
            self.ui_text[lang].menu.t1)
        self.ui.left_menu.findChild(QPushButton, "btn_tactic").change_tooltip(
            self.ui_text[lang].menu.t2)
        self.ui.left_menu.findChild(QPushButton, "btn_stats").change_tooltip(
            self.ui_text[lang].menu.taux1)
        self.ui.left_menu.findChild(QPushButton, "btn_compare").change_tooltip(
            self.ui_text[lang].menu.t7)
        self.ui.left_menu.findChild(QPushButton,
                                    "btn_scouting").change_tooltip(
                                        self.ui_text[lang].menu.t8)
        self.ui.left_menu.findChild(QPushButton,
                                    "btn_settings").change_tooltip(
                                        self.ui_text[lang].menu.t10)
        self.ui.left_menu.findChild(QPushButton,
                                    "btn_languages").change_tooltip(
                                        self.ui_text[lang].menu.t11)
        self.ui.left_menu.findChild(QPushButton, "btn_help").change_tooltip(
            self.ui_text[lang].menu.t12)
        self.ui.left_menu.toggle_button.change_tooltip(
            self.ui_text[lang].menu.t4)

        # Translating tooltip title buttons
        self.ui.title_bar.findChild(QPushButton, "btn_refresh").change_tooltip(
            self.ui_text[lang].title_buttons_tooltips.b1)
        self.ui.title_bar.findChild(
            QPushButton, "btn_top_settings").change_tooltip(
                self.ui_text[lang].title_buttons_tooltips.b2)
        self.ui.title_bar.minimize_button.change_tooltip(
            self.ui_text[lang].title_buttons_tooltips.b3)
        self.ui.title_bar.maximize_restore_button.change_tooltip(
            self.ui_text[lang].title_buttons_tooltips.b4)
        self.ui.title_bar.close_button.change_tooltip(
            self.ui_text[lang].title_buttons_tooltips.b5)

        # Translating left inside menu
        self.ui.load_squad_btn.setText(self.ui_text[lang].left_content.b1)
        self.ui.load_scouting_btn.setText(self.ui_text[lang].left_content.b2)
        self.ui.load_old_btn.setText(self.ui_text[lang].left_content.b3)

        # Translating right inside menu
        self.ui.right_btn_1.setText(self.ui_text[lang].right_content.b1)
        self.ui.right_btn_2.setText(self.ui_text[lang].right_content.b2)
        self.ui.right_btn_3.setText(self.ui_text[lang].right_content.b3)

        # Translate page 7
        self.ui.btn_compare_stats.setText(
            self.ui_text[lang].pages.p7.btn_compare_s)
        self.ui.btn_compare_attrs.setText(
            self.ui_text[lang].pages.p7.btn_compare_a)
        self.ui.btn_send.setText(self.ui_text[lang].pages.p7.btn_compare_d)

        # Translating page 10
        self.ui.clustering_btn_send.setText(
            self.ui_text[lang].pages.p10.process_btn)

        # Translate charts
        self.ui.graph_statistics.chart.change_language(lang)
        self.ui.spyder_graph_widget.spyder_chart.change_language(lang)
        self.ui.clustering_chart.inner_chart.change_language(lang)

        # Translate help tab
        self.first_collapsable.title_frame.change_title(self.ui_text[self.language].pages.p9.first_collapse[0])
        self.text_first_collapsable.setText(self.ui_text[self.language].pages.p9.first_collapse[1])

        self.second_collapsable.title_frame.change_title(self.ui_text[self.language].pages.p9.second_collapse[0])

        self.third_collapsable.title_frame.change_title(self.ui_text[self.language].pages.p9.third_collapse[0])
        self.text_third_collapsable.setText(self.ui_text[self.language].pages.p9.third_collapse[1])

        self.fourth_collapsable.title_frame.change_title(self.ui_text[self.language].pages.p9.fourth_collapse[0])
        self.text_fourth_collapsable.setText(self.ui_text[self.language].pages.p9.fourth_collapse[1])

        self.fifth_collapsable.title_frame.change_title(self.ui_text[self.language].pages.p9.fifth_collapse[0])
        self.text_fifth_collapsable.setText(self.ui_text[self.language].pages.p9.fifth_collapse[1])

        self.sixth_collapsable.title_frame.change_title(self.ui_text[self.language].pages.p9.sixth_collapse[0])
        self.text_sixth_collapsable.setText(self.ui_text[self.language].pages.p9.sixth_collapse[1])

        self.seventh_collapsable.title_frame.change_title(self.ui_text[self.language].pages.p9.seventh_collapse[0])
        self.text_seventh_collapsable.setText(self.ui_text[self.language].pages.p9.seventh_collapse[1])

        self.eighth_collapsable.title_frame.change_title(self.ui_text[self.language].pages.p9.eighth_collapse[0])
        self.text_eighth_collapsable.setText(self.ui_text[self.language].pages.p9.eighth_collapse[1])

        self.ninth_collapsable.title_frame.change_title(self.ui_text[self.language].pages.p9.ninth_collapse[0])
        self.text_ninth_collapsable.setText(self.ui_text[self.language].pages.p9.ninth_collapse[1])

    # CREATE AND LOAD CHECHBOXES TO COMPARE
    # ///////////////////////////////////////////
    def create_and_load_checkboxes(self):
        """It creates and loads checkboxes to compare players"""
        if (self.ui.group_chk_stats_widget.get_count() is not None
                and self.ui.group_chk_attrs_widget.get_count() is not None):
            self.ui.group_chk_attrs_widget.remove_all_buttons()
            self.ui.group_chk_stats_widget.remove_all_buttons()
        if self.language == "en":
            self.ui.group_chk_attrs_widget.add_buttons(util_lists.list_en[2],
                                                       0)
            self.ui.group_chk_stats_widget.add_buttons(util_lists.list_en[0],
                                                       0)
        elif self.language == "es":
            self.ui.group_chk_attrs_widget.add_buttons(util_lists.list_es[2],
                                                       0)
            self.ui.group_chk_stats_widget.add_buttons(util_lists.list_es[0],
                                                       0)

        # TEST SECTION
        self.ui.first_squad_player_combo.currentIndexChanged.connect(
            self.update_inner_combo)
        self.update_inner_combo(
            self.ui.first_squad_player_combo.currentIndex())

        self.ui.second_squad_player_combo.currentIndexChanged.connect(
            self.second_update_inner_combo)
        self.second_update_inner_combo(
            self.ui.second_squad_player_combo.currentIndex())

    def update_inner_combo(self, index):
        """
        The function takes the index of the selected item in the first combo box and uses it to find the corresponding
        list of items in the second combo box

        :param index: The index of the item that was selected
        """
        first_dependent_list = self.ui.first_squad_player_combo.itemData(index)
        if first_dependent_list:
            self.ui.first_player_combo.clear()
            self.ui.first_player_combo.addItems(first_dependent_list)

    def second_update_inner_combo(self, index):
        """
        The function takes the index of the selected item in the second squad player combo box and uses that index to
        get the list of players associated with that squad. It then clears the second player combo box and adds the
        list of players to the second player combo box

        :param index: The index of the item that was selected
        """
        second_dependent_list = self.ui.second_squad_player_combo.itemData(
            index)
        if second_dependent_list:
            self.ui.second_player_combo.clear()
            self.ui.second_player_combo.addItems(second_dependent_list)

    def create_edits_for_scouting(self):
        """
        It creates a list of buttons for the user to click on, and then it creates a list of line edits for the user
        to type in
        """
        if (self.ui.group_lineedits_attrs_widget.get_lines() is not None and
                self.ui.group_lineedits_stats_widget.get_lines() is not None):
            self.ui.group_lineedits_attrs_widget.reset_all_lines()
            self.ui.group_lineedits_stats_widget.reset_all_lines()
        if self.language == "en":
            self.ui.group_lineedits_attrs_widget.add_buttons(
                util_lists.list_en[2], 1)
            self.ui.group_lineedits_stats_widget.add_buttons(
                util_lists.list_en[0], 1)
        elif self.language == "es":
            self.ui.group_lineedits_attrs_widget.add_buttons(
                util_lists.list_es[2], 1)
            self.ui.group_lineedits_stats_widget.add_buttons(
                util_lists.list_es[0], 1)

    def create_lines_for_clustering(self):
        """It creates a list of buttons for the user to select from"""
        if self.ui.group_clustering_filters.get_lines() is not None:
            self.ui.group_clustering_filters.reset_all_lines()
        if self.language == "en":
            self.ui.group_clustering_filters.add_buttons(
                util_lists.filters_en, 2)
        elif self.language == "es":
            self.ui.group_clustering_filters.add_buttons(
                util_lists.filters_es, 2)

    # THREE FUNCTIONS FOR ACTUAL SQUAD, SCOUT, OLD SQUAD
    # //////////////////////////////////////////////////
    def add_squad_names(self, tmp_l):
        """
        It takes a list of strings, and adds them to two combo boxes

        :param tmp_l: list of strings
        """
        if self.ui.first_squad_player_combo.count() == 3:
            self.ui.first_squad_player_combo.clear()
            self.ui.first_player_combo.clear()
            self.ui.second_squad_player_combo.clear()
            self.ui.second_player_combo.clear()
        self.ui.first_squad_player_combo.addItem(
            self.ui_text[self.language].menu.g0, tmp_l)
        self.ui.second_squad_player_combo.addItem(
            self.ui_text[self.language].menu.g0, tmp_l)
        self.ui.spyder_graph_widget.spyder_chart.set_data(self.df_squad)

    def add_scouting_names(self, tmp_l):
        """
        It takes a list of strings, and adds them to two combo boxes

        :param tmp_l: list of strings
        """
        if self.ui.first_squad_player_combo.count() == 3:
            self.ui.first_squad_player_combo.clear()
            self.ui.first_player_combo.clear()
            self.ui.second_squad_player_combo.clear()
            self.ui.second_player_combo.clear()
        self.ui.first_squad_player_combo.addItem(
            self.ui_text[self.language].menu.g1, tmp_l)
        self.ui.second_squad_player_combo.addItem(
            self.ui_text[self.language].menu.g1, tmp_l)
        self.ui.spyder_graph_widget.spyder_chart.set_data(self.df_scouting)

    def add_old_squad_names(self, tmp_l):
        if self.ui.first_squad_player_combo.count() == 3:
            self.ui.first_squad_player_combo.clear()
            self.ui.first_player_combo.clear()
            self.ui.second_squad_player_combo.clear()
            self.ui.second_player_combo.clear()
        self.ui.first_squad_player_combo.addItem(
            self.ui_text[self.language].menu.g2, tmp_l)
        self.ui.second_squad_player_combo.addItem(
            self.ui_text[self.language].menu.g2, tmp_l)

    # SEND DATA FOR COMPARE GRAPHIC
    # ///////////////////////////////////////////////////
    def send_data_compare_graphic(self):
        """
        It takes the data from the GUI and returns it to the main program to procces the comparative graph
        :return: the actual players, the squad, and the checked buttons.
        """
        checked_buttons = []
        actual_players = []
        squad = []
        if not self.ui.btn_compare_attrs.isEnabled():
            for i in range(self.ui.group_chk_attrs_widget.get_count()):
                if self.ui.group_chk_attrs_widget.button_group.button(
                        i).isChecked():
                    checked_buttons.append(
                        self.ui.group_chk_attrs_widget.button_group.button(
                            i).get_name())
        elif not self.ui.btn_compare_stats.isEnabled():
            for i in range(self.ui.group_chk_stats_widget.get_count()):
                if self.ui.group_chk_stats_widget.button_group.button(
                        i).isChecked():
                    checked_buttons.append(
                        self.ui.group_chk_stats_widget.button_group.button(
                            i).get_name())
        actual_players.append(self.ui.first_player_combo.currentText())
        actual_players.append(self.ui.second_player_combo.currentText())
        squad.append(self.ui.first_squad_player_combo.currentText())
        squad.append(self.ui.second_squad_player_combo.currentText(), )
        return actual_players, squad, checked_buttons

    def process_data_compare_players(self):
        """It takes the data from the database and sends it to the chart widget to be displayed"""
        players_info, squads, options_info = self.send_data_compare_graphic()
        self.ui.spyder_graph_widget.spyder_chart.set_chart(
            players_info, squads, options_info)

    def collect_scout_data(self):
        """It takes the values from the GUI and puts them into a list"""
        attrs_set = []
        stats_set = []
        if self.language == "en":
            for value_child, operator_child, identifier in zip(
                    self.ui.right_column.scroll_area_1.findChildren(QLineEdit),
                    self.ui.right_column.scroll_area_1.findChildren(QComboBox),
                    util_lists.list_en[2],
            ):
                if value_child.text() == "":
                    tmp_value_child = float(0)
                else:
                    tmp_value_child = float(value_child.text().replace(
                        ",", "."))

                attrs_set.append([
                    identifier,
                    operator_child.currentText(), tmp_value_child
                ])
            for value_child, operator_child, identifier in zip(
                    self.ui.right_column.scroll_area_2.findChildren(QLineEdit),
                    self.ui.right_column.scroll_area_2.findChildren(QComboBox),
                    util_lists.list_en[0],
            ):
                if value_child.text() == "":
                    tmp_value_child = float(0)
                else:
                    tmp_value_child = float(value_child.text().replace(
                        ",", "."))

                stats_set.append([
                    identifier,
                    operator_child.currentText(), tmp_value_child
                ])
        if self.language == "es":
            for value_child, operator_child, identifier in zip(
                    self.ui.right_column.scroll_area_1.findChildren(QLineEdit),
                    self.ui.right_column.scroll_area_1.findChildren(QComboBox),
                    util_lists.list_es[2],
            ):
                if value_child.text() == "":
                    tmp_value_child = float(0)
                else:
                    tmp_value_child = float(value_child.text().replace(
                        ",", "."))

                attrs_set.append([
                    identifier,
                    operator_child.currentText(), tmp_value_child
                ])
            for value_child, operator_child, identifier in zip(
                    self.ui.right_column.scroll_area_2.findChildren(QLineEdit),
                    self.ui.right_column.scroll_area_2.findChildren(QComboBox),
                    util_lists.list_es[0],
            ):
                if value_child.text() == "":
                    tmp_value_child = float(0)
                else:
                    tmp_value_child = float(value_child.text().replace(
                        ",", "."))

                stats_set.append([
                    identifier,
                    operator_child.currentText(), tmp_value_child
                ])
        self.filter_scout_data(stats_set, attrs_set)

    def filter_scout_data(self, stats, attrs):
        """
        This function filters the dataframe based on the attributes and stats that the user has selected

        :param stats: A list of lists, where each list is a stat and the operator and value to filter by
        :param attrs: a list of lists, each list containing the attribute name, the operator, and the value
        """
        filtered_df = self.df_scout_for_table.copy()
        for _, item in enumerate(attrs):
            if item[1] == ">" and item[2] == 0.0:
                continue
            if item[1] == ">":
                filtered_df = filtered_df[
                    filtered_df[item[0]] > item[2]]
            if item[1] == "<":
                if item[2] > 0.0:
                    filtered_df = filtered_df[
                        filtered_df[item[0]] < item[2]]
                elif item[2] == 0.0:
                    continue
            if item[1] == ">=":
                filtered_df = filtered_df[
                    filtered_df[item[0]] >= item[2]]
            if item[1] == "<=":
                filtered_df = filtered_df[
                    filtered_df[item[0]] <= item[2]]

        for _, item in enumerate(stats):
            if item[1] == ">" and item[2] == 0.0:
                continue
            if item[1] == ">":
                filtered_df = filtered_df[
                    filtered_df[item[0]] > item[2]]
            if item[1] == "<":
                if item[2] > 0.0:
                    filtered_df = filtered_df[
                        filtered_df[item[0]] < item[2]]
                elif item[2] == 0.0:
                    continue
            if item[1] == ">=":
                filtered_df = filtered_df[
                    filtered_df[item[0]] >= item[2]]
            if item[1] == "<=":
                filtered_df = filtered_df[
                    filtered_df[item[0]] <= item[2]]

        self.tables_helper_scouting(filtered_df)

    def collect_results_clustering(self):
        """
        It collects the values of the filters and returns them as a list
        :return: A list of lists.
        """
        data = []
        if self.language == "en":
            for value_child, operator_child, identifier in zip(
                    self.ui.load_pages.clustering_filters_frame.findChildren(
                        QLineEdit),
                    self.ui.load_pages.clustering_filters_frame.findChildren(
                        QComboBox),
                    util_lists.filters_en,
            ):
                if value_child.text() == "":
                    tmp_value_child = float(0)
                else:
                    tmp_value_child = float(value_child.text().replace(
                        ",", "."))

                data.append([
                    identifier,
                    operator_child.currentText(), tmp_value_child
                ])
        if self.language == "es":
            for value_child, operator_child, identifier in zip(
                    self.ui.load_pages.clustering_filters_frame.findChildren(
                        QLineEdit),
                    self.ui.load_pages.clustering_filters_frame.findChildren(
                        QComboBox),
                    util_lists.filters_es,
            ):
                if value_child.text() == "":
                    tmp_value_child = float(0)
                else:
                    tmp_value_child = float(value_child.text().replace(
                        ",", "."))

                data.append([
                    identifier,
                    operator_child.currentText(), tmp_value_child
                ])

        return data

    def clustering_management(self):
        """It takes a dataframe, performs some clustering, and then plots the results"""
        tmp_filters = self.collect_results_clustering()
        base_columns_plus = None
        complementary_df = None
        df_alone = None
        tmp_df = None
        col_name = self.df_scouting.columns[0]
        if self.language == "en":
            tmp_df = self.df_scouting[util_lists.numerical_clustering_en]
            complementary_df = self.df_scouting[util_lists.list_en[0]]
            df_alone = self.df_squad[self.df_squad[col_name].str.contains(
                self.ui.clustering_player_combo.currentText())]
            df_alone = df_alone[util_lists.numerical_clustering_en]
        elif self.language == "es":
            tmp_df = self.df_scouting[util_lists.numerical_clustering_es]
            complementary_df = self.df_scouting[util_lists.list_es[0]]
            df_alone = self.df_squad[self.df_squad[col_name].str.contains(
                self.ui.clustering_player_combo.currentText())]
            df_alone = df_alone[util_lists.numerical_clustering_es]

        df_player_clusters = tmp_df.fillna(tmp_df.mean())

        names = self.df_scouting[col_name].values.tolist()

        names.append(self.ui.clustering_player_combo.currentText())
        df_player_clusters = pd.concat([df_player_clusters, df_alone], axis=0)

        x = df_player_clusters.values
        scaler = preprocessing.MinMaxScaler()
        x_scaled = scaler.fit_transform(x)
        x_norm = pd.DataFrame(x_scaled)

        pca = PCA(n_components=2)
        reduced = pd.DataFrame(pca.fit_transform(x_norm))

        kmeans = KMeans(n_clusters=5)
        kmeans = kmeans.fit(reduced)
        _labels = kmeans.predict(reduced)  # skipcq: PYL-W0612 lgtm [py/unused-local-variable]
        _centroid = kmeans.cluster_centers_  # skipcq: PYL-W0612 lgtm [py/unused-local-variable]
        clusters = kmeans.labels_.tolist()

        reduced["cluster"] = clusters
        reduced[col_name] = names
        reduced = pd.concat([reduced, complementary_df], axis=1)

        base_columns = ["x", "y", "cluster", col_name]
        if self.language == "en":
            base_columns_plus = base_columns + util_lists.list_en[0]
        elif self.language == "es":
            base_columns_plus = base_columns + util_lists.list_es[0]

        reduced.columns = base_columns_plus

        player_x = float(
            reduced[reduced[col_name] == self.ui.clustering_player_combo.
                    currentText()]["x"].tolist()[0])
        player_y = float(
            reduced[reduced[col_name] == self.ui.clustering_player_combo.
                    currentText()]["y"].tolist()[0])

        reduced["dist_to_player"] = np.sqrt((player_x - reduced["x"])**2 +
                                            (player_y - reduced["y"])**2)

        player_cluster = int(
            reduced[reduced[col_name] == self.ui.clustering_player_combo.
                    currentText()]["cluster"].tolist()[0])
        df_p_s_c = reduced[(reduced["cluster"] == player_cluster)]
        for index, element in enumerate(tmp_filters):  # skipcq: PYL-W0612
            if tmp_filters[index][1] == ">" and tmp_filters[index][2] == 0.0:
                continue
            if tmp_filters[index][1] == ">":
                df_p_s_c = df_p_s_c[
                    df_p_s_c[tmp_filters[index][0]] > tmp_filters[index][2]]
            if tmp_filters[index][1] == "<":
                if tmp_filters[index][2] > 0.0:
                    df_p_s_c = df_p_s_c[df_p_s_c[tmp_filters[index][0]] <
                                        tmp_filters[index][2]]
                elif tmp_filters[index][2] == 0.0:
                    continue

            if tmp_filters[index][1] == ">=":
                df_p_s_c = df_p_s_c[
                    df_p_s_c[tmp_filters[index][0]] >= tmp_filters[index][2]]

            if tmp_filters[index][1] == "<=":
                df_p_s_c = df_p_s_c[
                    df_p_s_c[tmp_filters[index][0]] <= tmp_filters[index][2]]

        df_p_s_c = df_p_s_c[df_p_s_c[col_name] !=
                            self.ui.clustering_player_combo.currentText()]
        df_p_s_c = df_p_s_c.sort_values(by="dist_to_player", ascending=True)
        printable_names = df_p_s_c[col_name].values.tolist()
        self.ui.clustering_chart.inner_chart.update_chart(
            reduced, printable_names,
            self.ui.clustering_player_combo.currentText())
        self.ui.clustering_chart.add_player_to_list(printable_names)

    # ///////////////////////////////////////////
    # END CUSTOM FUNCTIONS FOR FUNCTIONALITY
    # ///////////////////////////////////////////


# MAIN FUNCTION TO START
# Set initial class and also additional parameter of the "QApplication" class
# ///////////////////////////////////////////
def main():
    """
    `main()` is the entry point of the application. It creates an instance of the `QApplication` class, which is the
    main class of the Qt framework. It also creates an instance of the `MainWindow` class, which is the main window
    of the application
    """
    # APPLICATION
    # ///////////////////////////////////////////
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # EXEC EXIT APP
    # ///////////////////////////////////////////
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
