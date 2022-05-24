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


class Ui_MainWindow(object):
    def setupUi(self, parent):
        if not parent.objectName():
            parent.setObjectName(u"MainWindow")

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
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget_layout = QVBoxLayout(self.central_widget)
        self.central_widget_layout.setObjectName(u"central_widget_layout")

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
        self.window.setObjectName(u"window")

        # If disable custom title bar
        if not self.settings["custom_title_bar"]:
            self.window.set_stylesheet(border_radius=0, border_size=0)

        # ADD FRAME LEFT MENU
        # Add here custom left bar
        # ///////////////////////////////////////////////////////////////
        left_menu_margin = self.settings["left_menu_content_margins"]
        left_menu_minimum = self.settings["left_menu_size"]["minimum"]
        self.left_menu_frame = QFrame()
        self.left_menu_frame.setObjectName(u"left_menu_frame")
        self.left_menu_frame.setMaximumSize(left_menu_minimum + (left_menu_margin * 2), 17280)
        self.left_menu_frame.setMinimumSize(left_menu_minimum + (left_menu_margin * 2), 0)

        # LEFT MENU LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.left_menu_layout = QHBoxLayout(self.left_menu_frame)
        self.left_menu_layout.setObjectName(u"left_menu_layout")
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
        self.left_menu.setObjectName(u"left_menu")

        self.left_menu_layout.addWidget(self.left_menu)

        # ADD LEFT MENU
        # Add here the left column with Stacked Widgets
        # ///////////////////////////////////////////////////////////////
        self.left_column_frame = QFrame()
        self.left_column_frame.setObjectName(u"left_column_frame")
        self.left_column_frame.setMaximumWidth(self.settings["left_column_size"]["minimum"])
        self.left_column_frame.setMinimumWidth(self.settings["left_column_size"]["minimum"])
        self.left_column_frame.setStyleSheet(f"background: {self.themes['app_color']['bg_two']}")

        # ADD LAYOUT TO LEFT COLUMN
        # ///////////////////////////////////////////////////////////////
        self.left_column_layout = QVBoxLayout(self.left_column_frame)
        self.left_column_layout.setObjectName(u"left_column_layout")
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
        self.left_column.setObjectName(u"left_column")

        self.left_column_layout.addWidget(self.left_column)

        # ADD RIGHT WIDGETS
        # Add here the right widgets
        # ///////////////////////////////////////////////////////////////
        self.right_app_frame = QFrame()
        self.right_app_frame.setObjectName(u"right_app_frame")

        # ADD RIGHT APP LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.right_app_layout = QVBoxLayout(self.right_app_frame)
        self.right_app_layout.setObjectName(u"right_app_layout")
        self.right_app_layout.setContentsMargins(3, 3, 3, 3)
        self.right_app_layout.setSpacing(6)

        # ADD TITLE BAR FRAME
        # ///////////////////////////////////////////////////////////////
        self.title_bar_frame = QFrame()
        self.title_bar_frame.setObjectName(u"title_bar_frame")
        self.title_bar_layout = QVBoxLayout(self.title_bar_frame)
        self.title_bar_layout.setObjectName(u"title_bar_layout")
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
        self.title_bar.setObjectName(u"title_bar")

        self.title_bar_layout.addWidget(self.title_bar)

        self.right_app_layout.addWidget(self.title_bar_frame)  # TODO change position2

        # ADD CONTENT AREA
        # ///////////////////////////////////////////////////////////////
        self.content_area_frame = QFrame()
        self.content_area_frame.setObjectName(u"content_area_frame")

        # CONTENT AREA LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.content_area_layout = QHBoxLayout(self.content_area_frame)
        self.content_area_layout.setObjectName(u"content_area_layout")
        self.content_area_layout.setContentsMargins(0, 0, 0, 0)
        self.content_area_layout.setSpacing(0)

        # RIGHT BAR
        # ///////////////////////////////////////////////////////////////
        self.right_column_frame = QFrame(self.content_area_frame)
        self.right_column_frame.setObjectName(u"right_column_frame")

        # IMPORT RIGHT COLUMN
        # ///////////////////////////////////////////////////////////////
        self.content_area_right_layout = QVBoxLayout(self.right_column_frame)
        self.content_area_right_layout.setObjectName(u"content_area_right_layout")
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

        self.content_area_layout.addWidget(self.right_column_frame)

        # LEFT CONTENT
        # ///////////////////////////////////////////////////////////////
        self.content_area_left_frame = QFrame()
        self.content_area_left_frame.setObjectName(u"content_area_left_frame")

        # IMPORT MAIN PAGES
        # ///////////////////////////////////////////////////////////////
        self.load_pages = Ui_MainPages()
        self.load_pages.setupUi(self.content_area_left_frame)

        self.content_area_layout.addWidget(self.content_area_left_frame)

        self.right_app_layout.addWidget(self.content_area_frame)

        # CREDITS / BOTTOM APP FRAME
        # ///////////////////////////////////////////////////////////////
        self.credits_frame = QFrame()
        self.credits_frame.setObjectName(u"credits_frame")
        self.credits_frame.setMinimumHeight(26)
        self.credits_frame.setMaximumHeight(26)

        # CREATE LAYOUT CREDITS
        # ///////////////////////////////////////////////////////////////
        self.credits_layout = QVBoxLayout(self.credits_frame)
        self.credits_layout.setObjectName(u"credits_layout")
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
        self.credits.setObjectName(u"credits")

        # ADD TO CREDITS LAYOUT
        self.credits_layout.addWidget(self.credits)

        self.right_app_layout.addWidget(self.credits_frame)

        self.central_widget_layout.addWidget(self.window)  # TODO change position

        parent.setCentralWidget(self.central_widget)

