# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'right_columnIWUfAa.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from pyside_core import *

class Ui_RightColumn(object):
    def setupUi(self, RightColumn):
        if not RightColumn.objectName():
            RightColumn.setObjectName(u"RightColumn")
        RightColumn.resize(240, 600)
        self.main_pages_layout = QVBoxLayout(RightColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(RightColumn)
        self.menus.setObjectName(u"menus")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.verticalLayout = QVBoxLayout(self.menu_1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)

        self.btn_1_frame = QFrame(self.menu_1)
        self.btn_1_frame.setObjectName(u"btn_1_frame")
        self.btn_1_frame.setMinimumSize(QSize(0, 40))
        self.btn_1_frame.setMaximumSize(QSize(16777215, 40))
        self.btn_1_frame.setFrameShape(QFrame.NoFrame)
        self.btn_1_frame.setFrameShadow(QFrame.Raised)
        self.btn_1_menu_1_layout = QVBoxLayout(self.btn_1_frame)
        self.btn_1_menu_1_layout.setSpacing(0)
        self.btn_1_menu_1_layout.setObjectName(u"btn_1_menu_1_layout")
        self.btn_1_menu_1_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.btn_1_frame)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)
        self.scroll_area_1 = QScrollArea()

        self.scroll_area_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_1.setWidgetResizable(True)

        self.verticalLayout.addWidget(self.scroll_area_1)

        self.menus.addWidget(self.menu_1)
        self.menu_2 = QWidget()
        self.menu_2.setObjectName(u"menu_2")
        self.verticalLayout_2 = QVBoxLayout(self.menu_2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.btn_2_frame = QFrame(self.menu_2)
        self.btn_2_frame.setObjectName(u"btn_2_frame")
        self.btn_2_frame.setMinimumSize(QSize(0, 40))
        self.btn_2_frame.setMaximumSize(QSize(16777215, 40))
        self.btn_2_frame.setFrameShape(QFrame.NoFrame)
        self.btn_2_frame.setFrameShadow(QFrame.Raised)
        self.btn_1_menu_2_layout = QVBoxLayout(self.btn_2_frame)
        self.btn_1_menu_2_layout.setSpacing(0)
        self.btn_1_menu_2_layout.setObjectName(u"btn_1_menu_2_layout")
        self.btn_1_menu_2_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.btn_2_frame)
        font = QFont()
        font.setPointSize(16)
        self.label_2 = QLabel(self.menu_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font-size: 16pt")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.menus.addWidget(self.menu_2)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(RightColumn)

        self.menus.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(RightColumn)
    # setupUi

    def retranslateUi(self, RightColumn):
        RightColumn.setWindowTitle(QCoreApplication.translate("RightColumn", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("RightColumn", u"Menu 2 - Right Menu", None))
    # retranslateUi

