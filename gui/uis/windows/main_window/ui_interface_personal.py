# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.core.functions import Functions

# IMPORT PYSIDE CORE
# ///////////////////////////////////////////////////////////////
from pyside_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT CUSTOM WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# IMPORT MAIN WINDOW PAGES / AND SIDE BOXES FOR APP
# ///////////////////////////////////////////////////////////////
from gui.uis.pages.ui_main_pages import Ui_MainPages

# RIGHT COLUMN
# ///////////////////////////////////////////////////////////////
from gui.uis.columns.ui_right_column import Ui_RightColumn

# PY WINDOW
# ///////////////////////////////////////////////////////////////
class Ui_MainWindow(object):
    def setupUi(self, parent):
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
        parent.resize(self.settings["startup_size"][0], self.settings["startup_size"][1])
        parent.setMinimumSize(self.settings["minimum_size"][0], self.settings["minimum_size"][1])

        # SET CENTRAL WIDGET
        # Add central widget to app
        # ///////////////////////////////////////////////////////////////
        self.central_widget = QWidget()
        self.central_widget.setStyleSheet(f'''
            font: {self.settings["font"]["text_size"]}pt "{self.settings["font"]["family"]}";
            color: {self.themes["app_color"]["text_foreground"]};
        ''')
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
            text_color=self.themes["app_color"]["text_foreground"]
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
        self.left_menu_frame.setMaximumSize(left_menu_minimum + (left_menu_margin * 2), 17280)
        self.left_menu_frame.setMinimumSize(left_menu_minimum + (left_menu_margin * 2), 0)

        # LEFT MENU LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.left_menu_layout = QHBoxLayout(self.left_menu_frame)
        self.left_menu_layout.setContentsMargins(
            left_menu_margin,
            left_menu_margin,
            left_menu_margin,
            left_menu_margin
        )

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
            text_active=self.themes["app_color"]["text_active"]
        )

        self.left_menu_layout.addWidget(self.left_menu)

        # ADD LEFT COLUMN
        # Add here the left column with Stacked Widgets
        # ///////////////////////////////////////////////////////////////
        self.left_column_frame = QFrame()
        self.left_column_frame.setMaximumWidth(self.settings["left_column_size"]["minimum"])
        self.left_column_frame.setMinimumWidth(self.settings["left_column_size"]["minimum"])
        self.left_column_frame.setStyleSheet(f"background: {self.themes['app_color']['bg_two']}")

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
            icon_path=Functions.set_svg_icon("icon_settings.svg"),
            dark_one=self.themes["app_color"]["dark_one"],
            bg_color=self.themes["app_color"]["bg_three"],
            btn_color=self.themes["app_color"]["bg_three"],
            btn_color_hover=self.themes["app_color"]["bg_two"],
            btn_color_pressed=self.themes["app_color"]["bg_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            context_color=self.themes["app_color"]["context_color"],
            icon_color_pressed=self.themes["app_color"]["icon_pressed"],
            icon_close_path=Functions.set_svg_icon("icon_close.svg")
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
            logo_image="logo_top_100x22.svg",
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
            is_custom_title_bar=self.settings["custom_title_bar"]
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
        self.right_column_frame.setMinimumWidth(self.settings["right_column_size"]["minimum"])
        self.right_column_frame.setMaximumWidth(self.settings["right_column_size"]["minimum"])

        # IMPORT RIGHT COLUMN
        # ///////////////////////////////////////////////////////////////
        self.content_area_right_layout = QVBoxLayout(self.right_column_frame)
        self.content_area_right_layout.setContentsMargins(5, 5, 5, 5)
        self.content_area_right_layout.setSpacing(0)

        # RIGHT BG
        # ///////////////////////////////////////////////////////////////
        self.content_area_right_bg_frame = QFrame()
        self.content_area_right_bg_frame.setObjectName(u"content_area_right_bg_frame")
        self.content_area_right_bg_frame.setStyleSheet(f'''
        #content_area_right_bg_frame {{
            border-radius: 8px;
            background-color: {self.themes["app_color"]["bg_two"]};
        }}    
        ''')

        # ADD BG
        self.content_area_right_layout.addWidget(self.content_area_right_bg_frame)

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
            parent=self.load_pages.vertical_pitch_frame
        )

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
            copyright=self.settings["copyright"],
            version=self.settings["version"],
            font_family=self.settings["font"]["family"],
            text_size=self.settings["font"]["text_size"],
            text_description_color=self.themes["app_color"]["text_description"]
        )

        # ADD TO CREDITS LAYOUT
        self.credits_layout.addWidget(self.credits)

        ######## START NOTIFICATION SECTION ########

        # CREATE POPUP NOTIFICATION CONTAINER
        # ///////////////////////////////////////////////////////////////
        self.popup_notification_container = PyPopupNotification(self.right_app_frame)
        self.popup_notification_container.setObjectName(u"popup_notification_container")
        self.popup_notification_container.setMinimumHeight(40)
        self.popup_notification_container.setMaximumWidth(400)
        self.popup_notification_container.setStyleSheet(f'''
        #popup_notification_container {{
            background-color: red;
        }}
        ''')

        # CREATE LAYOUT POPUP NOTIFICATION CONTAINER
        # ///////////////////////////////////////////////////////////////
        self.popup_notification_container_layout = QVBoxLayout(self.popup_notification_container)
        self.popup_notification_container_layout.setObjectName(u"popup_notification_container_layout")

        # CREATE POPUP NOTIFICATION SUBCONTAINER
        # ///////////////////////////////////////////////////////////////
        self.popup_notification_subcontainer = QWidget()
        self.popup_notification_subcontainer.setObjectName(u"popup_notification_subcontainer")

        # CREATE LAYOUT POPUP NOTIFICATION SUBCONTAINER
        # ///////////////////////////////////////////////////////////////
        self.popup_notification_subcontainer_layout = QVBoxLayout(self.popup_notification_subcontainer)
        self.popup_notification_subcontainer_layout.setObjectName(u"popup_notification_subcontainer_layout")

        # CREATE LIST NOTIFICATION FRAME
        # ///////////////////////////////////////////////////////////////
        self.title_notification_frame = QFrame()
        self.title_notification_frame.setObjectName(u"list_notification_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_notification_frame.sizePolicy().hasHeightForWidth())
        self.title_notification_frame.setSizePolicy(sizePolicy)
        self.title_notification_frame.setFrameShape(QFrame.StyledPanel)
        self.title_notification_frame.setFrameShadow(QFrame.Raised)

        # CREATE LAYOUT LIST NOTIFICATION FRAME
        # ///////////////////////////////////////////////////////////////
        self.title_notification_frame_layout = QHBoxLayout(self.title_notification_frame)
        self.title_notification_frame_layout.setObjectName(u"list_notification_frame_layout")


        # Title notification
        self.title_notification = QLabel()
        self.title_notification.setObjectName(u"title_notification")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title_notification.sizePolicy().hasHeightForWidth())
        self.title_notification.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setBold(True)
        self.title_notification.setFont(font)
        self.title_notification.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.title_notification.setText("ESTE ES EL TITULOOO")

        # Button close notification
        self.btn_close_notification = QPushButton()
        self.btn_close_notification.setObjectName(u"btn_close_notification")

        self.title_notification_frame_layout.addWidget(self.title_notification)
        self.title_notification_frame_layout.addWidget(self.btn_close_notification, 0, Qt.AlignRight)

        # ADD LIST NOTIFICATION FRAME
        self.popup_notification_subcontainer_layout.addWidget(self.title_notification_frame)


        # List label
        self.list_label = QLabel()
        self.list_label.setObjectName(u"list_label")
        self.list_label.setFont(font)
        self.list_label.setAlignment(Qt.AlignCenter)
        self.list_label.setText("ESTA ES LA LISTAAAAA") # TEST

        # Add list label
        self.popup_notification_subcontainer_layout.addWidget(self.list_label)

        # ADD SUBCONTAINER TO CONTAINER
        self.popup_notification_container_layout.addWidget(self.popup_notification_subcontainer)


        ######## END NOTIFICATION SECTION  ########


        # ADD WIDGETS TO RIGHT LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.right_app_layout.addWidget(self.title_bar_frame)
        self.right_app_layout.addWidget(self.content_area_frame)
        self.right_app_layout.addWidget(self.popup_notification_container) # TEST
        self.right_app_layout.addWidget(self.credits_frame)


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
            "is_active": True
        },
        {
            "btn_icon": "icon_squad.svg",
            "btn_id": "btn_squad",
            "btn_text": "Squad",
            "btn_tooltip": "Show your squad",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_tactic.svg",
            "btn_id": "btn_tactic",
            "btn_text": "Tactic",
            "btn_tooltip": "Show your tactic",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_development.svg",
            "btn_id": "btn_development",
            "btn_text": "Development",
            "btn_tooltip": "Show flaws of your players",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_stats.svg",
            "btn_id": "btn_stats",
            "btn_text": "Statistics",
            "btn_tooltip": "Show statistics",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_metrics.svg",
            "btn_id": "btn_metrics",
            "btn_text": "Metrics",
            "btn_tooltip": "Show players metrics",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_compare.svg",
            "btn_id": "btn_compare",
            "btn_text": "Compare",
            "btn_tooltip": "Comparation between players",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_scouting.svg",
            "btn_id": "btn_scouting",
            "btn_text": "Scouting",
            "btn_tooltip": "Show scouted players",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_employees.svg",
            "btn_id": "btn_employees",
            "btn_text": "Employees",
            "btn_tooltip": "Show your staff",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_settings.svg",
            "btn_id": "btn_settings",
            "btn_text": "Settings",
            "btn_tooltip": "Open settings",
            "show_top": False,
            "is_active": False
        },
        {
            "btn_icon": "icon_info.svg",
            "btn_id": "btn_info",
            "btn_text": "Information",
            "btn_tooltip": "Open information",
            "show_top": False,
            "is_active": False
        },
        {
            "btn_icon": "icon_help.svg",
            "btn_id": "btn_help",
            "btn_text": "Help",
            "btn_tooltip": "Open help",
            "show_top": False,
            "is_active": False
        }
    ]

    # ADD TITLE BAR BUTTONS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_buttons = [
        {
            "btn_icon": "icon_refresh.svg",
            "btn_id": "btn_refresh",
            "btn_tooltip": "Refresh",
            "is_active": False
        },
        {
            "btn_icon": "icon_settings.svg",
            "btn_id": "btn_top_settings",
            "btn_tooltip": "Top settings",
            "is_active": False
        }
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
        if self.title_bar.sender() != None:
            return self.title_bar.sender()
        elif self.left_menu.sender() != None:
            return self.left_menu.sender()
        elif self.left_column.sender() != None:
            return self.left_column.sender()
        elif self.pitch_widget.sender() != None:
            return self.pitch_widget.sender()

    # TODO FIX SENDER FROM PITCH WIDGET
    # SETUP MAIN WINDOW WITH CUSTOM PARAMETER
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
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
            icon_path=Functions.set_svg_icon("icon_settings.svg")
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
            text="Load scouting file",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.load_scouting_btn.setMaximumHeight(40)
        self.load_scouting_btn.setEnabled(False)  # TODO enable button
        self.left_column.menus.btn_2_layout.addWidget(self.load_scouting_btn)

        # PAGES CONFIGURATION
        # ///////////////////////////////////////////////////////////////
        # PAGE 1 - Introduction to App
        # TODO edit layouts

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
            context_color=self.themes["app_color"]["context_color"]
        )
        # ADD WIDGETS TO PAGE 2
        self.load_pages.row_1_layout.addWidget(self.table_squad)

        # PAGE 3 - Tactic view

        # TODO descomentar si no funciona
        # self.pitch_image = QLabel(self.load_pages.vertical_pitch_frame)
        # self.pitch_image.setObjectName(u"pitch_image")
        # self.pitch_image.setGeometry(QRect(0, 0, 550, 820))
        # sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.pitch_image.sizePolicy().hasHeightForWidth())
        # self.pitch_image.setSizePolicy(sizePolicy)
        # self.pitch_image.setMinimumSize(QSize(550, 820))
        # self.pitch_image.setPixmap(QPixmap("gui/images/png_images/vertical_pitch.png"))
        # self.pitch_image.setScaledContents(True)
        # self.pitch_image.setAlignment(Qt.AlignCenter)
        # self.pitch_image.raise_()
        #
        # # Add pitch players
        # self.image_player = "icon_player_identifier.svg"
        # # BTN POS 1
        # self.btn_pos_1 = PyPlayerButton(
        #     icon_path=Functions.set_svg_icon(self.image_player),
        #     parent=self.load_pages.vertical_pitch_frame,
        #     app_parent=self.central_widget,
        #     btn_id="btn_pos_1",
        # )
        # self.btn_pos_1.setGeometry(QRect(250, 710, 48, 48))
        #
        # # BTN POS 2
        # self.btn_pos_2 = PyPlayerButton(
        #     icon_path=Functions.set_svg_icon(self.image_player),
        #     parent=self.load_pages.vertical_pitch_frame,
        #     app_parent=self.central_widget,
        #     btn_id="btn_pos_2",
        # )
        # self.btn_pos_2.setGeometry(QRect(175, 630, 48, 48))
        # # BTN POS 3
        # self.btn_pos_3 = PyPlayerButton(
        #     icon_path=Functions.set_svg_icon(self.image_player),
        #     parent=self.load_pages.vertical_pitch_frame,
        #     app_parent=self.central_widget,
        #     btn_id="btn_pos_3",
        # )
        # self.btn_pos_3.setGeometry(QRect(327, 630, 48, 48))
        # # BTN POS 4
        # self.btn_pos_4 = PyPlayerButton(
        #     icon_path=Functions.set_svg_icon(self.image_player),
        #     parent=self.load_pages.vertical_pitch_frame,
        #     app_parent=self.central_widget,
        #     btn_id="btn_pos_4",
        # )
        # self.btn_pos_4.setGeometry(QRect(450, 595, 48, 48))
        # # # BTN POS 5
        # self.btn_pos_5 = PyPlayerButton(
        #     icon_path=Functions.set_svg_icon(self.image_player),
        #     parent=self.load_pages.vertical_pitch_frame,
        #     app_parent=self.central_widget,
        #     btn_id="btn_pos_5",
        # )
        # self.btn_pos_5.setGeometry(QRect(50, 595, 48, 48))
        # # # BTN POS 6
        # self.btn_pos_6 = PyPlayerButton(
        #     icon_path=Functions.set_svg_icon(self.image_player),
        #     parent=self.load_pages.vertical_pitch_frame,
        #     app_parent=self.central_widget,
        #     btn_id="btn_pos_6",
        # )
        # self.btn_pos_6.setGeometry(QRect(250, 490, 48, 48))
        # # # BTN POS 7
        # self.btn_pos_7 = PyPlayerButton(
        #     icon_path=Functions.set_svg_icon(self.image_player),
        #     parent=self.load_pages.vertical_pitch_frame,
        #     app_parent=self.central_widget,
        #     btn_id="btn_pos_7",
        # )
        # self.btn_pos_7.setGeometry(QRect(155, 360, 48, 48))
        # # # BTN POS 8
        # self.btn_pos_8 = PyPlayerButton(
        #     icon_path=Functions.set_svg_icon(self.image_player),
        #     parent=self.load_pages.vertical_pitch_frame,
        #     app_parent=self.central_widget,
        #     btn_id="btn_pos_8",
        # )
        # self.btn_pos_8.setGeometry(QRect(347, 360, 48, 48))
        # # # BTN POS 9
        # self.btn_pos_9 = PyPlayerButton(
        #     icon_path=Functions.set_svg_icon(self.image_player),
        #     parent=self.load_pages.vertical_pitch_frame,
        #     app_parent=self.central_widget,
        #     btn_id="btn_pos_9",
        # )
        # self.btn_pos_9.setGeometry(QRect(50, 210, 48, 48))
        # # # BTN POS 10
        # self.btn_pos_10 = PyPlayerButton(
        #     icon_path=Functions.set_svg_icon(self.image_player),
        #     parent=self.load_pages.vertical_pitch_frame,
        #     app_parent=self.central_widget,
        #     btn_id="btn_pos_10",
        # )
        # self.btn_pos_10.setGeometry(QRect(450, 210, 48, 48))
        # # # BTN POS 11
        # self.btn_pos_11 = PyPlayerButton(
        #     icon_path=Functions.set_svg_icon(self.image_player),
        #     parent=self.load_pages.vertical_pitch_frame,
        #     app_parent=self.central_widget,
        #     btn_id="btn_pos_11",
        # )
        # self.btn_pos_11.setGeometry(QRect(250, 110, 48, 48))


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
            context_color=self.themes["app_color"]["context_color"]
        )

        # ADD WIDGETS TO PAGE 3
        self.load_pages.list_table_layout.addWidget(self.table_tactic)

        # RIGHT COLUMN CONFIGURATION
        # ///////////////////////////////////////////////////////////////

        # Button to change to menu 2
        self.right_btn_1 = PyPushButton(
            text="Show Menu 2",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_right = QIcon(Functions.set_svg_icon("icon_arrow_right.svg"))
        self.right_btn_1.setIcon(self.icon_right)
        self.right_btn_1.setMaximumHeight(40)
        self.right_btn_1.clicked.connect(lambda: self.set_right_column_menu(
            self.right_column.menu_2
        ))
        self.right_column.btn_1_menu_1_layout.addWidget(self.right_btn_1)

        # Button to change to menu 1
        self.right_btn_2 = PyPushButton(
            text="Show Menu 1",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_left = QIcon(Functions.set_svg_icon("icon_arrow_left.svg"))
        self.right_btn_2.setIcon(self.icon_left)
        self.right_btn_2.setMaximumHeight(40)
        self.right_btn_2.clicked.connect(lambda: self.set_right_column_menu(
            self.right_column.menu_1
        ))
        self.right_column.btn_1_menu_2_layout.addWidget(self.right_btn_2)

        # ENGLISH BUTTON
        # Button to change UI to english
        # ///////////////////////////////////////////////////////////////
        self.english_language_btn = PyPushButton(
            text="English",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_english = QIcon(Functions.set_svg_image("us.svg"))
        self.english_language_btn.setIcon(self.icon_english)
        self.english_language_btn.setMaximumHeight(40)
        # TODO connect function

        self.right_column.btn_en_layout.addWidget(self.english_language_btn)

        # SPANISH BUTTON
        # Button to change UI to spanish
        # ///////////////////////////////////////////////////////////////
        self.spanish_language_btn = PyPushButton(
            text="Español",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_spanish = QIcon(Functions.set_svg_image("es.svg"))
        self.spanish_language_btn.setIcon(self.icon_spanish)
        self.spanish_language_btn.setMaximumHeight(40)
        # TODO connect function

        self.right_column.btn_es_layout.addWidget(self.spanish_language_btn)

        # ///////////////////////////////////////////////////////////////
        # END CUSTOM WIDGETS

    # SET MAIN WINDOW PAGES
    # ///////////////////////////////////////////////////////////////
    def set_page(self, page):
        self.load_pages.pages.setCurrentWidget(page)

    # SET LEFT COLUMN PAGES
    # ///////////////////////////////////////////////////////////////
    def set_left_column_menu(self, menu, title, icon_path):
        self.left_column.menus.menus.setCurrentWidget(menu)
        self.left_column.title_label.setText(title)
        self.left_column.icon.set_icon(icon_path)

    # RETURN IF LEFT COLUMN IS VISIBLE
    # ///////////////////////////////////////////////////////////////
    def left_column_is_visible(self):
        width = self.left_column_frame.width()
        if width == 0:
            return False
        else:
            return True

    # RETURN IF RIGHT COLUMN IS VISIBLE
    # ///////////////////////////////////////////////////////////////
    def right_column_is_visible(self):
        width = self.right_column_frame.width()
        if width == 0:
            return False
        else:
            return True

    # SET RIGHT COLUMN PAGES
    # ///////////////////////////////////////////////////////////////
    def set_right_column_menu(self, menu):
        self.right_column.menus.setCurrentWidget(menu)

    # GET TITLE BUTTON BY OBJECT NAME
    # ///////////////////////////////////////////////////////////////
    def get_title_bar_btn(self, object_name):
        return self.title_bar_frame.findChild(QPushButton, object_name)

    # GET TITLE BUTTON BY OBJECT NAME
    # ///////////////////////////////////////////////////////////////
    def get_left_menu_btn(self, object_name):
        return self.left_menu.findChild(QPushButton, object_name)

    # LEFT AND RIGHT COLUMNS / SHOW / HIDE
    # ///////////////////////////////////////////////////////////////
    def toggle_left_column(self):
        # GET ACTUAL COLUMN SIZE
        width = self.left_column_frame.width()
        right_column_width = self.right_column_frame.width()

        self.start_box_animation(width, right_column_width, "left")

    def toggle_right_column(self):
        # GET ACTUAL COLUMNS SIZE
        left_column_width = self.left_column_frame.width()
        width = self.right_column_frame.width()

        self.start_box_animation(left_column_width, width, "right")

    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0
        time_animation = self.settings["time_animation"]
        minimum_left = self.settings["left_column_size"]["minimum"]
        maximum_left = self.settings["left_column_size"]["maximum"]
        minimum_right = self.settings["right_column_size"]["minimum"]
        maximum_right = self.settings["right_column_size"]["maximum"]

        # Check left Values
        if left_box_width == minimum_left and direction == "left":
            left_width = maximum_left
        else:
            left_width = minimum_left

        # Check right values
        if right_box_width == minimum_right and direction == "right":
            right_width = maximum_right
        else:
            right_width = minimum_right

        # ANIMATION LEFT BOX
        self.left_box = QPropertyAnimation(self.left_column_frame, b"minimumWidth")
        self.left_box.setDuration(time_animation)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX
        self.right_box = QPropertyAnimation(self.right_column_frame, b"minimumWidth")
        self.right_box.setDuration(time_animation)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.stop()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()