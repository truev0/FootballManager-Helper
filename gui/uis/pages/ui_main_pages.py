# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesyeoGXi.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(1051, 858)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
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

        # START NEW SECTION
        # ///////////////////////////////////////////////

        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")

        self.pages.addWidget(self.page_4)

        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")

        self.column_1_layout_5 = QHBoxLayout(self.page_5)
        self.column_1_layout_5.setObjectName(u"column_1_layout_5")

        self.pages.addWidget(self.page_5)

        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")

        self.pages.addWidget(self.page_6)

        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")

        self.pages.addWidget(self.page_7)

        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")

        self.pages.addWidget(self.page_8)

        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")

        self.pages.addWidget(self.page_9)

        self.page10 = QWidget()
        self.page10.setObjectName(u"page10")

        self.pages.addWidget(self.page10)

        # END NEW SECTION
        # ///////////////////////////////////////////////

        self.main_pages_layout.addWidget(self.pages)

        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(2)

        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Welcome To FM Excel Helper", None))
    # retranslateUi

