
from pyside_core import *


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(1051, 858)
        # MAIN WIDGET LAYOUT
        # /////////////////////////////////////////////////////////
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)

        # MAIN PAGES
        # /////////////////////////////////////////////////////////
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")

        # PAGE 1
        # /////////////////////////////////////////////////////////
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.welcome_base = QFrame(self.page_1)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(300, 150))
        self.welcome_base.setMaximumSize(QSize(300, 150))
        self.welcome_base.setFrameShape(QFrame.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Raised)
        self.center_page_layout = QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(300, 120))
        self.logo.setMaximumSize(QSize(300, 120))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.center_page_layout.addWidget(self.logo)

        self.label = QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.center_page_layout.addWidget(self.label)

        self.page_1_layout.addWidget(self.welcome_base, 0, Qt.AlignHCenter)

        self.pages.addWidget(self.page_1)

        # PAGE 2
        # /////////////////////////////////////////////////////////
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_2)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 840, 580))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout.addLayout(self.row_1_layout)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_2)

        # PAGE 3
        # /////////////////////////////////////////////////////////
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setSpacing(5)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.page_3_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area_tactic = QScrollArea(self.page_3)
        self.scroll_area_tactic.setObjectName(u"scroll_area_tactic")
        self.scroll_area_tactic.setStyleSheet(u"background: transparent;")
        self.scroll_area_tactic.setFrameShape(QFrame.NoFrame)
        self.scroll_area_tactic.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_tactic.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_tactic.setWidgetResizable(True)
        self.scroll_area_tactic.setAlignment(Qt.AlignCenter)
        self.content_tactic = QWidget()
        self.content_tactic.setObjectName(u"content_tactic")
        self.content_tactic.setGeometry(QRect(0, 0, 1031, 838))
        self.content_tactic.setStyleSheet(u"background: transparent;")
        self.horizontalLayout = QHBoxLayout(self.content_tactic)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.vertical_pitch_frame = QFrame(self.content_tactic)
        self.vertical_pitch_frame.setObjectName(u"vertical_pitch_frame")
        self.vertical_pitch_frame.setMinimumSize(QSize(550, 790))
        self.vertical_pitch_frame.setFrameShape(QFrame.NoFrame)
        self.vertical_pitch_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.vertical_pitch_frame)

        self.horizontalSpacer = QSpacerItem(198, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.list_table_frame = QFrame(self.content_tactic)
        self.list_table_frame.setObjectName(u"list_table_frame")
        self.list_table_frame.setMinimumSize(QSize(250, 600))
        self.list_table_frame.setFrameShape(QFrame.NoFrame)
        self.list_table_frame.setFrameShadow(QFrame.Raised)
        self.list_table_layout = QHBoxLayout(self.list_table_frame)
        self.list_table_layout.setSpacing(0)
        self.list_table_layout.setObjectName(u"list_table_layout")
        self.list_table_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.list_table_frame)

        self.scroll_area_tactic.setWidget(self.content_tactic)

        self.page_3_layout.addWidget(self.scroll_area_tactic)

        self.pages.addWidget(self.page_3)

        # PAGE 4
        # /////////////////////////////////////////////////////////
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.column_1_layout_4 = QVBoxLayout(self.page_4)
        self.column_1_layout_4.setObjectName(u"column_1_layout_5")
        self.column_1_layout_4.setContentsMargins(5, 5, 5, 5)
        self.column_1_layout_4.setSpacing(5)

        self.welcome_base_4 = QFrame(self.page_4)
        self.welcome_base_4.setObjectName(u"welcome_base")
        self.welcome_base_4.setMinimumSize(QSize(300, 180))
        self.welcome_base_4.setMaximumSize(QSize(300, 180))
        self.welcome_base_4.setFrameShape(QFrame.NoFrame)
        self.welcome_base_4.setFrameShadow(QFrame.Raised)
        self.center_page_layout_4 = QVBoxLayout(self.welcome_base_4)
        self.center_page_layout_4.setObjectName(u"center_page_layout_4")
        self.center_page_layout_4.setContentsMargins(0, 0, 0, 0)
        self.center_page_layout_4.setSpacing(10)
        self.logo_4 = QFrame(self.welcome_base_4)
        self.logo_4.setObjectName(u"logo_4")
        self.logo_4.setMinimumSize(QSize(250, 150))
        self.logo_4.setMaximumSize(QSize(250, 150))
        self.logo_4.setFrameShape(QFrame.NoFrame)
        self.logo_4.setFrameShadow(QFrame.Raised)
        self.logo_layout_4 = QHBoxLayout(self.logo_4)
        self.logo_layout_4.setObjectName(u"logo_layout_4")
        self.logo_layout_4.setContentsMargins(0, 0, 0, 0)
        self.logo_layout_4.setSpacing(0)

        self.center_page_layout_4.addWidget(self.logo_4)

        self.column_1_layout_4.addWidget(self.welcome_base_4, 0, Qt.AlignHCenter)

        self.pages.addWidget(self.page_4)

        # PAGE 5
        # /////////////////////////////////////////////////////////
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")

        self.column_1_layout_5 = QHBoxLayout(self.page_5)
        self.column_1_layout_5.setObjectName(u"column_1_layout_5")

        self.pages.addWidget(self.page_5)

        # PAGE 6
        # /////////////////////////////////////////////////////////
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")

        self.column_1_layout_6 = QHBoxLayout(self.page_6)
        self.column_1_layout_6.setObjectName(u"column_1_layout_6")

        self.pages.addWidget(self.page_6)

        # PAGE 7
        # /////////////////////////////////////////////////////////
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")

        # Main Page 7 Layout
        self.page_7_main_layout = QHBoxLayout(self.page_7)
        self.page_7_main_layout.setObjectName(u"page_7_main_layout")
        self.page_7_main_layout.setContentsMargins(3, 3, 3, 3)
        self.page_7_main_layout.setSpacing(0)

        # Left Frame (Page 7)
        self.compare_left_frame = QFrame()
        self.compare_left_frame_layout = QVBoxLayout(self.compare_left_frame)

        # Left Top Frame (Page 7)
        self.compare_top_left_frame = QFrame()
        self.compare_top_left_frame.setMaximumHeight(150)
        self.compare_top_left_frame_layout = QVBoxLayout(self.compare_top_left_frame)

        # Sub1 Left Top Frame (Page 7)
        self.compare_sub1_top_left_frame = QFrame()
        self.compare_sub1_top_left_frame_layout = QHBoxLayout(self.compare_sub1_top_left_frame)

        # Sub2 Left Top Frame (Page 7)
        self.compare_sub2_top_left_frame = QFrame()
        self.compare_sub2_top_left_frame_layout = QHBoxLayout(self.compare_sub2_top_left_frame)

        self.compare_top_left_frame_layout.addWidget(self.compare_sub1_top_left_frame)
        self.compare_top_left_frame_layout.addWidget(self.compare_sub2_top_left_frame)

        # Left Bottom Frame (Page 7)
        self.compare_bottom_left_frame = QFrame()
        self.compare_bottom_left_frame_layout = QHBoxLayout(self.compare_bottom_left_frame)


        self.compare_left_frame_layout.addWidget(self.compare_top_left_frame)
        self.compare_left_frame_layout.addWidget(self.compare_bottom_left_frame)

        # Right Frame (Page 7)
        self.compare_right_frame = QFrame()
        self.compare_right_frame.setMinimumWidth(450)
        self.compare_right_frame.setMaximumWidth(500)
        self.compare_right_frame_layout = QVBoxLayout(self.compare_right_frame)

        # Frame for first button
        self.btn_compare_1_frame = QFrame()
        self.btn_compare_1_frame.setObjectName("btn_compare_1_frame")
        self.btn_compare_1_frame.setMinimumSize(QSize(0, 40))
        self.btn_compare_1_frame.setMaximumSize(QSize(16777215, 40))
        self.btn_compare_1_layout = QVBoxLayout(self.btn_compare_1_frame)
        self.btn_compare_1_layout.setContentsMargins(0, 0, 0, 0)
        self.btn_compare_1_layout.setSpacing(0)

        self.compare_right_frame_layout.addWidget(self.btn_compare_1_frame)

        # Frame for second button
        self.btn_compare_2_frame = QFrame()
        self.btn_compare_2_frame.setObjectName("btn_compare_2_frame")
        self.btn_compare_2_frame.setMinimumSize(QSize(0, 40))
        self.btn_compare_2_frame.setMaximumSize(QSize(16777215, 40))
        self.btn_compare_2_layout = QVBoxLayout(self.btn_compare_2_frame)
        self.btn_compare_2_layout.setContentsMargins(0, 0, 0, 0)
        self.btn_compare_2_layout.setSpacing(0)

        self.compare_right_frame_layout.addWidget(self.btn_compare_2_frame)

        # Stacked for change between attrs and stats
        self.compare_pages = QStackedWidget()
        self.compare_pages.setObjectName("compare_pages")

        # Menu 1
        self.menu1_compare = QWidget()
        self.menu1_compare.setObjectName("menu1_compare")
        self.menu1_compare_layout = QHBoxLayout(self.menu1_compare)
        self.menu1_compare_layout.setContentsMargins(5, 5, 5, 5)
        self.menu1_compare_layout.setSpacing(5)
        # ANADIR AQUI LOS CHECKBOX DE ATTRS

        self.compare_pages.addWidget(self.menu1_compare)

        # Menu 2
        self.menu2_compare = QWidget()
        self.menu2_compare.setObjectName("menu2_compare")
        self.menu2_compare_layout = QHBoxLayout(self.menu2_compare)
        self.menu2_compare_layout.setContentsMargins(5, 5, 5, 5)
        self.menu2_compare_layout.setSpacing(5)
        # ANADIR AQUI LOS CHECKBOX DE STATS

        self.compare_pages.addWidget(self.menu2_compare)
        self.compare_pages.setCurrentIndex(0)

        self.compare_right_frame_layout.addWidget(self.compare_pages)

        # Frame for 'send' button
        self.btn_send_frame = QFrame()
        self.btn_send_frame.setObjectName("btn_send_frame")
        self.btn_send_frame.setMinimumSize(QSize(0, 40))
        self.btn_send_frame.setMaximumSize(QSize(16777215, 40))
        self.btn_send_layout = QVBoxLayout(self.btn_send_frame)
        self.btn_send_layout.setContentsMargins(0, 0, 0, 0)
        self.btn_send_layout.setSpacing(0)

        self.compare_right_frame_layout.addWidget(self.btn_send_frame)

        self.page_7_main_layout.addWidget(self.compare_left_frame)
        self.page_7_main_layout.addWidget(self.compare_right_frame)

        self.pages.addWidget(self.page_7)

        # PAGE 8
        # /////////////////////////////////////////////////////////
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.page_8_layout = QVBoxLayout(self.page_8)
        self.page_8_layout.setSpacing(5)
        self.page_8_layout.setObjectName(u"page_8_layout")
        self.page_8_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area_8 = QScrollArea(self.page_8)
        self.scroll_area_8.setObjectName(u"scroll_area_8")
        self.scroll_area_8.setStyleSheet(u"background: transparent;")
        self.scroll_area_8.setFrameShape(QFrame.NoFrame)
        self.scroll_area_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_8.setWidgetResizable(True)
        self.contents_8 = QWidget()
        self.contents_8.setObjectName(u"contents_8")
        self.contents_8.setGeometry(QRect(0, 0, 840, 580))
        self.contents_8.setStyleSheet(u"background: transparent;")
        self.verticalLayout_8 = QVBoxLayout(self.contents_8)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.row_1_layout_8 = QHBoxLayout()
        self.row_1_layout_8.setObjectName(u"row_1_layout_8")

        self.verticalLayout_8.addLayout(self.row_1_layout_8)

        self.scroll_area_8.setWidget(self.contents_8)

        self.page_8_layout.addWidget(self.scroll_area_8)

        self.pages.addWidget(self.page_8)

        # PAGE 9
        # /////////////////////////////////////////////////////////
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")

        self.pages.addWidget(self.page_9)

        # PAGE 10
        # /////////////////////////////////////////////////////////
        self.page10 = QWidget()
        self.page10.setObjectName(u"page10")

        self.pages.addWidget(self.page10)

        # ADD PAGES TO MAIN LAYOUT
        # /////////////////////////////////////////////////////////
        self.main_pages_layout.addWidget(self.pages)

        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(2)

        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Welcome To FM Excel Helper", None))
    # retranslateUi

