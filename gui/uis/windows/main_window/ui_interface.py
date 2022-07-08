# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
# IMPORT KHAMISIKIBET WIDGET
# ///////////////////////////////////////////
from Custom_Widgets.Widgets import QCustomSlideMenu

# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget
)
from PySide6.QtCore import QEasingCurve, QParallelAnimationGroup, QPropertyAnimation, Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtSvgWidgets import QSvgWidget

from gui.core.functions import set_svg_icon, set_svg_image

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# RIGHT COLUMN
# ///////////////////////////////////////////////////////////////
from gui.uis.columns.ui_right_column import Ui_RightColumn

# IMPORT MAIN WINDOW PAGES / AND SIDE BOXES FOR APP
# ///////////////////////////////////////////////////////////////
from gui.uis.pages.ui_main_pages import Ui_MainPages

# IMPORT CUSTOM WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import (
    PyClusteringWidget,
    PyComboBox,
    PyCredits,
    PyLeftColumn,
    PyLeftMenu,
    PyPushButton,
    PySpyderWidget,
    PyStatsWidget,
    PyTableWidget,
    PyTitleBar,
    PyVerticalPitch,
    PyWindow,
    PyButtonGroup,
)
from gui.widgets.py_title_bar.py_title_button import PyTitleButton


# PY WINDOW
# ///////////////////////////////////////////////////////////////
# This class is used to create all interface of the application
class Ui_MainWindow(object):

    def __init__(self):
        self.delete_session_btn = None
        self.load_session_btn = None
        self.save_session_btn = None
        self.group = None
        self.right_box = None
        self.left_box = None
        self.icon_spanish = None
        self.spanish_language_btn = None
        self.icon_english = None
        self.english_language_btn = None
        self.right_btn_3 = None
        self.icon_left = None
        self.right_btn_2 = None
        self.icon_right = None
        self.right_btn_1 = None
        self.clustering_chart = None
        self.group_clustering_filters = None
        self.clustering_btn_send = None
        self.clustering_player_combo = None
        self.group_lineedits_stats_widget = None
        self.group_lineedits_attrs_widget = None
        self.table_scouting = None
        self.btn_send = None
        self.group_chk_stats_widget = None
        self.group_chk_attrs_widget = None
        self.btn_compare_attrs = None
        self.btn_compare_stats = None
        self.spyder_graph_widget = None
        self.second_player_combo = None
        self.second_squad_player_combo = None
        self.first_player_combo = None
        self.first_squad_player_combo = None
        self.graph_statistics = None
        self.table_tactic = None
        self.table_squad = None
        self.logo_svg = None
        self.load_old_btn = None
        self.load_scouting_btn = None
        self.load_squad_btn = None
        self.language = None
        self.list_label = None
        self.btn_close_notification = None
        self.title_notification = None
        self.title_notification_frame_layout = None
        self.title_notification_frame = None
        self.popup_notification_subcontainer_layout = None
        self.popup_notification_subcontainer = None
        self.popup_notification_container_layout = None
        self.popup_notification_container = None
        self.credits = None
        self.credits_layout = None
        self.credits_frame = None
        self.pitch_widget = None
        self.load_pages = None
        self.content_area_left_frame = None
        self.right_column = None
        self.content_area_right_bg_frame = None
        self.content_area_right_layout = None
        self.right_column_frame = None
        self.content_area_layout = None
        self.content_area_frame = None
        self.title_bar = None
        self.title_bar_layout = None
        self.title_bar_frame = None
        self.right_app_layout = None
        self.right_app_frame = None
        self.left_column = None
        self.left_column_layout = None
        self.left_column_frame = None
        self.left_menu = None
        self.left_menu_layout = None
        self.left_menu_frame = None
        self.window = None
        self.central_widget_layout = None
        self.central_widget = None
        self.themes = None
        self.settings = None

    def setupUi(self, parent):
        """
        Initialize interface of the main window

        :param parent: The parent widget of the window
        """
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # SET INITIAL PARAMETERS
        # ///////////////////////////////////////////////////////////////
        parent.resize(self.settings["startup_size"][0],
                      self.settings["startup_size"][1])
        parent.setMinimumSize(self.settings["minimum_size"][0],
                              self.settings["minimum_size"][1])

        # SET CENTRAL WIDGET
        # Add central widget to app
        # ///////////////////////////////////////////////////////////////
        self.central_widget = QWidget()
        self.central_widget.setStyleSheet(f"""
            font: {self.settings["font"]["text_size"]}pt "{self.settings["font"]["family"]}";
            color: {self.themes["app_color"]["text_foreground"]};
        """)
        self.central_widget_layout = QVBoxLayout(self.central_widget)

        if self.settings["custom_title_bar"]:
            self.central_widget_layout.setContentsMargins(10, 10, 10, 10)
        else:
            self.central_widget_layout.setContentsMargins(0, 0, 0, 0)

        # LOAD PY WINDOW CUSTOM WIDGET
        # Add inside PyWindow "layout" all Widgets
        # ///////////////////////////////////////////////////////////////
        self.window = PyWindow(
            parent,
            bg_color=self.themes["app_color"]["bg_one"],
            border_color=self.themes["app_color"]["bg_two"],
            text_color=self.themes["app_color"]["text_foreground"],
        )

        # If disable custom title bar
        if not self.settings["custom_title_bar"]:
            self.window.set_stylesheet(border_radius=0, border_size=0)

        # ADD PY WINDOW TO CENTRAL WIDGET
        self.central_widget_layout.addWidget(self.window)

        # ADD FRAME LEFT MENU
        # Add here custom left bar
        # ///////////////////////////////////////////////////////////////
        left_menu_margin = self.settings["left_menu_content_margins"]
        left_menu_minimum = self.settings["left_menu_size"]["minimum"]
        self.left_menu_frame = QFrame()
        self.left_menu_frame.setMaximumSize(
            left_menu_minimum + (left_menu_margin * 2), 17280)
        self.left_menu_frame.setMinimumSize(
            left_menu_minimum + (left_menu_margin * 2), 0)

        # LEFT MENU LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.left_menu_layout = QHBoxLayout(self.left_menu_frame)
        self.left_menu_layout.setContentsMargins(left_menu_margin,
                                                 left_menu_margin,
                                                 left_menu_margin,
                                                 left_menu_margin)

        # ADD LEFT MENU
        # Add custom left menu here
        # ///////////////////////////////////////////////////////////////
        self.left_menu = PyLeftMenu(
            parent=self.left_menu_frame,
            app_parent=self.central_widget,
            dark_one=self.themes["app_color"]["dark_one"],
            dark_three=self.themes["app_color"]["dark_three"],
            dark_four=self.themes["app_color"]["dark_four"],
            bg_one=self.themes["app_color"]["bg_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_pressed"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            context_color=self.themes["app_color"]["context_color"],
            text_foreground=self.themes["app_color"]["text_foreground"],
            text_active=self.themes["app_color"]["text_active"],
        )

        self.left_menu_layout.addWidget(self.left_menu)

        # ADD LEFT COLUMN
        # Add here the left column with Stacked Widgets
        # ///////////////////////////////////////////////////////////////
        self.left_column_frame = QFrame()
        self.left_column_frame.setMaximumWidth(
            self.settings["left_column_size"]["minimum"])
        self.left_column_frame.setMinimumWidth(
            self.settings["left_column_size"]["minimum"])
        self.left_column_frame.setStyleSheet(
            f"background: {self.themes['app_color']['bg_two']}")

        # ADD LAYOUT TO LEFT COLUMN
        # ///////////////////////////////////////////////////////////////
        self.left_column_layout = QVBoxLayout(self.left_column_frame)
        self.left_column_layout.setContentsMargins(0, 0, 0, 0)

        # ADD CUSTOM LEFT MENU WIDGET
        # ///////////////////////////////////////////////////////////////
        self.left_column = PyLeftColumn(
            parent,
            app_parent=self.central_widget,
            text_title="Settings Left Frame",
            text_title_size=self.settings["font"]["title_size"],
            text_title_color=self.themes["app_color"]["text_foreground"],
            icon_path=set_svg_icon("icon_settings.svg"),
            dark_one=self.themes["app_color"]["dark_one"],
            bg_color=self.themes["app_color"]["bg_three"],
            btn_color=self.themes["app_color"]["bg_three"],
            btn_color_hover=self.themes["app_color"]["bg_two"],
            btn_color_pressed=self.themes["app_color"]["bg_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            context_color=self.themes["app_color"]["context_color"],
            icon_color_pressed=self.themes["app_color"]["icon_pressed"],
            icon_close_path=set_svg_icon("icon_close.svg"),
        )

        self.left_column_layout.addWidget(self.left_column)

        # ADD RIGHT WIDGETS
        # Add here the right widgets
        # ///////////////////////////////////////////////////////////////
        self.right_app_frame = QFrame()

        # ADD RIGHT APP LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.right_app_layout = QVBoxLayout(self.right_app_frame)
        self.right_app_layout.setContentsMargins(3, 3, 3, 3)
        self.right_app_layout.setSpacing(6)

        # ADD TITLE BAR FRAME
        # ///////////////////////////////////////////////////////////////
        self.title_bar_frame = QFrame()
        self.title_bar_frame.setMinimumHeight(40)
        self.title_bar_frame.setMaximumHeight(40)
        self.title_bar_layout = QVBoxLayout(self.title_bar_frame)
        self.title_bar_layout.setContentsMargins(0, 0, 0, 0)

        # ADD CUSTOM TITLE BAR
        # ///////////////////////////////////////////////////////////////
        self.title_bar = PyTitleBar(
            parent,
            logo_width=100,
            app_parent=self.central_widget,
            logo_image="logotop_100x22.svg",
            bg_color=self.themes["app_color"]["bg_two"],
            div_color=self.themes["app_color"]["bg_three"],
            btn_bg_color=self.themes["app_color"]["bg_two"],
            btn_bg_color_hover=self.themes["app_color"]["bg_three"],
            btn_bg_color_pressed=self.themes["app_color"]["bg_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_pressed"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            context_color=self.themes["app_color"]["context_color"],
            dark_one=self.themes["app_color"]["dark_one"],
            text_foreground=self.themes["app_color"]["text_foreground"],
            radius=8,
            font_family=self.settings["font"]["family"],
            title_size=self.settings["font"]["title_size"],
            is_custom_title_bar=self.settings["custom_title_bar"],
        )

        self.title_bar_layout.addWidget(self.title_bar)

        # ADD CONTENT AREA
        # ///////////////////////////////////////////////////////////////
        self.content_area_frame = QFrame()

        # CONTENT AREA LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.content_area_layout = QHBoxLayout(self.content_area_frame)
        self.content_area_layout.setContentsMargins(0, 0, 0, 0)
        self.content_area_layout.setSpacing(0)

        # RIGHT BAR
        # ///////////////////////////////////////////////////////////////
        self.right_column_frame = QFrame()
        self.right_column_frame.setMinimumWidth(
            self.settings["right_column_size"]["minimum"])
        self.right_column_frame.setMaximumWidth(
            self.settings["right_column_size"]["minimum"])

        # IMPORT RIGHT COLUMN
        # ///////////////////////////////////////////////////////////////
        self.content_area_right_layout = QVBoxLayout(self.right_column_frame)
        self.content_area_right_layout.setContentsMargins(5, 5, 5, 5)
        self.content_area_right_layout.setSpacing(0)

        # RIGHT BG
        # ///////////////////////////////////////////////////////////////
        self.content_area_right_bg_frame = QFrame()
        self.content_area_right_bg_frame.setObjectName(
            "content_area_right_bg_frame")
        self.content_area_right_bg_frame.setStyleSheet(f"""
        #content_area_right_bg_frame {{
            border-radius: 8px;
            background-color: {self.themes["app_color"]["bg_two"]};
        }}
        """)

        # ADD BG
        self.content_area_right_layout.addWidget(
            self.content_area_right_bg_frame)

        # ADD RIGHT PAGES TO RIGHT COLUMN
        self.right_column = Ui_RightColumn()
        self.right_column.setupUi(self.content_area_right_bg_frame)

        # LEFT CONTENT
        # ///////////////////////////////////////////////////////////////
        self.content_area_left_frame = QFrame()

        # IMPORT MAIN PAGES
        # ///////////////////////////////////////////////////////////////
        self.load_pages = Ui_MainPages()
        self.load_pages.setupUi(self.content_area_left_frame)

        # ADD TO LAYOUT
        self.content_area_layout.addWidget(self.content_area_left_frame)
        self.content_area_layout.addWidget(self.right_column_frame)

        # ADD PITCH WIDGET
        # ///////////////////////////////////////////////////////////////
        self.pitch_widget = PyVerticalPitch(
            parent=self.load_pages.vertical_pitch_frame)

        # CREDITS / BOTTOM APP FRAME
        # ///////////////////////////////////////////////////////////////
        self.credits_frame = QFrame()
        self.credits_frame.setMinimumHeight(26)
        self.credits_frame.setMaximumHeight(26)

        # CREATE LAYOUT CREDITS
        # ///////////////////////////////////////////////////////////////
        self.credits_layout = QVBoxLayout(self.credits_frame)
        self.credits_layout.setContentsMargins(0, 0, 0, 0)

        # ADD CUSTOM CREDIT WDIGET
        # ///////////////////////////////////////////////////////////////
        self.credits = PyCredits(
            bg_two=self.themes["app_color"]["bg_two"],
            copyright_text=self.settings["copyright"],
            version=self.settings["version"],
            font_family=self.settings["font"]["family"],
            text_size=self.settings["font"]["text_size"],
            text_description_color=self.themes["app_color"]
            ["text_description"],
        )

        # ADD TO CREDITS LAYOUT
        self.credits_layout.addWidget(self.credits)

        # START NOTIFICATION SECTION

        # CREATE POPUP NOTIFICATION CONTAINER
        # ///////////////////////////////////////////////////////////////
        # TODO FIX STYLE
        self.popup_notification_container = QCustomSlideMenu(
            self.right_app_frame)
        self.popup_notification_container.setObjectName(
            "popup_notification_container")

        # CREATE LAYOUT POPUP NOTIFICATION CONTAINER
        # ///////////////////////////////////////////////////////////////
        self.popup_notification_container_layout = QVBoxLayout(
            self.popup_notification_container)
        self.popup_notification_container_layout.setObjectName(
            "popup_notification_container_layout")
        self.popup_notification_container_layout.setContentsMargins(0, 0, 0, 0)

        # CREATE POPUP NOTIFICATION SUBCONTAINER
        # ///////////////////////////////////////////////////////////////
        self.popup_notification_subcontainer = QWidget()
        self.popup_notification_subcontainer.setObjectName(
            "popup_notification_subcontainer")

        # CREATE LAYOUT POPUP NOTIFICATION SUBCONTAINER
        # ///////////////////////////////////////////////////////////////
        self.popup_notification_subcontainer_layout = QVBoxLayout(
            self.popup_notification_subcontainer)
        self.popup_notification_subcontainer_layout.setObjectName(
            "popup_notification_subcontainer_layout")
        self.popup_notification_subcontainer_layout.setContentsMargins(0, 0, 0, 0)

        # CREATE LIST NOTIFICATION FRAME
        # ///////////////////////////////////////////////////////////////
        self.title_notification_frame = QFrame()
        self.title_notification_frame.setObjectName("title_notification_frame")
        size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.title_notification_frame.sizePolicy().hasHeightForWidth())
        self.title_notification_frame.setSizePolicy(size_policy)
        self.title_notification_frame.setFrameShape(QFrame.StyledPanel)
        self.title_notification_frame.setFrameShadow(QFrame.Raised)
        self.title_notification_frame.setMaximumHeight(30)

        # CREATE LAYOUT LIST NOTIFICATION FRAME
        # ///////////////////////////////////////////////////////////////
        self.title_notification_frame_layout = QHBoxLayout(
            self.title_notification_frame)
        self.title_notification_frame_layout.setObjectName(
            "title_notification_frame_layout")
        self.title_notification_frame_layout.setContentsMargins(3, 3, 3, 3)

        # Title notification
        self.title_notification = QLabel()
        self.title_notification.setObjectName("title_notification")
        size_policy1 = QSizePolicy(QSizePolicy.Expanding,
                                   QSizePolicy.Preferred)
        size_policy1.setHorizontalStretch(0)
        size_policy1.setVerticalStretch(0)
        size_policy1.setHeightForWidth(
            self.title_notification.sizePolicy().hasHeightForWidth())
        self.title_notification.setSizePolicy(size_policy1)
        font = QFont()
        font.setBold(True)
        self.title_notification.setFont(font)
        self.title_notification.setAlignment(Qt.AlignLeading | Qt.AlignLeft
                                             | Qt.AlignVCenter)
        self.title_notification.setText("PLAYER LIST")

        # Button close notification
        self.btn_close_notification = PyTitleButton(
            self.title_notification_frame,
            self.popup_notification_subcontainer,
            width=24,
            height=24,
            radius=6,
            tooltip_text="Close popup",
            bg_color="transparent",
            icon_path=set_svg_icon("icon_close.svg"),
        )
        self.btn_close_notification.delete_tooltip()

        self.btn_close_notification.setObjectName("btn_close_notification")

        self.title_notification_frame_layout.addWidget(self.title_notification)
        self.title_notification_frame_layout.addWidget(
            self.btn_close_notification, 0, Qt.AlignRight)

        # ADD LIST NOTIFICATION FRAME
        self.popup_notification_subcontainer_layout.addWidget(
            self.title_notification_frame)


        # TAG NOTIFICATION FRAME
        self.tag_notification_frame = QFrame()
        self.tag_notification_frame.setObjectName("tag_notification_frame")
        self.tag_notification_frame.setFrameShape(QFrame.StyledPanel)
        self.tag_notification_frame.setFrameShadow(QFrame.Raised)
        self.tag_notification_frame.setStyleSheet(
            """
            QPushButton {
            font-size: 12px;
            padding: 4px;
            border-radius: 8px;
            border: 1px solid rgba(194, 221, 255, 0.8);
            background: rgba(194, 221, 255, 0.3);
            color: #dce1ec;
            }
            
            QPushButton:hover {
            background: rgba(63, 111, 209, 0.5);
            }
            """
        )
        self.tag_notification_frame_layout = QVBoxLayout(self.tag_notification_frame)
        self.tag_notification_frame_layout.setObjectName("tag_notification_frame_layout")
        self.tag_notification_frame_layout.setContentsMargins(5, 3, 5, 2)
        self.tag_notification_frame_layout.setSpacing(4)

        self.popup_notification_subcontainer_layout.addWidget(self.tag_notification_frame)

        self.tag_notification_frame.raise_()

        # ADD SUBCONTAINER TO CONTAINER
        self.popup_notification_container_layout.addWidget(
            self.popup_notification_subcontainer)

        # END NOTIFICATION SECTION

        # ADD WIDGETS TO RIGHT LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.right_app_layout.addWidget(self.title_bar_frame)
        self.right_app_layout.addWidget(self.content_area_frame)
        self.right_app_layout.addWidget(
            self.popup_notification_container)  # TEST
        self.right_app_layout.addWidget(self.credits_frame)

        self.popup_notification_container.setStyleSheet(
            "    #popup_notification_subcontainer{\n"
            "	border-color: #343b48;\n"
            "	border-radius:10px;\n"
            "	border-width: 1px;\n"
            "	margin: 0px;\n"
            "	background-color: #343b48;\n"
            "\n"
            "}\n"
            "\n"
            "#label_list {\n"
            "   border: 1px;\n"
            "   border-color: #1b1e23;\n"
            "   border-style: solid;\n"
            "	border-bottom-left-radius:10px;\n"
            "	border-bottom-right-radius:10px;\n"
            "	background-color: #3c4454;\n"
            "color: #dce1ec;\n"
            "\n"
            "}\n"
            "\n"
            "#title_notification_frame {\n"
            "	background-color:#1b1e23;\n"
            "border-top-right-radius: 10px;\n"
            "border-top-left-radius: 10px;\n"
            "}\n"
            "\n"
            "#title_notification {\n"
            "padding-left: 7px;\n"
            "color: #dce1ec;\n"
            "}")

        # ADD WIDGETS TO "PyWindow"
        # ///////////////////////////////////////////////////////////////
        self.window.layout.addWidget(self.left_menu_frame)
        self.window.layout.addWidget(self.left_column_frame)
        self.window.layout.addWidget(self.right_app_frame)

        # ADD CENTRAL WIDGET AND SET CONTENT MARGINS
        # ///////////////////////////////////////////////////////////////
        parent.setCentralWidget(self.central_widget)

    # ADD LEFT BUTTON
    # ///////////////////////////////////////////////////////////////
    add_left_buttons = [
        {
            "btn_icon": "icon_home.svg",
            "btn_id": "btn_home",
            "btn_text": "Home",
            "btn_tooltip": "Home page",
            "show_top": True,
            "is_active": True,
        },
        {
            "btn_icon": "icon_squad.svg",
            "btn_id": "btn_squad",
            "btn_text": "Squad",
            "btn_tooltip": "Show your squad",
            "show_top": True,
            "is_active": False,
        },
        {
            "btn_icon": "icon_tactic.svg",
            "btn_id": "btn_tactic",
            "btn_text": "Tactic",
            "btn_tooltip": "Show your tactic",
            "show_top": True,
            "is_active": False,
        },
        {
            "btn_icon": "icon_stats.svg",
            "btn_id": "btn_stats",
            "btn_text": "Statistics",
            "btn_tooltip": "Show statistics",
            "show_top": True,
            "is_active": False,
        },
        {
            "btn_icon": "icon_compare.svg",
            "btn_id": "btn_compare",
            "btn_text": "Compare",
            "btn_tooltip": "Comparation between players",
            "show_top": True,
            "is_active": False,
        },
        {
            "btn_icon": "icon_scouting.svg",
            "btn_id": "btn_scouting",
            "btn_text": "Scouting",
            "btn_tooltip": "Show scouted players",
            "show_top": True,
            "is_active": False,
        },
        {
            "btn_icon": "icon_metrics.svg",
            "btn_id": "btn_clustering",
            "btn_text": "PCA & KMeans Clustering",
            "btn_tooltip": "Clustering players",
            "show_top": True,
            "is_active": False,
        },
        {
            "btn_icon": "icon_settings.svg",
            "btn_id": "btn_settings",
            "btn_text": "Settings",
            "btn_tooltip": "Open settings",
            "show_top": False,
            "is_active": False,
        },
        {
            "btn_icon": "icon_info.svg",
            "btn_id": "btn_languages",
            "btn_text": "Languages",
            "btn_tooltip": "Open languages",
            "show_top": False,
            "is_active": False,
        },
        {
            "btn_icon": "icon_help.svg",
            "btn_id": "btn_help",
            "btn_text": "Help",
            "btn_tooltip": "Open help",
            "show_top": False,
            "is_active": False,
        },
    ]

    # ADD TITLE BAR BUTTONS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_buttons = [
        {
            "btn_icon": "icon_refresh.svg",
            "btn_id": "btn_refresh",
            "btn_tooltip": "Refresh",
            "is_active": False,
        },
        {
            "btn_icon": "icon_settings.svg",
            "btn_id": "btn_top_settings",
            "btn_tooltip": "Top settings",
            "is_active": False,
        },
    ]

    # ADD PLAYERS BUTTONS
    # ///////////////////////////////////////////////////////////////
    add_players_pitch_buttons = [
        {
            "btn_id": "btn_pos_1",
            "is_active": False,
            "size": 48,
            "posX": 250,
            "posY": 710,
        },
        {
            "btn_id": "btn_pos_2",
            "is_active": False,
            "size": 48,
            "posX": 175,
            "posY": 630,
        },
        {
            "btn_id": "btn_pos_3",
            "is_active": False,
            "size": 48,
            "posX": 327,
            "posY": 630,
        },
        {
            "btn_id": "btn_pos_4",
            "is_active": False,
            "size": 48,
            "posX": 450,
            "posY": 595,
        },
        {
            "btn_id": "btn_pos_5",
            "is_active": False,
            "size": 48,
            "posX": 50,
            "posY": 595,
        },
        {
            "btn_id": "btn_pos_6",
            "is_active": False,
            "size": 48,
            "posX": 250,
            "posY": 490,
        },
        {
            "btn_id": "btn_pos_7",
            "is_active": False,
            "size": 48,
            "posX": 155,
            "posY": 360,
        },
        {
            "btn_id": "btn_pos_8",
            "is_active": False,
            "size": 48,
            "posX": 347,
            "posY": 360,
        },
        {
            "btn_id": "btn_pos_9",
            "is_active": False,
            "size": 48,
            "posX": 50,
            "posY": 210,
        },
        {
            "btn_id": "btn_pos_10",
            "is_active": False,
            "size": 48,
            "posX": 450,
            "posY": 210,
        },
        {
            "btn_id": "btn_pos_11",
            "is_active": False,
            "size": 48,
            "posX": 250,
            "posY": 110,
        },
    ]

    # SETUP CUSTOM BUTTONS
    # Get sender() function when button is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        """
        If the sender is not None, return the sender of the button
        :return: The sender() method returns the object that emitted the signal.
        """
        if self.title_bar.sender() is not None:
            return self.title_bar.sender()
        if self.left_menu.sender() is not None:
            return self.left_menu.sender()
        if self.left_column.sender() is not None:
            return self.left_column.sender()
        if self.pitch_widget.sender() is not None:
            return self.pitch_widget.sender()
        return None

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETER
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        """
        The function `setup_gui` is called when the application is started. It sets up the GUI by adding buttons to
        the left menu, title bar, and pitch widget. It also sets the initial page and left and right menus
        """
        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD BUTTONS
        self.left_menu.add_menus(Ui_MainWindow.add_left_buttons)

        # TITLE BAR / EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD BUTTONS
        self.title_bar.add_menus(Ui_MainWindow.add_title_bar_buttons)

        # PITCH WIDGET / ADD BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD BUTTONS
        self.pitch_widget.add_btns(Ui_MainWindow.add_players_pitch_buttons)

        # ADD TITLE
        if self.settings["custom_title_bar"]:
            self.title_bar.set_title(self.settings["app_name"])
        else:
            self.title_bar.set_title("Welcome to FM Helper")

        # SET INITIAL PAGE / LEFT & RIGHT MENUS
        # ///////////////////////////////////////////////////////////////
        self.set_page(self.load_pages.page_1)
        self.set_left_column_menu(
            menu=self.left_column.menus.menu_1,
            title="Settings Left Column",
            icon_path=set_svg_icon("icon_settings.svg"),
        )
        self.set_right_column_menu(self.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # CUSTOM WIDGETS
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LANGUAGE
        # ///////////////////////////////////////////////////////////////
        self.language = self.settings["language"]

        # LEFT COLUMN CONFIGURATION
        # ///////////////////////////////////////////////////////////////
        # Load Squad Btn
        self.load_squad_btn = PyPushButton(
            name="squad",
            text="Load squad file",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
        )
        self.load_squad_btn.setMaximumHeight(40)
        self.left_column.menus.btn_1_layout.addWidget(self.load_squad_btn)

        # Load Scouting Btn
        self.load_scouting_btn = PyPushButton(
            name="scouting",
            text="Load scouting file",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
        )
        self.load_scouting_btn.setMaximumHeight(40)
        self.load_scouting_btn.setEnabled(False)
        self.left_column.menus.btn_2_layout.addWidget(self.load_scouting_btn)

        # Load Old Btn
        self.load_old_btn = PyPushButton(
            name="old",
            text="Load old squad file",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
        )
        self.load_old_btn.setMaximumHeight(40)
        self.load_old_btn.setEnabled(False)
        self.left_column.menus.btn_3_layout.addWidget(self.load_old_btn)
        # Save Session Btn
        self.save_session_btn = PyPushButton(
            name="save_session",
            text="Save actual session",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
        )
        self.save_session_btn.setMaximumHeight(40)
        self.save_session_btn.setMinimumHeight(40)
        self.left_column.menus.btn_6_layout.addWidget(self.save_session_btn)
        # Load Session Btn
        self.load_session_btn = PyPushButton(
            name="load_session",
            text="Load recently session",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
        )
        self.load_session_btn.setMaximumHeight(40)
        self.load_session_btn.setMinimumHeight(40)
        self.left_column.menus.btn_7_layout.addWidget(self.load_session_btn)
        # Delete sesion btn
        self.delete_session_btn = PyPushButton(
            name="delete_session",
            text="Delete actual session",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
        )
        self.delete_session_btn.setMaximumHeight(40)
        self.delete_session_btn.setMinimumHeight(40)
        self.left_column.menus.btn_8_layout.addWidget(self.delete_session_btn)

        # PAGES CONFIGURATION
        # ///////////////////////////////////////////////////////////////
        # COMMON SECTION FOR ALL PAGES
        # ///////////////////////////////////////////////////////////////

        # PAGE 1 - Introduction to App
        self.logo_svg = QSvgWidget(set_svg_image("logo.svg"))

        self.load_pages.logo_layout.addWidget(self.logo_svg, Qt.AlignCenter,
                                              Qt.AlignCenter)

        # PAGE 2 - Squad view
        # Add table model
        self.table_squad = PyTableWidget(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["dark_two"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["dark_two"],
            header_vertical_color=self.themes["app_color"]["bg_three"],
            bottom_line_color=self.themes["app_color"]["bg_three"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"],
        )
        # ADD WIDGETS TO PAGE 2
        self.load_pages.row_1_layout.addWidget(self.table_squad)

        # PAGE 3 - Tactic view

        # Add table list
        self.table_tactic = PyTableWidget(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["dark_two"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["dark_two"],
            header_vertical_color=self.themes["app_color"]["bg_three"],
            bottom_line_color=self.themes["app_color"]["bg_three"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"],
        )

        # ADD WIDGETS TO PAGE 3
        self.load_pages.list_table_layout.addWidget(self.table_tactic)

        # PAGE 5 - Statistics view

        self.graph_statistics = PyStatsWidget(
            name="graph_statistics",
            language=self.language,
            dark_one=self.themes["app_color"]["dark_one"],
            text_foreground=self.themes["app_color"]["text_foreground"],
            combo_border=self.themes["app_color"]["context_hover"],
            bg_two=self.themes["app_color"]["bg_two"],
            dark_three=self.themes["app_color"]["dark_three"],
            axis_color=self.themes["app_color"]["icon_active"],
            color_title=self.themes["app_color"]["text_title"],
            bar_color=self.themes["app_color"]["context_pressed"],
        )
        self.load_pages.column_1_layout_5.addWidget(self.graph_statistics)

        # PAGE 7 - Compare view
        # LEFT TOP SIDE OF PAGE
        # ///////////////////////////////////////////////////////////////

        # COMBO BOX TO SELECT SQUAD OF THE FIRST PLAYER TO COMPARE
        self.first_squad_player_combo = PyComboBox(
            dark_one=self.themes["app_color"]["dark_one"],
            text_foreground=self.themes["app_color"]["text_foreground"],
            combo_border=self.themes["app_color"]["context_hover"],
        )

        # COMBO BOX TO SELECT THE FIRST PLAYER DEPENDING ON THE SQUAD
        self.first_player_combo = PyComboBox(
            dark_one=self.themes["app_color"]["dark_one"],
            text_foreground=self.themes["app_color"]["text_foreground"],
            combo_border=self.themes["app_color"]["context_hover"],
        )

        # COMBO BOX TO SELECT SQUAD OF THE SECOND PLAYER TO COMPARE
        self.second_squad_player_combo = PyComboBox(
            dark_one=self.themes["app_color"]["dark_one"],
            text_foreground=self.themes["app_color"]["text_foreground"],
            combo_border=self.themes["app_color"]["context_hover"],
        )

        # COMBO BOX TO SELECT THE SECOND PLAYER DEPENDING ON THE SQUAD
        self.second_player_combo = PyComboBox(
            dark_one=self.themes["app_color"]["dark_one"],
            text_foreground=self.themes["app_color"]["text_foreground"],
            combo_border=self.themes["app_color"]["context_hover"],
        )

        # LEFT BOTTOM SIDE
        # ///////////////////////////////////////////////////////////////
        self.spyder_graph_widget = PySpyderWidget(
            language=self.language,
            bg_two=self.themes["app_color"]["bg_two"],
            bg_one=self.themes["app_color"]["bg_one"],
            dark_three=self.themes["app_color"]["dark_three"],
            axis_color=self.themes["app_color"]["icon_active"],
            color_title=self.themes["app_color"]["text_title"],
            line_color=self.themes["app_color"]["context_pressed"],
        )

        # RIGHT SIDE
        # ///////////////////////////////////////////////////////////////
        self.btn_compare_stats = PyPushButton(
            text="Select Statistics",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            name="stats",
        )
        self.btn_compare_stats.setMaximumHeight(40)

        self.btn_compare_attrs = PyPushButton(
            text="Select Attributes",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            name="attrs",
        )
        self.btn_compare_attrs.setEnabled(False)
        self.btn_compare_attrs.setMaximumHeight(40)

        # MID RIGHT SIDE
        # ///////////////////////////////////////////////////////////////
        self.group_chk_attrs_widget = PyButtonGroup()

        self.group_chk_stats_widget = PyButtonGroup()

        # BOTTOM  RIGHT SIDE
        self.btn_send = PyPushButton(
            text="Send Data",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            name="send_data",
        )
        self.btn_send.setMaximumHeight(40)

        # ADDING WIDGETS TO ITS RESPECTIVE LAYOUT
        # Left Side
        self.load_pages.compare_sub1_top_left_frame_layout.addWidget(
            self.first_squad_player_combo)
        self.load_pages.compare_sub1_top_left_frame_layout.addWidget(
            self.second_squad_player_combo)
        self.load_pages.compare_sub2_top_left_frame_layout.addWidget(
            self.first_player_combo)
        self.load_pages.compare_sub2_top_left_frame_layout.addWidget(
            self.second_player_combo)

        # Left Bottom Side
        self.load_pages.compare_bottom_left_frame_layout.addWidget(
            self.spyder_graph_widget)

        # Right Side
        self.load_pages.btn_compare_1_layout.addWidget(self.btn_compare_stats)
        self.load_pages.btn_compare_2_layout.addWidget(self.btn_compare_attrs)

        # Mid Right Side
        self.load_pages.menu1_compare_layout.addWidget(
            self.group_chk_attrs_widget)
        self.load_pages.menu2_compare_layout.addWidget(
            self.group_chk_stats_widget)

        # Bottom Right Side
        self.load_pages.btn_send_layout.addWidget(self.btn_send)

        # PAGE 8 - Scouting view
        self.table_scouting = PyTableWidget(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["dark_two"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["dark_two"],
            header_vertical_color=self.themes["app_color"]["bg_three"],
            bottom_line_color=self.themes["app_color"]["bg_three"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"],
        )
        # ADD WIDGETS TO PAGE 8
        self.load_pages.row_1_layout_8.addWidget(self.table_scouting)

        self.group_lineedits_attrs_widget = PyButtonGroup()

        self.group_lineedits_stats_widget = PyButtonGroup()

        # ADD LINEEDITS FOR FILTER IN PAGE 8
        self.right_column.scroll_area_1.setWidget(
            self.group_lineedits_attrs_widget)
        self.right_column.scroll_area_2.setWidget(
            self.group_lineedits_stats_widget)

        # PAGE 9 - Help view

        # PAGE 10 - Clustering view
        self.clustering_player_combo = PyComboBox(
            dark_one=self.themes["app_color"]["dark_one"],
            text_foreground=self.themes["app_color"]["text_foreground"],
            combo_border=self.themes["app_color"]["context_hover"],
        )
        self.load_pages.clustering_combo_layout.addWidget(
            self.clustering_player_combo)

        self.clustering_btn_send = PyPushButton(
            text="Process data",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
        )
        self.clustering_btn_send.setMaximumHeight(40)
        self.clustering_btn_send.setMaximumWidth(250)

        self.load_pages.clustering_btn_layout.addWidget(
            self.clustering_btn_send)

        self.group_clustering_filters = PyButtonGroup()
        self.load_pages.clustering_filters_layout.addWidget(
            self.group_clustering_filters)

        self.clustering_chart = PyClusteringWidget(
            language=self.language,
            bg_two=self.themes["app_color"]["bg_two"],
            dark_three=self.themes["app_color"]["dark_three"],
            axis_color=self.themes["app_color"]["icon_active"],
            color_title=self.themes["app_color"]["text_title"],
        )

        self.load_pages.clustering_bottom_layout.addWidget(
            self.clustering_chart)

        # RIGHT COLUMN CONFIGURATION
        # ///////////////////////////////////////////////////////////////

        # Button to change to menu 2
        self.right_btn_1 = PyPushButton(
            text="Show Menu 2",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
        )
        self.icon_right = QIcon(set_svg_icon("icon_arrow_right.svg"))
        self.right_btn_1.setIcon(self.icon_right)
        self.right_btn_1.setMaximumHeight(40)
        self.right_column.btn_1_menu_1_layout.addWidget(self.right_btn_1)

        # Button to change to menu 1
        self.right_btn_2 = PyPushButton(
            text="Show Menu 1",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
        )
        self.icon_left = QIcon(set_svg_icon("icon_arrow_left.svg"))
        self.right_btn_2.setIcon(self.icon_left)
        self.right_btn_2.setMaximumHeight(40)

        self.right_column.btn_1_menu_2_layout.addWidget(self.right_btn_2)

        # FILTER DATA BUTTON
        self.right_btn_3 = PyPushButton(
            text="Filter Data",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
        )
        self.right_btn_3.setMaximumHeight(40)
        self.right_column.filter_data_btn_layout.addWidget(self.right_btn_3)
        # LEFT COLUMN CONFIGURATION
        # ///////////////////////////////////////////////////////////////
        # ENGLISH BUTTON
        # Button to change UI to english
        # ///////////////////////////////////////////////////////////////
        self.english_language_btn = PyPushButton(
            text="English",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
        )
        self.icon_english = QIcon(set_svg_image("us.svg"))
        self.english_language_btn.setIcon(self.icon_english)
        self.english_language_btn.setMaximumHeight(40)

        self.left_column.menus.btn_4_layout.addWidget(
            self.english_language_btn)

        # SPANISH BUTTON
        # Button to change UI to spanish
        # ///////////////////////////////////////////////////////////////
        self.spanish_language_btn = PyPushButton(
            text="Español",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
        )
        self.icon_spanish = QIcon(set_svg_image("es.svg"))
        self.spanish_language_btn.setIcon(self.icon_spanish)
        self.spanish_language_btn.setMaximumHeight(40)

        self.left_column.menus.btn_5_layout.addWidget(
            self.spanish_language_btn)

        # ///////////////////////////////////////////////////////////////
        # END CUSTOM WIDGETS

    # SET MAIN WINDOW PAGES
    # ///////////////////////////////////////////////////////////////
    def set_page(self, page):
        """
        It sets the current page of the QStackedWidget to the page that is passed in

        :param page: The page to set the current page to
        """
        self.load_pages.pages.setCurrentWidget(page)

    # SET LEFT COLUMN PAGES
    # ///////////////////////////////////////////////////////////////
    def set_left_column_menu(self, menu, title, icon_path):
        """
        It sets the current widget of the menus QStackedWidget of left menu

        :param menu: The menu to be displayed
        :param title: The title of the menu
        :param icon_path: The path to the icon you want to use
        """
        self.left_column.menus.menus.setCurrentWidget(menu)
        self.left_column.title_label.setText(title)
        self.left_column.icon.set_icon(icon_path)

    # RETURN IF LEFT COLUMN IS VISIBLE
    # ///////////////////////////////////////////////////////////////
    def left_column_is_visible(self):
        """
        If the width of the left column frame is 0, then the left column is not visible.
        :return: The if its True or False.
        """
        width = self.left_column_frame.width()
        if width == 0:
            return False
        return True

    # RETURN IF RIGHT COLUMN IS VISIBLE
    # ///////////////////////////////////////////////////////////////
    def right_column_is_visible(self):
        """
        If the width of the right column frame is 0, then the right column is not visible.
        :return: The if its True or False.
        """
        width = self.right_column_frame.width()
        if width == 0:
            return False
        return True

    # SET RIGHT COLUMN PAGES
    # ///////////////////////////////////////////////////////////////
    def set_right_column_menu(self, menu):
        """
        It sets the current widget of the right column to the menu passed in

        :param menu: The menu to set
        """
        self.right_column.menus.setCurrentWidget(menu)

    # SET COMPARE COLUMN PAGES
    # ///////////////////////////////////////////////////////////////
    def set_compare_column_menu(self, menu, button):
        """
        It sets the current widget of the compare_pages QStackedWidget to the menu QWidget, and then disables the button
        that was clicked and enables the other button

        :param menu: the menu to be displayed
        :param button: The button that was clicked
        """
        self.load_pages.compare_pages.setCurrentWidget(menu)
        if "attrs" in button.get_name():
            self.btn_compare_attrs.setEnabled(False)
            self.btn_compare_stats.setEnabled(True)
        else:
            self.btn_compare_stats.setEnabled(False)
            self.btn_compare_attrs.setEnabled(True)

    # GET TITLE BUTTON BY OBJECT NAME
    # ///////////////////////////////////////////////////////////////
    def get_title_bar_btn(self, object_name):
        """
        It returns a QPushButton object from the title_bar_frame to know which button was clicked

        :param object_name: The name of the object you want to find
        :return: The title bar button with the object name passed in.
        """
        return self.title_bar_frame.findChild(QPushButton, object_name)

    # GET TITLE BUTTON BY OBJECT NAME
    # ///////////////////////////////////////////////////////////////
    def get_left_menu_btn(self, object_name):
        """
        It returns a QPushButton object from the left_menu QWidget object

        :param object_name: The name of the object you want to find
        :return: The left_menu object is being returned.
        """
        return self.left_menu.findChild(QPushButton, object_name)

    # LEFT AND RIGHT COLUMNS / SHOW / HIDE
    # ///////////////////////////////////////////////////////////////
    def toggle_left_column(self):
        """
        It gets the width of the left column and the right column, and then it starts an animation that will change the
        width of the left column to 0 and the width of the right column to the sum of the widths of the left and right
        columns
        """
        # GET ACTUAL COLUMN SIZE
        width = self.left_column_frame.width()
        right_column_width = self.right_column_frame.width()

        self.start_box_animation(width, right_column_width, "left")

    def toggle_right_column(self):
        """
        It gets the width of the left column, gets the width of the right column, and then calls a function that
        animates the width of the right column to 0
        """
        # GET ACTUAL COLUMNS SIZE
        left_column_width = self.left_column_frame.width()
        width = self.right_column_frame.width()

        self.start_box_animation(left_column_width, width, "right")

    def start_box_animation(self, left_box_width, right_box_width, direction):
        """
        It animates the left and right columns of the main window

        :param left_box_width: The current width of the left box
        :param right_box_width: The current width of the right box
        :param direction: left or right
        """
        _right_width = 0
        _left_width = 0
        time_animation = self.settings["time_animation"]
        minimum_left = self.settings["left_column_size"]["minimum"]
        maximum_left = self.settings["left_column_size"]["maximum"]
        minimum_right = self.settings["right_column_size"]["minimum"]
        maximum_right = self.settings["right_column_size"]["maximum"]

        # Check left Values
        if left_box_width == minimum_left and direction == "left":
            _left_width = maximum_left
        else:
            _left_width = minimum_left

        # Check right values
        if right_box_width == minimum_right and direction == "right":
            _right_width = maximum_right
        else:
            _right_width = minimum_right

        # ANIMATION LEFT BOX
        self.left_box = QPropertyAnimation(self.left_column_frame,
                                           b"minimumWidth")
        self.left_box.setDuration(time_animation)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(_left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX
        self.right_box = QPropertyAnimation(self.right_column_frame,
                                            b"minimumWidth")
        self.right_box.setDuration(time_animation)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(_right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.stop()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()
